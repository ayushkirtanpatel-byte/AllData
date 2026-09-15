# Holistic Data Preparer — Final Project

**Duration:** 8 Days (1 hour/day)
**Role:** Junior Data Scientist, Fintech Company

## 📌 Objective
End-to-end Data Preprocessing & Feature Engineering on a **Customer Credit Risk**
dataset: from data understanding to cleaning, imputation, outlier handling, encoding,
scaling, transformations, and feature engineering — producing a dataset ready for
Machine Learning modeling (predicting **loan default**).

## 📁 Repository Structure
```
holistic-data-preparer/
├── README.md
├── requirements.txt
├── data/
│   ├── generate_data.py               # Script that creates all 4 raw data sources
│   ├── transactions.csv               # Source 1: CSV
│   ├── customer_metadata.json         # Source 2: JSON
│   ├── loan_repayment.db              # Source 3: SQL (SQLite)
│   └── economic_indicators_api.json   # Source 4: Dummy API payload
├── notebooks/
│   ├── Holistic_Data_Preparer.ipynb        # Main notebook (Parts A-H, fully executed)
│   └── Holistic_Data_Preparer_preview.html # HTML export for quick viewing (no Jupyter needed)
├── docs/
│   └── theory_concepts.pdf            # Theory & definitions for every concept used
└── outputs/
    └── final_cleaned_dataset.csv      # Final, ML-ready dataset
```

## 🗂 Dataset
A synthetic **Customer Credit Risk** dataset (1,000 customers) with:
- **Demographics:** age, gender, region, education, employment type
- **Financial details:** income, loan amount, loan purpose, repayment history, credit score
- **Behavioral attributes:** transactions, spending habits, missed payments
- **Target:** `default_flag` → 0 = No Default, 1 = Default

The data is intentionally spread across 4 sources (CSV, JSON, SQL, dummy API) and
contains injected missing values and outliers, so every preprocessing technique in the
notebook has real data to work on.

## ▶️ How to Run
```bash
pip install -r requirements.txt
python data/generate_data.py          # (re)generates the raw data sources
jupyter notebook notebooks/Holistic_Data_Preparer.ipynb
```
Or simply open `notebooks/Holistic_Data_Preparer_preview.html` in a browser to view the
fully executed notebook (code + outputs + charts) without installing anything.

## 📓 Notebook Contents
| Part | Topic |
|---|---|
| A | Conceptual Foundation — Data Analysis, Project Planning, Framing ML Problems, Tensors (NumPy) |
| B | Data Acquisition — CSV, JSON, SQL, Dummy API |
| C | Data Understanding & Cleaning — `.info()`, `.describe()`, data-quality report, 6 missing-value strategies |
| D | Outlier Handling — Z-score, IQR, Percentile, Winsorization |
| E | Feature Engineering — mixed/date variables, Ordinal/Label/One-Hot Encoding, Binning/Binarization/Quantile/K-Means Binning |
| F | Feature Scaling — Standardization, Normalization, Min-Max, MaxAbs, Robust |
| G | Feature Construction & Transformation — `FunctionTransformer`, `PowerTransformer`, `ColumnTransformer`, engineered features |
| H | Final Deliverable — cleaned dataset + written report |

## 📊 Final Output
`outputs/final_cleaned_dataset.csv` — a fully cleaned, encoded, scaled, and
feature-engineered dataset, ready to be split into train/test sets for a binary
classification model.

## 📄 Theory Document
`docs/theory_concepts.pdf` contains short definitions for every concept and technique
used in the notebook (Parts A-H), for quick revision.

## 🛠 Tech Stack
Python · pandas · NumPy · scikit-learn · SciPy · Matplotlib · Seaborn · SQLite

## ✅ Expected Outcome
- Understand how to plan and execute a complete data preprocessing workflow.
- Perform detailed data cleaning using imputation and outlier handling.
- Apply advanced encoding and scaling techniques.
- Construct and transform features to improve ML-readiness.
- Deliver a high-quality dataset ready to directly build a Machine Learning model.

---
*This project was completed as part of the "Holistic Data Preparer" final assignment.*
