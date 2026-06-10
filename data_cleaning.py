import pandas as pd

# Step 1: Data Access & Familiarization
df = pd.read_csv("dataset.csv")

print("===== Dataset Information =====")
print(df.info())

print("\n===== First 5 Rows =====")
print(df.head())

print("\n===== Data Types =====")
print(df.dtypes)

# Create Data Dictionary
data_dictionary = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str)
})

data_dictionary.to_csv("data_dictionary.csv", index=False)

# Step 2: Data Quality Assessment

print("\n===== Missing Values =====")
print(df.isnull().sum())

print("\n===== Duplicate Rows =====")
print(df.duplicated().sum())

print("\n===== Statistical Summary =====")
print(df.describe(include='all'))

# Step 3: Data Cleaning & Transformation

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
for column in df.columns:
    try:
        df[column] = pd.to_numeric(df[column])
        df[column] = df[column].fillna(df[column].median())
    except:
        df[column] = df[column].fillna(df[column].mode()[0])

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Files Generated:")
print("1. data_dictionary.csv")
print("2. cleaned_dataset.csv")