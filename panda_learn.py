import pandas as pd

# Creates df = data frame
df = pd.read_csv("books.csv")

# Show first few rows
print(df.head())

# Rename a column
df.rename(columns={"Name": "Title"}, inplace=True)
df.rename(columns={"Score": "Rating"}, inplace=True)

# Show first few rows - debugging
# print(df.head())

# Drop a column
df.drop(columns=["Unnecessary colum"], inplace=True)

# Show first few rows - debugging
# print(df.head())

# Filter rows
popular = df[df["Rating"] > 4.5]

print(popular)

# Add a new column
df["Rating Out of 10"] = df["Rating"] * 2

# Show first few rows - debugging
print(df.head())