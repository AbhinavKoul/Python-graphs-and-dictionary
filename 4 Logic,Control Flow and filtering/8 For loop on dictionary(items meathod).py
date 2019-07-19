# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key,value in europe.items():   # 1st item it returns is key and 2nd element this fn returns is value
    print("the capital of "+key+" is "+str(value))