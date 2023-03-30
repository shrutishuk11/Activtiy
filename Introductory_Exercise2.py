# we can find the magnitude of Earthquake
import math
i = int(input("enter a intensity= "))
s= int(input("enter a standard intensity= "))
m = math.log(i/s)
print("magnitude of Earthquake=",m)