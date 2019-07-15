#import
import matplotlib.pyplot as plt

#data
year = [1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980]
pop = [2.238,2.57,2.62,2.65,2.69,2.81,2.85,2.91,2.99,3.21,3.72,4.02,4.20,4.51,4.86,5.10,5.15,5.89,6.00,6.22,6.46,6.84,7.21,7.95,8.42,8.56,8.94,9.54,10.05,11.56,12.69]

#plotting
plt.plot(year,pop)

#Adding Labels                       ####################################################
plt.xlabel("Year")
plt.ylabel("Population")

#adding Title
plt.title("World Population Projections")

#printing graph
plt.show()