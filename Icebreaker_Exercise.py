
wavelength = int(input("Enter wavelength : "))
if wavelength>=380 and wavelength<450:
    print("Color: Violet")
elif wavelength>=450 and wavelength<495:
    print("Color: Blue")
elif(wavelength>=495 and wavelength<570):
    print("Color: Green")
elif(wavelength>=570 and wavelength<590):
    print("Color: Yellow")
elif(wavelength>=590 and wavelength<620):
    print("Color: Orange")
elif(wavelength>=620 and wavelength<750):
    print("Color: Red")
else:
    print("Wavelength entered is outside the visible spectrum")