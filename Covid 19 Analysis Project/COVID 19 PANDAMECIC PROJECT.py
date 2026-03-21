import pandas as pd
df=pd.read_csv(r"C:\Users\shalu\New folder\Total_World_covid-19.csv")
##EXPLORATORY DATA ANALYSIS
print(df)
print(df.columns)
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.nunique())
print(df.isnull().sum())
print(df.drop_duplicates())
print(df['Critical'].isnull().sum())
print(df.fillna(0,inplace=True))
print(df.isnull().sum())
Total_Deaths=(df['Deaths'].sum())
print(Total_Deaths)
#Libraries installation 
import matplotlib.pyplot as plt
import seaborn as sns

#Top 10 Countries by Confirmed Cases (Bar Chart)
top10 = df.sort_values(by='Confirmed', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='Confirmed', y='Country', data=top10,color='green')

plt.title("Top 10 Countries by Confirmed COVID Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("Country")
plt.show()

#Death vs Confirmed (Scatter Plot)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Confirmed', y='Deaths', data=df,color='green')
plt.title("Confirmed vs Deaths")
plt.show()

#Distribution of Cases (Histogram)
plt.figure(figsize=(8,5))
sns.histplot(df['Confirmed'], bins=30, kde=True)
plt.title("Distribution of Confirmed Cases")
plt.show()

#Correlation Heatmap
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.show()

#Active vs Recovered
plt.figure(figsize=(8,6))
sns.scatterplot(x='Recovered', y='Active', data=df,color='green')
plt.title("Recovered vs Active Cases")
plt.show()

#Top 10 Countries with Labels
plt.figure(figsize=(10,6))
ax = sns.barplot(x='Deaths', y='Country', data=top10,color='green')

for i in ax.containers:
    ax.bar_label(i)

plt.title("Top 10 Countries with Labels")
plt.show()


#Top 5 Countries Share
top5 = df.sort_values(by='Confirmed', ascending=False).head(5)

plt.figure(figsize=(6,6))
plt.pie(top5['Confirmed'], labels=top5['Country'], autopct='%1.1f%%')

plt.title("Top 5 Countries Share")
plt.show()