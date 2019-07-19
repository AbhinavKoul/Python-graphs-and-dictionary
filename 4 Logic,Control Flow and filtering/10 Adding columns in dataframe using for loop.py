# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column that contains a uppercase version of the country names in the "country" column.
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"] = row["country"].upper()


# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)