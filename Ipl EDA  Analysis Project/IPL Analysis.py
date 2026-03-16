#importing pandas
import pandas as pd
df=pd.read_csv(r"C:\Users\shalu\Downloads\ipl dataset.csv")

##Exploratory data Analysis

print(df.columns)
print(df.head())
print(df.describe)
print(df.info())
print(df.shape)
print(df.drop(["Unnamed: 0","COST IN ₹ (CR.)"],axis=1,inplace=True))
print(df.columns)
print(df.rename(columns={"Player's List": "Players","Cost IN $ (000)":"Cost"},inplace=True))
print(df.columns)
print(df.dtypes)
print(df.dropna(axis=1))
print(df.isnull().sum())
df["Cost"]=df["Cost"].fillna(df["Cost"].mean())
print(df["Cost"])
df["2022 Squad"]=df["2022 Squad"].fillna("Unknown")
print(df.isnull().sum())
print("duplicates",df.duplicated().sum())
print(df.shape)

#Analysis
top_cosliest=df.sort_values(by="Cost",ascending=False)[["Players","Cost"]].head()
print(top_cosliest)

top_cheapest=df.sort_values(by="Cost",ascending=True)[["Players","Cost"]].head()
print(top_cheapest)

Type_count=df["TYPE"].value_counts()
print(Type_count)

Team_count=df["Team"].value_counts()
print(Team_count)

Total_players=df["Players"].nunique()
print("Total_players",Total_players)

Mostexpensive=df.loc[df['Cost'].idxmax(),['Players','Team','Cost']]
print(Mostexpensive)
print(df['Team'].value_counts())

#Filltering
Diff_Type=df[df["TYPE"]=="BOWLER"]
print(Diff_Type)
print([(df["Team"]=="Gujarat Titans") & (df["TYPE"]=="BOWLER")])

import seaborn as sns
import matplotlib.pyplot as plt

##Visulization
##Team wise players count

ax=sns.countplot(data=df,x='Team',color='green')
for container in ax.containers:
    ax.bar_label(container)
plt.title("Total players in each team")
plt.xticks(rotation=45)
plt.show()

##Players Type Distribution
bx=sns.countplot(data=df,x='TYPE',color='green')
for container in bx.containers:
    bx.bar_label(container)
plt.title("Players Type Distribution")
plt.show()

##Team Wise Spending cost
team_spending=df.groupby('Team')['Cost'].sum().reset_index()
sns.barplot(data=team_spending,x='Team',y='Cost')
plt.title("Total Team Spending")
plt.xticks(rotation=45)
plt.show()

##Top palayers

sns.barplot(data=top_cosliest,x='Players',y='Cost',color='purple')
plt.title("Top 5 Expensive Players")
plt.xticks(rotation=45)
plt.show()

##Base Price
TOP_Base_pricers=df.sort_values(by='Base Price',ascending=True)[["Players","Base Price"]].head(5)
print(TOP_Base_pricers)
sns.boxplot(data=df,x='Team',y='Base Price')
plt.title(" Base Price")
plt.xticks(rotation=45)
plt.show()

pie=df.groupby['Team']['Players'].count()
plt.pie(pie,df=data,)
plt.xticks(rotation=45)
plt.show()
