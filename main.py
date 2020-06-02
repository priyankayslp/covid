import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/covid.csv')
print(df.head())
print(df.dtypes)
cdf = df[['Date','Deaths']]
print(cdf.head())
cdf = cdf.groupby(['Date'],as_index=False)['Deaths'].sum()
print(cdf.head(200))
cdf['Date'] = pd.to_datetime(cdf['Date'], format='%d/%m/%y')
fig, ax = plt.subplots(figsize=(20, 10))
# Add x-axis and y-axis
ax.scatter(cdf.Date.values,
        cdf['Deaths'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Deaths")

plt.show()
#based on state
cdf = df[['Date','Deaths','State/UnionTerritory']]
cdf = cdf.groupby(['Date','State/UnionTerritory'],as_index=False)['Deaths'].sum()
print(cdf.head(200))
cdf['Date'] = pd.to_datetime(cdf['Date'], format='%d/%m/%y')
cdf=cdf.loc[cdf['State/UnionTerritory']=='Delhi']
print(cdf.head(200))
fig, ax = plt.subplots(figsize=(20, 10))

# Add x-axis and y-axis
ax.scatter(cdf.Date.values,
        cdf['Deaths'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Deaths")

plt.show()

