# 🛒 Customer Purchase Propensity
### Data Cleaning & Feature Engineering Pipeline

> **Junior Data Analyst Project**  
> A complete preprocessing and feature-engineering pipeline that combines data from **CSV, JSON, SQL, and API sources** and prepares it for a future Machine Learning model to predict whether a customer will make a purchase.

**Target variable:** `purchased` — Binary Classification  
**Scope:** Data cleaning, preprocessing, EDA, feature engineering & final dataset preparation  
**ML Model Training:** Not included in this repository

---

## 📌 Project Overview

The goal of this project is to transform multiple raw customer-related data sources into a **clean, consistent, analysis-ready dataset**.

The pipeline demonstrates practical data-preprocessing techniques including:

- Data integration from multiple sources
- Exploratory Data Analysis (EDA)
- Missing-value treatment
- Outlier detection and handling
- Date and mixed-format variable processing
- Categorical encoding
- Feature scaling
- Feature construction and transformation
- Final dataset export for future ML development

---

## 🗂️ Repository Structure

```text
.
├── data/
│   ├── customers.csv                 # Raw customer demographics
│   ├── transactions.json             # Raw transaction records
│   ├── products.sql                  # Product table (SQL DDL + INSERTs)
│   ├── api_users_raw.json            # Cached API response
│   ├── customers_raw_synthetic.csv  # Customers + synthesized fields
│   └── merged_raw.csv                # Merged data before cleaning
│
├── notebooks/
│   └── DataPreprocessing.ipynb       # Full executed walkthrough (Steps 1–10)
│
├── outputs/
│   ├── processed_customer_data.csv   # Final engineered dataset
│   └── eda_*.png                     # Saved EDA visualizations
│
├── feature_pipeline.py               # Reusable standalone pipeline
├── Summary_Report.md                 # One-page project summary
└── README.md                          # Project documentation
```

---

## 📊 Data Sources

| Source | File / Endpoint | Description |
|---|---|---|
| CSV | `customers.csv` | Customer demographics and IDs — 8 customers |
| JSON | `transactions.json` | 8 transaction records |
| SQL | `products.sql` | 6-row product table imported using `sqlite3` |
| API | `https://dummyjson.com/users` | Public API data fetched once and cached locally |

### 🔗 API Join Note

The public API contains demo users rather than the actual 8 customer records.

For this exercise, customer IDs **101–108** are mapped to DummyJSON user IDs **1–8** using:

```text
customer_id = api_user_id + 100
```

This is a **synthetic mapping created only for the exercise** and should not be interpreted as a real-world customer key.

---

## ⚠️ Synthetic Data Note

The original raw files do not contain some variables required by the project brief and ML framing, including:

- `signup_date`
- `last_purchase_date`
- `education`
- `satisfaction_level`
- `purchased`

These fields are generated in **Step 2** using a fixed random seed:

```python
np.random.default_rng(42)
```

The same step also introduces:

- Missing values
- Outliers
- Mixed-format customer IDs

This allows the required cleaning and preprocessing techniques to be demonstrated on realistic data-quality scenarios.

> **Transparency:** The synthesized fields and transformations are explicitly documented in the notebook and `Summary_Report.md`.

---

## 🔄 End-to-End Pipeline

### 1️⃣ Project Planning & ML Problem Framing
Define the business/ML problem as a **binary classification task** using the `purchased` target.

### 2️⃣ Data Import & Integration
Import and combine data from:

- CSV
- JSON
- SQL
- API

Data is merged using relevant keys such as `customer_id` and `product_id`.

### 3️⃣ Exploratory Data Analysis (EDA)
Perform:

- **Univariate analysis** — distributions, histograms, skewness
- **Bivariate analysis** — target correlations and boxplots
- **Multivariate analysis** — heatmap, pairplot and grouped statistics

### 4️⃣ Missing-Value Treatment
Compare multiple approaches:

