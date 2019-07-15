#Importing
import matplotlib.pyplot as plt

life_exp = [45,46,45,23,45,67,86,54,75,86,54,87,46,23,45,87,99,65,76,57,56,33]
# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()