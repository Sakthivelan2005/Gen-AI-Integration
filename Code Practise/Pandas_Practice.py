import pandas as pd

# 1. Define your data using a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "London", "Tokyo"]
}

# 2. Load the data into a DataFrame object
df = pd.DataFrame(data)

# 3. View the result
print(df)

del df['City']
print(df)

df["mark"] = [70,50,90]
print(df)

df1 = df.drop([0,1])
print(df1)

# Adding a row
df.loc[1] = ["Sakthi",22,100]
print(df)

# Specific value in the row
df.iloc[0,1] = 100
print(df)
