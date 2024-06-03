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
# The average life expectancy around the earth
print("Average age is ", df["Value"].mean())
# Finding minimum life expectancy at age 60 from dataset with "Value" column
print("Minimum life expectancy at age 60 is ", df['Value'].min())
# Finding maximum average age from dataset with "Value" column
print("Maximum life expectancy age is ", df['Value'].max())

# Determine the country with the highest life expectancy for a specific year
year = 2019  # Specify the year
highest_life_expectancy_country = df.loc[df['Period'] == year].nlargest(1, 'Value')['Location'].values[0]
print("Country with the highest life expectancy age in 2019 is ", highest_life_expectancy_country)


# checking for duplicates in 'Location' column
duplicate_values = df['Location'].duplicated()
print(duplicate_values)

# grouping the data by continent
gk = df.groupby('ParentLocation')
print(gk.first())