"""
Core Data Preprocessing & Feature Engineering Pipeline
Customer Purchase Propensity Project
"""
import json
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats

RNG = np.random.default_rng(42)

# ----------------------------------------------------------------------
# STEP 2: DATA IMPORT
# ----------------------------------------------------------------------

# 2a. CSV - customer demographics
customers = pd.read_csv("data/customers.csv")

# 2b. JSON - transactions
with open("data/transactions.json") as f:
    transactions = pd.DataFrame(json.load(f))

# 2c. SQL - products (import using sqlite3, as instructed)
conn = sqlite3.connect(":memory:")
with open("data/products.sql") as f:
    conn.executescript(f.read())
products = pd.read_sql_query("SELECT * FROM products", conn)
conn.close()

# 2d. API - dummyjson.com/users (saved locally after fetching, since customers.csv
# only has 8 customers we map customer_id 101-108 -> dummyjson id 1-8 for demo)
with open("data/api_users_raw.json") as f:
    api_users = pd.json_normalize(json.load(f))
api_users = api_users.rename(columns={
    "id": "api_user_id",
    "company.department": "department",
    "company.title": "job_title",
    "address.city": "api_city",
    "address.country": "api_country",
})[["api_user_id", "email", "university", "department", "job_title", "api_city", "api_country"]]
api_users["customer_id"] = api_users["api_user_id"] + 100  # 1->101 ... 8->108

# ----------------------------------------------------------------------
# SYNTHETIC SUPPLEMENTARY FIELDS
# (customers.csv/transactions.json/products.sql do not contain signup_date,
#  education, satisfaction, or a purchase target column, all of which the
#  brief requires us to engineer against. We generate them here with a fixed
#  seed so the raw-data quality issues we need to demonstrate - missing
#  values, outliers, mixed-format IDs, mixed dtypes - are present and
#  reproducible. This is documented as a data limitation in the summary report.)
# ----------------------------------------------------------------------

n = len(customers)
signup_dates = pd.to_datetime("2024-01-01") + pd.to_timedelta(RNG.integers(0, 500, n), unit="D")
last_purchase = signup_dates + pd.to_timedelta(RNG.integers(5, 400, n), unit="D")

education_levels = RNG.choice(["High School", "Bachelor's", "Master's", "PhD"], size=n, p=[0.25, 0.4, 0.25, 0.1])
satisfaction = RNG.choice(["Low", "Medium", "High"], size=n, p=[0.2, 0.5, 0.3])
total_purchases = RNG.integers(1, 30, n)

customers["signup_date"] = signup_dates.strftime("%Y-%m-%d")
customers["last_purchase_date"] = last_purchase.strftime("%Y-%m-%d")
customers["education"] = education_levels
customers["satisfaction_level"] = satisfaction
customers["total_purchases"] = total_purchases

# purchase propensity target, weakly correlated with income/total_purchases
prob = 1 / (1 + np.exp(-((customers["income"] - customers["income"].mean()) / 15000
                          + (customers["total_purchases"] - 15) / 10)))
customers["purchased"] = RNG.binomial(1, prob)

# --- inject realistic messiness ---
# mixed-format customer IDs embedding letters (e.g. "CUST101") in a copy column
customers["customer_id_raw"] = customers["customer_id"].apply(lambda x: f"CUST{x}" if RNG.random() < 0.4 else str(x))

# missing values (MCAR-ish) in several columns
for col, frac in [("income", 0.2), ("age", 0.12), ("education", 0.15),
                   ("satisfaction_level", 0.12), ("last_purchase_date", 0.1)]:
    idx = customers.sample(frac=frac, random_state=RNG.integers(0, 10000)).index
    customers.loc[idx, col] = np.nan

# a couple of outliers in income and age
customers.loc[customers.sample(1, random_state=1).index, "income"] = 950000
customers.loc[customers.sample(1, random_state=2).index, "age"] = 121
customers.loc[customers.sample(1, random_state=3).index, "income"] = -500  # bad data entry

customers.to_csv("data/customers_raw_synthetic.csv", index=False)
print("Step 2 complete. Shapes:", customers.shape, transactions.shape, products.shape, api_users.shape)

# --- merge everything on customer_id / product_id ---
txn_products = transactions.merge(products, on="product_id", how="left")
txn_agg = txn_products.groupby("customer_id").agg(
    n_transactions=("transaction_id", "count"),
    total_spent=("amount", "sum"),
    avg_order_value=("amount", "mean"),
    fav_category=("category", lambda x: x.mode().iat[0] if not x.mode().empty else np.nan),
    most_common_payment=("payment_mode", lambda x: x.mode().iat[0] if not x.mode().empty else np.nan),
).reset_index()

