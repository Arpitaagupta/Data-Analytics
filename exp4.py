import pandas as pd

df = pd.read_csv('gapminder-FiveYearData.csv')


# Q1. Year-wise mean of lifeExp
year_mean_lifeExp = df.groupby('year')['lifeExp'].mean()

# Q2. Year and Continent-wise mean of lifeExp
year_continent_mean_lifeExp = df.groupby(['year', 'continent'])['lifeExp'].mean()

# Q3. Finding the number of unique countries in each continent
unique_countries_per_continent = df.groupby('continent')['country'].nunique()

# Q4. Finding the total number of unique countries in the dataset
total_unique_countries = df['country'].nunique()

# Q5. Finding the first and last sample in the dataset
first_sample = df.iloc[0]
last_sample = df.iloc[-1]

# Q6. Creating a new dataset with only country, year, and continent attributes
new_dataset = df[['country', 'year', 'continent']]

# Q7. Checking if there are any null data in the dataset
null_data_check = df.isnull().any()

# Printing the results
print("Q1. Year-wise mean of lifeExp:")
print(year_mean_lifeExp)

print("\nQ2. Year and Continent-wise mean of lifeExp:")
print(year_continent_mean_lifeExp)

print("\nQ3. Number of unique countries in each continent:")
print(unique_countries_per_continent)

print("\nQ4. Total number of unique countries in the dataset:")
print(total_unique_countries)

print("\nQ5. First sample in the dataset:")
print(first_sample)

print("\nLast sample in the dataset:")
print(last_sample)

print("\nQ6. New dataset with only country, year, and continent attributes:")
print(new_dataset)

print("\nQ7. Checking for null data in the dataset:")
print(null_data_check)

