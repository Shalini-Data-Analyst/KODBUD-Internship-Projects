🦠 COVID-19 Data Analysis Project
📌 Project Overview

This project focuses on Exploratory Data Analysis (EDA) of global COVID-19 data using Python. The goal is to analyze trends, identify patterns, and visualize the impact of the pandemic across different countries.

🎯 Objectives
Analyze COVID-19 dataset to understand global trends
Identify top affected countries based on confirmed cases and deaths
Explore relationships between key variables (Confirmed, Deaths, Recovered, Active)
Create meaningful visualizations for better insights
-------

🛠️ Tools & Technologies
Python
Pandas – Data cleaning & analysis
Matplotlib – Data visualization
Seaborn – Advanced visualization
--------

📂 Dataset
Dataset used: Global COVID-19 Data
File: Total_World_covid-19.csv
Contains:
Country
Confirmed Cases
Deaths
Recovered Cases
Active Cases
Critical Cases
---------

🔍 Data Cleaning Steps
Checked dataset structure using .info(), .shape(), .columns
Handled missing values using fillna(0)
Removed duplicate records
Verified null values before and after cleaning
Converted data into proper formats for analysis
---------

📊 Exploratory Data Analysis (EDA)
✔️ Basic Analysis
Summary statistics using .describe()
Unique values count
Data types verification
✔️ Key Metrics
Total Deaths calculated from dataset
📈 Visualizations
🔹 Top 10 Countries by Confirmed Cases
Bar chart showing most affected countries
🔹 Confirmed vs Deaths
Scatter plot showing relationship between cases and deaths
🔹 Distribution of Confirmed Cases
Histogram with KDE curve
🔹 Correlation Heatmap
Shows relationships between numerical variables
🔹 Recovered vs Active Cases
Scatter plot to understand recovery trends
🔹 Top 10 Countries (Deaths with Labels)
Bar chart with data labels
🔹 Top 5 Countries Share
Pie chart showing contribution of top countries
📌 Key Insights
A small number of countries contribute to the majority of cases
Strong positive correlation between confirmed cases and deaths
Recovery trends vary significantly across countries
Data visualization helps quickly identify high-risk regions
▶️ How to Run the Project
Clone the repository:
git clone https://github.com/your-username/covid19-analysis.git
Install required libraries:
pip install pandas matplotlib seaborn
Run the script:
python covid_analysis.py
📷 Sample Output
Bar charts, scatter plots, heatmaps, and pie charts generated using Seaborn & Matplotlib
🚀 Future Improvements
Add time-series analysis
Build an interactive dashboard (Power BI / Tableau / Streamlit)
Include predictive modeling using machine learning
👩‍💻 Author

Shalini M
Aspiring Data Analyst

⭐ Conclusion

This project demonstrates strong skills in:

Data cleaning
Exploratory Data Analysis
Data visualization

It serves as a solid foundation for real-world data analysis projects.