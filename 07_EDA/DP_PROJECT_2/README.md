# 📊 Data Preprocessing & Feature Engineering Project — Healthcare Dataset

## 🚀 Overview

This project applies **data preprocessing techniques** — handling missing values and outliers — on a real healthcare dataset of 700 patient records.
The goal is to prepare raw data for machine learning by improving its quality and reliability.

---

## 🎯 Objectives

* Handle missing values using multiple imputation techniques
* Detect and treat outliers using statistical methods
* Compare different preprocessing techniques
* Generate a clean dataset suitable for machine learning

---

## 📁 Dataset

The dataset (`healthcare_dataset_700_rows.csv`) contains **700 patient records** with the following features:

* `patient_id` → Unique identifier
* `age` → Age of patient
* `gender` → Male/Female
* `region` → Geographic region
* `bmi` → Body Mass Index
* `blood_pressure` → Blood pressure level
* `cholesterol` → Cholesterol level
* `glucose` → Glucose level
* `disease_risk` → Target variable (0 = Low, 1 = High)

### ⚠️ Data Characteristics

* `age` (5.0%), `gender` (4.0%), `region` (4.0%), `bmi` (2.86%), `cholesterol` (4.29%) and `glucose` (4.29%) contain **missing values**
* `bmi`, `blood_pressure`, `cholesterol` and `glucose` contain **outliers** (extreme high/low values)
* Real-world style healthcare data

---

## 🛠️ Techniques Used

### 🔹 Missing Value Handling

* Simple Imputation (Mean) — `bmi`, `cholesterol`
* Most Frequent (Mode) — `gender`, `region`
* Random Sampling + Missing Indicator — `bmi`
* KNN Imputation — `age`, `bmi`, `cholesterol`, `glucose`
* MICE (Multiple Imputation by Chained Equations) — `age`, `bmi`, `cholesterol`, `glucose`

---

### 🔹 Outlier Detection & Treatment

* Z-Score Method
* IQR (Interquartile Range)
* Percentile Capping
* Winsorization

---

## 📊 Final Approach

After comparing different techniques:

* **Best Imputation Method:** MICE — it models each numerical column as a function of the others, preserving relationships between variables better than mean/mode imputation alone.
* **Best Outlier Method:** IQR — robust to skewed data and does not assume a normal distribution.

These methods provided better data consistency and preserved relationships between variables.

---

## 📂 Project Structure

```
📁 Project Folder
│── 📄 healthcare_data_cleansing.ipynb   # Main notebook
│── 📄 healthcare_dataset_700_rows.csv   # Raw dataset
│── 📄 cleaned_health_data.csv           # Final cleaned dataset
│── 📄 README.md                         # Project documentation
```

---

## 📈 Output

* Cleaned dataset with:

  * No missing values (0 across all columns)
  * Reduced outliers (700 → 635 rows after IQR filtering)
* Dataset ready for machine learning models

---

## 📌 Key Learnings

* Importance of handling missing values properly
* Impact of outliers on data analysis
* Comparison of different preprocessing techniques
* Real-world data cleaning workflow

---

## 🚀 Conclusion

Data preprocessing is a crucial step in any data science project.
This project demonstrates how different techniques can significantly improve data quality and prepare a real healthcare dataset for accurate modeling.

## VIDEO LINK 

https://drive.google.com/file/d/1A8BW6nuTw03Kv2smtiJyd0p-vMcIxOF2/view?usp=sharing

