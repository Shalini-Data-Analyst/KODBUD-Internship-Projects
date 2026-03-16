import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv')
##EDA Explorotary data analysis Campaign analysis
print(df)
print(df.columns)
print(df.shape)
print(df.head())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df['Campaign_ID'].nunique())
pd.concat([df["Location"],df['Customer_Segment']]).unique()
print(df['Campaign_Type'].value_counts())
print(df['Channel_Used'].value_counts())



##Acqusition cost analysis

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.figure(figsize=(10,5))
sns.scatterplot(x='Acquisition_Cost',y='ROI',data=df)
plt.title('Cost',fontsize='10',color='blue')
plt.show()

##campaign type analysis 
plt.figure(figsize=(10,5))
sns.barplot(x='Channel_Used',y='Conversion_Rate',data=df,hue='Campaign_Type',estimator='mean')
plt.title('channel',fontsize='10',color='blue')
plt.ylim(0,10)
plt.show()


##profit analysis
plt.figure(figsize=(10,5))
sns.barplot(x='Company',y='ROI',estimator='mean',data=df,hue='Campaign_Type')
plt.title('profit',fontsize='10',color='blue')
plt.show()

#correlation
correlation=df[['Engagement_Score','Conversion_Rate']].corr()
print(correlation)
sns.heatmap(correlation,annot=True,cmap='coolwarm')

proportion=df.groupby('Location')['ROI'].sum()
plt.figure(figsize=(12,5)) 
plt.title('proportion',color='green')
plt.pie(proportion,labels=proportion.index,autopct='%1.2f%%',shadow=True)
plt.show()

##Customer Segmentation analysis

plt.figure(figsize=(10,5))
plt.title("Target Audience",color='green',fontsize=20)
sns.countplot(x="Target_Audience",data=df,color='blue')
plt.show()

