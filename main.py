import pandas as pd

# Load the data
df = pd.read_csv('life_expectancy_at_birth.csv')
# Showing number of rows and columns before cleaning
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nAvailable Features:")
print(df.columns.tolist())
# Print the first 5 rows of the dataframe
print(df.head())
# Check for missing values
print(df.isnull().sum())
# Remove duplicates
df = df.drop_duplicates()
# Fill missing values with a specific value (e.g., 0)
df = df.fillna(0)
# Showing number of rows and columns after cleaning
print(df.shape)