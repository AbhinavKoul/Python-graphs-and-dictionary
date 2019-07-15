# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

##################################################### BASIC APPROACH WITHOUT DICTIONARIES
# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

#####################################################
#USING DICTIONARY
#####################################################

europe = { 'spain':'madrid',"france":"paris","germany":"berlin","norway":"oslo"}   #DICTIONARY MADE

# Print europe
print(europe)

# Print out the keys in europe          #USING KEY() MEATHOD ON OBJECT dict_name
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe["norway"])