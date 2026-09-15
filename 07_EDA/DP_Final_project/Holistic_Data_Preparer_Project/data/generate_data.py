"""
Generates the synthetic multi-source Customer Credit Risk dataset used
throughout the Holistic Data Preparer project.

Sources created (mirrors the real-world scenario in the assignment):
1. transactions.csv        -> main transactions dataset (CSV)
2. customer_metadata.json  -> customer demographic metadata (JSON)
3. loan_repayment.db       -> repayment history (SQL / SQLite table)
4. economic_indicators_api.json -> "fetched" from a dummy external API
"""

import numpy as np
import pandas as pd
import json
import sqlite3
import os

np.random.seed(42)
N = 1000  # number of customers

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

customer_id = [f"CUST{100000+i}" for i in range(N)]

# ---------------------------------------------------------------
# Base demographic / financial attributes
# ---------------------------------------------------------------
age = np.random.randint(21, 65, N).astype(float)
gender = np.random.choice(["Male", "Female", "Other"], N, p=[0.48, 0.48, 0.04])
region = np.random.choice(["North", "South", "East", "West"], N)
education_level = np.random.choice(
    ["Primary", "Secondary", "Graduate", "Post-Graduate"], N, p=[0.1, 0.3, 0.4, 0.2]
)
employment_type = np.random.choice(
    ["Salaried", "Self-Employed", "Unemployed"], N, p=[0.6, 0.3, 0.1]
)

annual_income = np.random.lognormal(mean=12.8, sigma=0.6, size=N)  # in INR
loan_amount = annual_income * np.random.uniform(0.1, 0.9, N)
loan_purpose = np.random.choice(
    ["Home", "Car", "Education", "Business", "Other"], N
)
credit_score = np.random.normal(650, 80, N)
repayment_history = np.random.poisson(1.2, N)  # missed payments in last 12 months
transaction_count = np.random.poisson(45, N)   # transactions in last 6 months
spending_ratio = np.random.beta(2, 5, N) * 100  # spending-to-income %

join_date = pd.to_datetime(
    np.random.choice(pd.date_range("2015-01-01", "2025-12-31"), N)
)

# ---------------------------------------------------------------
# Target variable: loan default, weakly dependent on credit_score /
# repayment_history / spending_ratio so the dataset is not pure noise
# ---------------------------------------------------------------
risk_score = (
    (700 - credit_score) / 100
    + repayment_history * 0.4
    + spending_ratio / 50
    + np.random.normal(0, 1, N)
)
default_flag = (risk_score > np.percentile(risk_score, 75)).astype(int)

# ---------------------------------------------------------------
# Inject missing values (as documented in the dataset spec)
# ---------------------------------------------------------------
def inject_missing(arr, frac, dtype=float):
    arr = np.array(arr, dtype=object)
    idx = np.random.choice(len(arr), size=int(len(arr) * frac), replace=False)
    arr[idx] = np.nan
    return arr

age = inject_missing(age, 0.06)
annual_income = inject_missing(annual_income, 0.05)
credit_score = inject_missing(credit_score, 0.05)
employment_type = inject_missing(employment_type, 0.04)
gender = inject_missing(gender, 0.03)

# ---------------------------------------------------------------
# Inject outliers
# ---------------------------------------------------------------
out_idx = np.random.choice(N, size=15, replace=False)
annual_income = np.array(annual_income, dtype=object)
for i in out_idx:
    if annual_income[i] is not np.nan and not (isinstance(annual_income[i], float) and np.isnan(annual_income[i])):
        annual_income[i] = float(annual_income[i]) * np.random.uniform(8, 15)

out_idx2 = np.random.choice(N, size=15, replace=False)
loan_amount = np.array(loan_amount, dtype=object)
for i in out_idx2:
    loan_amount[i] = float(loan_amount[i]) * np.random.uniform(5, 10)

out_idx3 = np.random.choice(N, size=10, replace=False)
credit_score = np.array(credit_score, dtype=object)
for i in out_idx3:
    if not (isinstance(credit_score[i], float) and np.isnan(credit_score[i])):
        credit_score[i] = float(np.random.choice([250, 900, 920, 240]))

# ---------------------------------------------------------------
# Assemble master frame (in-memory only, then split across sources)
# ---------------------------------------------------------------
master = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "gender": gender,
    "region": region,
    "education_level": education_level,
    "employment_type": employment_type,
    "annual_income": annual_income,
    "loan_amount": loan_amount,
    "loan_purpose": loan_purpose,
    "credit_score": credit_score,
    "repayment_history": repayment_history,
    "transaction_count": transaction_count,
    "spending_ratio": spending_ratio,
    "join_date": join_date.astype(str),
    "default_flag": default_flag,
})

# ============================================================
# SOURCE 1: transactions.csv  (main transactions / financial data)
# ============================================================
transactions_cols = [
    "customer_id", "annual_income", "loan_amount", "loan_purpose",
    "credit_score", "transaction_count", "spending_ratio", "default_flag",
]
master[transactions_cols].to_csv(os.path.join(OUT_DIR, "transactions.csv"), index=False)

# ============================================================
# SOURCE 2: customer_metadata.json (demographics)
# ============================================================
metadata_cols = [
    "customer_id", "age", "gender", "region", "education_level",
    "employment_type", "join_date",
]
metadata_records = json.loads(master[metadata_cols].to_json(orient="records"))
with open(os.path.join(OUT_DIR, "customer_metadata.json"), "w") as f:
    json.dump(metadata_records, f, indent=2)

# ============================================================
# SOURCE 3: loan_repayment.db (SQLite table -> simulates SQL source)
# ============================================================
db_path = os.path.join(OUT_DIR, "loan_repayment.db")
if os.path.exists(db_path):
    os.remove(db_path)
conn = sqlite3.connect(db_path)
master[["customer_id", "repayment_history"]].to_sql(
    "repayment_history", conn, index=False, if_exists="replace"
)
conn.close()

# ============================================================
# SOURCE 4: economic_indicators_api.json (dummy external API payload)
# Region level macro-economic indicators
# ============================================================
regions = ["North", "South", "East", "West"]
api_payload = {
    "status": "success",
    "source": "dummy-economic-api",
    "data": [
        {
            "region": r,
            "inflation_rate": round(np.random.uniform(4.0, 7.5), 2),
            "unemployment_rate": round(np.random.uniform(3.0, 9.0), 2),
            "avg_interest_rate": round(np.random.uniform(7.0, 12.0), 2),
        }
        for r in regions
    ],
}
with open(os.path.join(OUT_DIR, "economic_indicators_api.json"), "w") as f:
    json.dump(api_payload, f, indent=2)

print("Generated data sources in:", OUT_DIR)
print(" - transactions.csv:", transactions_cols)
print(" - customer_metadata.json:", metadata_cols)
print(" - loan_repayment.db (table: repayment_history)")
print(" - economic_indicators_api.json (simulated API)")
