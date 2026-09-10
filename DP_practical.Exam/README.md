# Customer Purchase Propensity — Data Cleaning & Feature Engineering Pipeline

Junior Data Analyst project: clean, preprocess, and engineer features from multiple raw
sources (CSV, JSON, SQL, API) to prepare a dataset for a future ML model that predicts
whether a customer will make a purchase (`purchased`, binary classification). No model
is trained here — this repo covers preprocessing and feature engineering only.

## Repo structure
```
.
├── data/
│   ├── customers.csv               # raw customer demographics (given)
│   ├── transactions.json           # raw transaction records (given)
│   ├── products.sql                # raw product table, SQL DDL + INSERTs (given)
│   ├── api_users_raw.json          # cached response from https://dummyjson.com/users
│   ├── customers_raw_synthetic.csv # customers.csv + synthesized fields (see note below)
│   └── merged_raw.csv              # customers + transactions + products + API, pre-cleaning
├── notebooks/
│   └── DataPreprocessing.ipynb     # full, executed walkthrough (Steps 1–10) with EDA plots
├── outputs/
│   ├── processed_customer_data.csv # final engineered dataset (Step 10 deliverable)
│   └── eda_*.png                   # saved EDA charts (histograms, heatmap, pairplot, boxplots)
├── feature_pipeline.py             # standalone, reusable script version of the pipeline
├── Summary_Report.md               # 1-page summary: techniques, issues, what worked best
└── README.md
```

## Data sources
- `customers.csv` — customer demographics and IDs (8 customers)
- `transactions.json` — 8 transaction records
- `products.sql` — 6-row product table, imported into pandas via `sqlite3`
- API — `https://dummyjson.com/users`, fetched once and cached as `data/api_users_raw.json`

**Note on the API join:** the public API returns arbitrary demo users, not real records
for these 8 customers. To demonstrate a working 4-source join as required by the brief,
customer IDs 101–108 are mapped to dummyjson user IDs 1–8 (`customer_id = api_user_id + 100`).
This is a synthetic mapping for the exercise, not a real-world key.

**Note on synthesized columns:** the raw files don't include `signup_date`,
`last_purchase_date`, `education`, `satisfaction_level`, or a purchase target — all of
which later pipeline steps (and the ML framing) require. These are generated with a
fixed random seed (`np.random.default_rng(42)`) in Step 2 of the notebook, along with
injected missing values, outliers, and mixed-format customer IDs, so the cleaning
techniques required by the brief have real material to operate on. This is called out
explicitly in the notebook and in `Summary_Report.md` rather than hidden.

## How to run
```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
python feature_pipeline.py          # runs the full pipeline, writes outputs/processed_customer_data.csv
# or, for the full narrative + charts:
jupyter nbconvert --to notebook --execute notebooks/DataPreprocessing.ipynb
```

## Pipeline steps covered
1. Project planning & ML problem framing (binary classification: `purchased`)
2. Data import from CSV, JSON, SQL, and API; merge on `customer_id` / `product_id`
3. EDA — univariate (histograms, skew), bivariate (correlation with target, boxplots),
   multivariate (heatmap, pairplot, grouped stats)
4. Missing data — Simple Imputer, mode imputation, missing-indicator + random-sample,
   KNN Imputer, MICE (`IterativeImputer`), Complete Case Analysis (compared, not used)
5. Outlier detection — Z-score, IQR, percentile methods, plus Winsorizing
6. Mixed & datetime variables — date parsing, `days_since_signup` /
   `days_since_last_purchase`, regex extraction of numeric IDs from mixed-format strings
7. Encoding — Label, One-Hot, Ordinal (education/satisfaction), income binning
8. Feature scaling — StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler,
   Normalizer, and a `ColumnTransformer` applying several at once
9. Feature construction — interaction feature, `FunctionTransformer` (log/sqrt/reciprocal),
   `PowerTransformer` (Box-Cox & Yeo-Johnson), quantile binning, binarization
10. Final export to `outputs/processed_customer_data.csv`

See `Summary_Report.md` for the biggest data-quality issues found and which
imputation/scaling combination was carried forward.