df = customers.merge(txn_agg, on="customer_id", how="left").merge(api_users, on="customer_id", how="left")
print("\nMerged dataset shape:", df.shape)
print(df.info())
df.to_csv("data/merged_raw.csv", index=False)

# ----------------------------------------------------------------------
# STEP 6 (partial, needed before later steps): mixed / datetime handling
# ----------------------------------------------------------------------
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"], errors="coerce")
df["days_since_last_purchase"] = (pd.Timestamp("2025-10-15") - df["last_purchase_date"]).dt.days
df["days_since_signup"] = (pd.Timestamp("2025-10-15") - df["signup_date"]).dt.days

# handle mixed customer_id_raw: extract the numeric part
df["customer_id_clean"] = df["customer_id_raw"].astype(str).str.extract(r"(\d+)").astype(float)

print("\nStep 6 done - dates & mixed IDs handled")
print(df[["customer_id", "customer_id_raw", "customer_id_clean", "signup_date", "days_since_signup"]].head())

# ----------------------------------------------------------------------
# STEP 4: MISSING DATA - demonstrate multiple techniques (separate copies)
# ----------------------------------------------------------------------
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

num_cols_missing = ["income", "age"]
cat_cols_missing = ["education", "satisfaction_level"]

# 4a. Simple Imputer (mean for numeric, most_frequent for categorical)
df_simple = df.copy()
df_simple[num_cols_missing] = SimpleImputer(strategy="mean").fit_transform(df_simple[num_cols_missing])
df_simple[cat_cols_missing] = SimpleImputer(strategy="most_frequent").fit_transform(df_simple[cat_cols_missing])

# 4b. Most Frequent imputation applied to everything (mode-based)
df_mode = df.copy()
for c in num_cols_missing + cat_cols_missing:
    df_mode[c] = df_mode[c].fillna(df_mode[c].mode().iat[0])

# 4c. Missing indicator + random sample imputation
df_indicator = df.copy()
for c in num_cols_missing + cat_cols_missing:
    df_indicator[f"{c}_was_missing"] = df_indicator[c].isna().astype(int)
    observed = df_indicator[c].dropna()
    fill_vals = observed.sample(df_indicator[c].isna().sum(), replace=True, random_state=42).values
    df_indicator.loc[df_indicator[c].isna(), c] = fill_vals

# 4d. KNN Imputer (numeric only, multivariate)
df_knn = df.copy()
knn_input = df_knn[["income", "age", "total_purchases"]]
df_knn[["income", "age", "total_purchases"]] = KNNImputer(n_neighbors=3).fit_transform(knn_input)

# 4e. MICE (IterativeImputer) - chained imputation for correlated numeric features
df_mice = df.copy()
mice_input = df_mice[["income", "age", "total_purchases", "total_spent"]]
df_mice[["income", "age", "total_purchases", "total_spent"]] = IterativeImputer(random_state=42, max_iter=10).fit_transform(mice_input)

# 4f. Complete Case Analysis (drop rows with any missing, for comparison only)
df_cca = df.dropna(subset=num_cols_missing + cat_cols_missing)

print(f"\nStep 4 done. Complete-case rows retained: {len(df_cca)}/{len(df)}")

# choose KNN-imputed numeric + SimpleImputer categorical as the "winning" combo
# going forward (documented reasoning in the summary report)
df_final = df.copy()
df_final[["income", "age", "total_purchases"]] = df_knn[["income", "age", "total_purchases"]]
df_final[cat_cols_missing] = df_simple[cat_cols_missing]
df_final["last_purchase_date"] = df_final["last_purchase_date"].fillna(df_final["last_purchase_date"].median())
df_final["days_since_last_purchase"] = (pd.Timestamp("2025-10-15") - df_final["last_purchase_date"]).dt.days

# ----------------------------------------------------------------------
# STEP 5: OUTLIER DETECTION & HANDLING (on income, age)
# ----------------------------------------------------------------------
def zscore_outliers(s, thresh=3):
    z = np.abs(stats.zscore(s))
    return z > thresh

def iqr_outliers(s, k=1.5):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return (s < q1 - k * iqr) | (s > q3 + k * iqr)

def percentile_outliers(s, lower=0.01, upper=0.99):
    lo, hi = s.quantile(lower), s.quantile(upper)
    return (s < lo) | (s > hi)

z_out = zscore_outliers(df_final["income"])
iqr_out = iqr_outliers(df_final["income"])
pct_out = percentile_outliers(df_final["income"])
print(f"\nStep 5: Outliers in income -> Z-score: {z_out.sum()}, IQR: {iqr_out.sum()}, Percentile: {pct_out.sum()}")

