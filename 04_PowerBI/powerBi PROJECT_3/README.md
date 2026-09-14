# 📊 Sales Data Analysis Project (Power BI)

## 📌 Project Overview
This project is based on sales data analysis using Power BI, where I worked on multiple tables and created a complete data model for analysis.

---

## 📂 Data Import
I imported the following datasets into Power BI:
- Sales_Fact  
- Returns_Fact  
- Customer_Dim  
- Product_Dim  
- Date_Dim  
- Region_Dim  

---

## 🔗 Data Modeling
- Created relationships between fact and dimension tables  
- Ensured proper connections for accurate analysis across:
  - Customer  
  - Product  
  - Region  
  - Date  

---

## 🧮 Calculated Columns
- **Profit** = SalesAmount - Cost  
- **Return Flag** → Identify returned products  
- **Customer Full Name** → First Name + Last Name  

---

## 📐 DAX Measures
- Total Sales → `SUM`  
- Total Cost  
- Total Profit → Sales - Cost  
- Return Rate → `DIVIDE`  
- Average Sale  

✔ Created a **Measure Table** to organize all DAX measures.

---

## 🎯 Filter Context & Functions
Used key DAX functions:
- `CALCULATE` → Modify filter context  
- `ALL` → Remove filters  
- `FILTER` → Apply custom conditions  

---

## 🧩 Other DAX Functions Used
- Aggregations: `SUM`, `AVERAGE`, `MAX`  
- Logic: `IF`, `SWITCH`  
- Counting: `DISTINCTCOUNT`  
- Text: `CONCATENATE`  
- Date: `YEAR`, `MONTH`  

---

## ⏳ Time Intelligence
- Year-to-Date → `TOTALYTD`  
- Previous Year Comparison → `SAMEPERIODLASTYEAR`  
- Running Total → `CALCULATE` + `DATESBETWEEN`  

---

## 📊 Visualization (Matrix)
Created a **Matrix visual** to analyze data based on:
- Region  
- Product Category  
- Customer Segment  
- Year & Month  

✔ Helps compare performance like a pivot table.

---

## 📘 Key Learnings
- Data Modeling  
- DAX Calculations  
- Filter Context  
- Time-Based Analysis  
- Data Visualization  

---

## ⚠️ Important Note
**QUICK MEASURE (YEAR-OVER-YEAR AND PREVIOUS MONTH) IS NOT WORKING IN MY PROJECT DUE TO DATE TABLE ISSUE.**
