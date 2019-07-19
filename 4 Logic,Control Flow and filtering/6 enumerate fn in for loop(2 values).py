# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas) :
    print("room"+str(index)+":"+str(a))

#since in previous it prints room 0 which makes no sence to other people
# Code the for loop
for index, area in enumerate(areas) :
    index = index + 1
    print("room " + str(index) + ": " + str(area))