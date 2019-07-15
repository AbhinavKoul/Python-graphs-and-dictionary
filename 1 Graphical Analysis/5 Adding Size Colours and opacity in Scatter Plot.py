#import
import matplotlib.pyplot as plt
import numpy as np

#data
year = [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980]
pop = [2.238,2.57,2.62,2.65,2.69,2.81,2.85,2.91,2.99,3.21,3.72,4.02,4.20,4.51,4.86,5.10,5.15,5.89,6.00,6.22,6.46,6.84,7.21,7.95,8.42,8.56,8.94,9.54,10.05,11.56,12.69]

#Adding and Managing Data
year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop
np_pop = np.array(pop)       #to be able to distinguish easily between bubbles
np_pop ** 100
#plotting
plt.scatter(year,pop,s=np_pop,alpha=0.7)      # FOR COLOURS WE NEED TO LEARN DICTIONARY SO WE WILL DO THAT LATER

#Adding Labels
plt.xlabel("Year")
plt.ylabel("Population")

#adding Title
plt.title("World Population Projections")

ticks_val = [0,2,4,6,8,10]
ticks_label = ["0B","2B","4B","6B","8B","10B"]

#Making Y AXIS LABELING                                 
plt.yticks(ticks_val,ticks_label)

#printing graph
plt.show()