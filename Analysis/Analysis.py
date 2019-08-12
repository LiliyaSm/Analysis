import pandas as pd
path = "authors.csv"
df = pd.read_csv(path, header=None)

headers = ["nickname", "date", "types", "user url"]
df.columns = headers
print(df.head(10))