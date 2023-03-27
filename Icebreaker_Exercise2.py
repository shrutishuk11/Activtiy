wavelength = float(input(' Enter the wavelength: '))
if 1*10**-3 <= wavelength <= 1*10**-1:
    Wtype = 'Radio Waves'

elif 1*10**-3 <= wavelength <= 1*10**-1:
    Wtype = 'Microwaves'

elif 7*10**-7 <= wavelength <= 1*10**-1:
    Wtype = 'Infrared'

elif 4*10**-7 <= wavelength <= 7*10**-7:
    Wtype = 'Visible Light'

elif 1*10**-8 <= wavelength <= 4*10**-7:
    Wtype = 'Ultraviolet'

elif 1*10**-11 <= wavelength <= 1*10**-8:
    Wtype = 'X-Rays'

elif  wavelength >= 1*10**-11:
    Wtype = 'Gamma Rays'


print('Your wavelength is {0}'.format(Wtype))