temp = float(input("Enter the temperatue  "))
velocity = float(input("Enter the wind velocity  "))
wind_chill = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.74)*pow(velocity,0.16)
print("Wind factor is ",wind_chill)