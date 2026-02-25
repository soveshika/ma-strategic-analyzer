import pandas as pd

# Load the data
df = pd.read_csv("File 1.csv")

# See how big it is
print("Shape:", df.shape)

# See the column names
print("\nColumns:", df.columns.tolist())

# See the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# See if any data is missing
print("\nMissing values:")
print(df.isnull().sum())
# See what the data actually looks like
print("\nFull first 5 rows:")
print(df.head().to_string())

# See unique parent companies
print("\nParent Companies:")
print(df['Parent Company'].unique())

# See acquisition price info
print("\nAcquisition Price Stats:")
print(df['Acquisition Price'].describe())