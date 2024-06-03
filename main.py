import pandas as pd

# Load the data
df = pd.read_csv('life_expectancy_at_birth.csv')
# Showing number of rows and columns before cleaning
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nAvailable Features:")
print(df.columns.tolist())