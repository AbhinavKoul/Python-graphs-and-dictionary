# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc[["MOR"],["drives_right"]])

# Print sub-DataFrame containing the observations for Russia and Morocco and the columns country and drives_right.
print(cars.loc[["RU","MOR"],["country","drives_right"]])

#Great! You might wonder if you can also combine label-based selection the loc way and index-based selection the iloc way.
#  You can! It's done with ix, but we won't go into that here.