# Winsorize to cap extreme values (1st/99th percentile) - applied to final df
for col in ["income", "age"]:
    lo, hi = df_final[col].quantile(0.01), df_final[col].quantile(0.99)
    df_final[col] = df_final[col].clip(lo, hi)

print("Income after winsorizing:\n", df_final["income"].describe())

# ----------------------------------------------------------------------
# STEP 7: ENCODING CATEGORICAL DATA
# ----------------------------------------------------------------------
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

df_final["gender_label_enc"] = LabelEncoder().fit_transform(df_final["gender"])

ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
city_ohe = ohe.fit_transform(df_final[["city"]])
city_ohe_df = pd.DataFrame(city_ohe, columns=[f"city_{c}" for c in ohe.categories_[0]], index=df_final.index)
df_final = pd.concat([df_final, city_ohe_df], axis=1)

education_order = [["High School", "Bachelor's", "Master's", "PhD"]]
df_final["education_ordinal"] = OrdinalEncoder(categories=education_order).fit_transform(df_final[["education"]])
satisfaction_order = [["Low", "Medium", "High"]]
df_final["satisfaction_ordinal"] = OrdinalEncoder(categories=satisfaction_order).fit_transform(df_final[["satisfaction_level"]])

# encoding numerical: binning income groups
df_final["income_group"] = pd.cut(df_final["income"], bins=[0, 40000, 55000, 70000, np.inf],
                                   labels=["Low", "Mid", "High", "Very High"])

print("\nStep 7 done. New encoded columns added.")

# ----------------------------------------------------------------------
# STEP 8: FEATURE SCALING
# ----------------------------------------------------------------------
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, Normalizer
from sklearn.compose import ColumnTransformer

scale_cols = ["income", "age", "total_spent"]
df_final[[f"{c}_standard" for c in scale_cols]] = StandardScaler().fit_transform(df_final[scale_cols])
df_final[[f"{c}_minmax" for c in scale_cols]] = MinMaxScaler().fit_transform(df_final[scale_cols])
df_final[[f"{c}_maxabs" for c in scale_cols]] = MaxAbsScaler().fit_transform(df_final[scale_cols])
df_final[[f"{c}_robust" for c in scale_cols]] = RobustScaler().fit_transform(df_final[scale_cols])
df_final[[f"{c}_norm" for c in scale_cols]] = Normalizer().fit_transform(df_final[scale_cols])

ct = ColumnTransformer([
    ("std", StandardScaler(), ["income"]),
    ("minmax", MinMaxScaler(), ["age"]),
], remainder="drop")
ct_out = ct.fit_transform(df_final)
print("\nStep 8 done. ColumnTransformer output shape:", ct_out.shape)

# ----------------------------------------------------------------------
# STEP 9: FEATURE CONSTRUCTION & TRANSFORMATION
# ----------------------------------------------------------------------
from sklearn.preprocessing import FunctionTransformer, PowerTransformer, KBinsDiscretizer

df_final["purchase_per_day"] = df_final["total_purchases"] / df_final["days_since_signup"].replace(0, np.nan)
df_final["purchase_per_day"] = df_final["purchase_per_day"].fillna(0)

df_final["income_log"] = FunctionTransformer(np.log1p).fit_transform(df_final[["income"]])
df_final["income_sqrt"] = FunctionTransformer(np.sqrt).fit_transform(df_final[["income"]].clip(lower=0))
df_final["income_reciprocal"] = FunctionTransformer(lambda x: 1 / (x + 1)).fit_transform(df_final[["income"]])

pt_yj = PowerTransformer(method="yeo-johnson")
df_final["income_yeojohnson"] = pt_yj.fit_transform(df_final[["income"]])
pt_bc = PowerTransformer(method="box-cox")
df_final["income_boxcox"] = pt_bc.fit_transform(df_final[["income"]].clip(lower=1))

kbd = KBinsDiscretizer(n_bins=4, encode="ordinal", strategy="quantile")
df_final["income_binned"] = kbd.fit_transform(df_final[["income"]])

df_final["frequent_buyer"] = (df_final["total_purchases"] > df_final["total_purchases"].median()).astype(int)

print("\nStep 9 done. Feature construction complete. Final shape:", df_final.shape)

# ----------------------------------------------------------------------
# STEP 10: FINAL OUTPUT
# ----------------------------------------------------------------------
df_final.to_csv("outputs/processed_customer_data.csv", index=False)
print("\nSaved outputs/processed_customer_data.csv with shape", df_final.shape)
print(df_final.columns.tolist())
