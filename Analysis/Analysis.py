import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot

path = "authors.csv"
df = pd.read_csv(path, header=None, na_values=['error']) 

headers = ["nickname", "date", "types", "user url"]
df.columns = headers
#df.replace("error", np.nan, inplace  = True) #NaN is used as a placeholder for missing data consistently in pandas, float. None - object
df = df.dropna().reset_index(drop=True) # delete Nan and reset index, because we droped two rows, 
#Do not try to insert index into dataframe columns. This resets the index to the default integer index.

df.to_csv("authors_red.csv", index=False) # save without indexes


quantity = df['nickname'].value_counts().reset_index() # as_index = false - only for dataframes, not serias
quantity.columns = ["nickname", "amount"]
#quantity.reset_index(level=0, inplace=True)
quantity.to_csv("authors_quantity_commits.csv", index=False) 

quantity['percentage'] = quantity['amount']/quantity['amount'].sum()

print(quantity.head())
#print(quantity.amount.apply(type))



#####
#Binning
######



plt.pyplot.hist(quantity["amount"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("amount")
plt.pyplot.title("horsepower bins")