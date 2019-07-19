# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab,row in cars.iterrows():    #iterrows returns 2 values (1. row label and 2.row content as panda series)
    print(lab)
    print(row)