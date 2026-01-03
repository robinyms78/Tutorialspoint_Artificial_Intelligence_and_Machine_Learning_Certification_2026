# Pandas

import pandas as pd

# read a csv file
df=pd.read_csv("2_Python_Libraries/diabetes.csv")
print(df)
print(df.head())
print(df.shape)

# data types
print(df.dtypes)

# column names
print(df.columns)

# null value counts
print(df.count())

subset=df[['Pregnancies','Age']]
print(subset)
print(subset.shape)

# sorting of data
sorted_df = df.sort_values(['Pregnancies', 'Age'], ascending=[True, False])
print(sorted_df)

# grouping of data
grouped_df = df.groupby('Pregnancies')['Age'].mean()
print(grouped_df)

# https://pandas.pydata.org/docs/user_guide/index.html