- Simple Imputer
- Mode imputation
- Missing indicators + random-sample imputation
- KNN Imputer
- MICE / `IterativeImputer`
- Complete Case Analysis

The approaches are evaluated before selecting the method carried forward.

### 5️⃣ Outlier Detection & Treatment
Use:

- Z-score
- IQR method
- Percentile method
- Winsorizing

### 6️⃣ Datetime & Mixed Variables
Process:

- Date parsing
- `days_since_signup`
- `days_since_last_purchase`
- Regex-based extraction of numeric IDs from mixed-format strings

### 7️⃣ Categorical Encoding
Apply:

- Label Encoding
- One-Hot Encoding
- Ordinal Encoding
- Education / satisfaction encoding
- Income binning

### 8️⃣ Feature Scaling
Evaluate:

- `StandardScaler`
- `MinMaxScaler`
- `MaxAbsScaler`
- `RobustScaler`
- `Normalizer`

A `ColumnTransformer` is used to apply appropriate transformations to different feature groups.

### 9️⃣ Feature Construction & Transformation
Create and transform features using:

- Interaction features
- `FunctionTransformer`
  - Log
  - Square root
  - Reciprocal
- `PowerTransformer`
  - Box-Cox
  - Yeo-Johnson
- Quantile binning
- Binarization

### 🔟 Final Dataset Export
The final engineered dataset is exported to:

```text
outputs/processed_customer_data.csv
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation & preprocessing |
| NumPy | Numerical operations & synthetic data generation |
| Scikit-learn | Imputation, encoding, scaling & transformations |
| SciPy | Statistical processing |
| Matplotlib | Data visualization |
| Seaborn | EDA visualizations |
| SQLite3 | SQL data import |
| Jupyter Notebook | Interactive analysis & documentation |

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
```

### 2. Run the Standalone Pipeline

```bash
python feature_pipeline.py
```

This executes the preprocessing pipeline and generates:

```text
outputs/processed_customer_data.csv
```

### 3. Run the Full Notebook

For the complete step-by-step walkthrough with EDA charts:

```bash
jupyter nbconvert --to notebook --execute notebooks/DataPreprocessing.ipynb
```

---

## 📈 Project Outputs

The project produces:

- Cleaned and transformed customer data
- Engineered ML-ready features
- EDA visualizations
- Final processed dataset
- Documented preprocessing decisions

### Final Deliverable

```text
outputs/processed_customer_data.csv
```

---

## 🧪 Key Preprocessing Techniques Covered

| Area | Techniques |
|---|---|
| Missing Data | Simple Imputer, Mode, KNN, MICE, Missing Indicators |
| Outliers | Z-score, IQR, Percentiles, Winsorizing |
| Datetime | Date parsing, date-difference features |
| IDs | Regex-based numeric extraction |
| Encoding | Label, One-Hot, Ordinal |
| Scaling | Standard, MinMax, MaxAbs, Robust, Normalizer |
| Transformations | Log, Sqrt, Reciprocal, Box-Cox, Yeo-Johnson |
| Feature Engineering | Interactions, Binning, Binarization |
| Pipeline | ColumnTransformer |

---

## 📚 Project Documentation

For a concise explanation of the major data-quality issues, preprocessing decisions, and the techniques carried forward, see:

**[`Summary_Report.md`](Summary_Report.md)**

For the complete analysis and visual walkthrough, see:

**[`notebooks/DataPreprocessing.ipynb`](notebooks/DataPreprocessing.ipynb)**

---

## 🎯 Final Objective

The final output of this project is a **clean, transformed and feature-engineered customer dataset** that can serve as the foundation for a future Machine Learning model predicting customer purchase behavior.

> **This repository focuses on preprocessing and feature engineering only. No ML model is trained here.**

---

### 👨‍💻 Project Status

**Status:** ✅ Data preprocessing & feature engineering completed  
**Final Output:** `outputs/processed_customer_data.csv`  
**Next Step:** Build and evaluate a Machine Learning classification model
