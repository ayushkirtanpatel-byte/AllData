# 📊 Data Preprocessing and Feature Engineering

## 🎯 Project Overview

This project focuses on **Data Preprocessing, Data Understanding, Data Cleaning, Exploratory Data Analysis (EDA), and Data Profiling** using a real-world customer churn dataset.

The objective is to prepare raw data for machine learning by applying data acquisition techniques, cleaning procedures, exploratory analysis, and profiling methods.

---

# 📌 Problem Statement

A consumer insights company has provided customer purchase behavior data collected from multiple sources such as:

* 📄 CSV Files
* 📑 JSON Files
* 🗄️ SQL Databases
* 🌐 APIs

The goal is to analyze customer behavior and frame a machine learning problem to predict customer churn.

---

# 🎯 Objectives

* Understand the fundamentals of data analysis.
* Learn the role of tensors in machine learning.
* Load data from multiple sources.
* Perform data cleaning and preprocessing.
* Conduct Exploratory Data Analysis (EDA).
* Generate data profiling insights.
* Prepare the dataset for machine learning applications.

---

# 📂 Dataset Information

### Dataset Name

Customer Churn Dataset

### Features

| Feature           | Description                        |
| ----------------- | ---------------------------------- |
| CustomerID        | Unique customer identifier         |
| Age               | Customer age                       |
| Gender            | Customer gender                    |
| Tenure            | Duration of customer relationship  |
| Usage Frequency   | Frequency of product/service usage |
| Support Calls     | Number of support calls            |
| Payment Delay     | Payment delay count                |
| Subscription Type | Customer subscription plan         |
| Contract Length   | Subscription contract duration     |
| Total Spend       | Total customer spending            |
| Last Interaction  | Days since last interaction        |
| Churn             | Target variable                    |

### Target Variable

**Churn**

* 0 → Customer Retained
* 1 → Customer Churned

---

# 🧠 Part A: Fundamentals

## What is Data Analysis?

Data Analysis is the process of collecting, cleaning, transforming, and interpreting data to extract meaningful insights and support decision-making.

---

## Data Science Project Lifecycle

1. Business Understanding
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Model Building
7. Model Evaluation
8. Deployment

---

## Machine Learning Problem Statement

Build a machine learning model that predicts whether a customer will churn based on customer behavior and spending patterns.

---

## Tensors

A Tensor is a multi-dimensional data structure used in Machine Learning and Deep Learning.

### Types of Tensors

* Scalar (0D)
* Vector (1D)
* Matrix (2D)
* Tensor (3D+)

---

# 📥 Part B: Data Acquisition

Data was collected and demonstrated using multiple sources:

### CSV File

* Loaded using Pandas.

### JSON File

* Parsed using Python JSON library.

### SQL Database

* Connected using SQLite.

### API

* Data fetched using Random User API.

---

# 🧹 Part C: Data Understanding & Cleaning

The following preprocessing steps were performed:

### Initial Exploration

* `head()`
* `info()`
* `describe()`

### Data Quality Checks

* Missing Value Detection
* Duplicate Record Detection
* Data Type Verification

### Cleaning Operations

* Removed duplicate records.
* Verified data consistency.
* Removed irrelevant columns where required.

---

# 📊 Part D: Exploratory Data Analysis (EDA)

## 🔹 Univariate Analysis

Performed analysis on:

* Age Distribution
* Total Spend Distribution
* Usage Frequency Distribution
* Churn Distribution

### Goal

Understand the distribution of individual variables.

---

## 🔹 Bivariate Analysis

Performed analysis on:

* Gender vs Churn
* Total Spend vs Churn
* Subscription Type vs Churn
* Contract Length vs Churn

### Goal

Understand relationships between two variables.

---

## 🔹 Multivariate Analysis

Performed analysis using:

### Correlation Heatmap

Used to identify relationships among numerical features.

### Pair Plot

Used to identify feature interactions and patterns.

---

# 📑 Part E: Data Profiling

Manual data profiling was performed to summarize:

### Missing Values

Checked using:

```python
df.isnull().sum()
```

### Descriptive Statistics

Generated using:

```python
df.describe()
```

### Correlation Analysis

Performed using:

```python
df.corr()
```

### Data Quality Checks

* Missing Values
* Duplicate Records
* Data Types
* Correlation Analysis

---

# 📈 Key Insights

* Customer tenure influences churn behavior.
* Spending patterns show significant variation among customers.
* Subscription type impacts customer retention.
* Usage frequency is associated with churn probability.
* Correlation analysis helps identify important predictive features.

---

# 🛠️ Technologies Used

### Programming Language

* Python 🐍

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* JSON
* SQLite3
* Requests

### Development Environment

* Jupyter Notebook
* Visual Studio Code

---

# 📁 Project Structure

```text
Data_Preprocessing_Project/
│
├── customer_churn_dataset-testing-master.csv
├── sample.json
├── customer.db
├── Data_Preprocessing_Project.ipynb
├── Theory_Notes.ipynb
├── README.md
└── screenshots/
```

---

# ✅ Expected Outcomes

By completing this project:

* Gain hands-on experience in data acquisition.
* Understand tensors and their role in machine learning.
* Perform data cleaning and preprocessing.
* Conduct EDA (Univariate, Bivariate, Multivariate).
* Generate profiling insights.
* Prepare datasets for machine learning workflows.

---

# 🚀 Conclusion

This project demonstrates the complete workflow of data preprocessing and exploratory data analysis. Various data acquisition techniques, cleaning procedures, visualization methods, and profiling approaches were applied to transform raw customer data into meaningful insights suitable for machine learning applications.

---

## 👨‍💻 Author

**Ayush**

Junior Data Analyst Project

Data Preprocessing and Feature Engineering
