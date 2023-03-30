import math
v= float(input("enter wind speed in m/s= "))
t= float(input("enter wind temperature in Kelvin= "))
wci = 13.12 + (0.62*t)-(11.4*math.pow(v,0.16))+(0.4*t*math.pow(v,0.16))
print("Temperature that a person feels because of wind=",wci)