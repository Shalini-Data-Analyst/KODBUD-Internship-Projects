🏥 Healthcare Data Cleaning & Preparation (Excel Project)
📌 Project Overview

This project focuses on cleaning and preparing a healthcare dataset using Microsoft Excel. The goal was to transform raw, 



## 🛠 Tools Used
- Microsoft Excel
- Pivot Tables
- Pivot Charts
- Slicers
- Dashboard Design

---

## 📊 Dataset Features
- BMI & HBA1C
- Heart Issues
- Cancer History
- Smoking Status
- Weight Status
- Diabetes Status
- Hospital Tier
- City Tier
- Healthcare Charges

---


---


unstructured data into a clean, consistent, and analysis-ready format.

🎯 Objective

To identify and remove irrelevant and inconsistent data

To handle missing values and duplicate records

To standardize text formatting for better readability

To prepare a structured dataset suitable for analysis and visualization

📂 Dataset Description

The dataset contains patient-related information with the following columns:

Customer ID

First Name

Middle Name

Last Name

Unnamed Columns (irrelevant data)

🧹 Data Cleaning Steps
1. Initial Data Inspection

Reviewed dataset using Excel filters and sorting

Identified missing values, duplicates, and unnecessary columns

2. Removal of Irrelevant Columns

Deleted columns:

Unnamed: 4

Unnamed: 5

These columns contained mostly null or unusable data

3. Handling Missing Values

Checked for blanks using filters

No critical missing values found in key columns

4. Removing Duplicates

Used Data → Remove Duplicates feature

Ensured all records are unique

5. Standardizing Column Names

Renamed columns for consistency:

Customer ID → customer_id

First Name → first_name

Middle Name → middle_name

Last Name → last_name

6. Cleaning Text Data

Removed extra spaces using TRIM()

Standardized capitalization using PROPER()

Example Formula:

=PROPER(TRIM(A2))
7. Data Consistency Check

Ensured uniform formatting across all rows

Verified no blank rows or inconsistent entries

## 🔍 Key Analysis
- Charges by Weight Status  
- Diabetes vs Weight Category  
- Charges vs Age  
- Impact of Smoking & Cancer History  
- Medical indicators (BMI, HBA1C) comparison  

---

## ✅ Skills Demonstrated
- Data Cleaning
- Pivot Table Analysis
- Dashboard Creation
- Slicer Connections
- Data Visualization
- Healthcare Data Interpretation

✅ Final Dataset

Cleaned and structured dataset

Removed duplicates and unnecessary columns

Standardized naming conventions

🛠️ Tools Used

Microsoft Excel

📊 Key Excel Features Used

Filters & Sorting

Remove Duplicates Tool

TRIM() Function

PROPER() Function

🚀 Outcome

The dataset is now:

Clean and consistent

Free from duplicates and irrelevant data

Ready for data analysis, visualization, or machine learning

📌 Future Improvements

Perform data visualization (charts/dashboards)

Apply statistical analysis

Integrate with tools like Power BI or Python

Author - Shalini M

