"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.

Acá la fórmula:
https://www.calculateme.com/gas-mileage/us-mpg-to-liters-per-100-km
"""
GALLON_US_IN_LITERS = 3.785411784
MILE_IN_KILOMETERS = 1.609344

while True:
    esValido = True
    try:
        mpg = float(input("Ingrese el valor de eficiencia de combustible en MPG (estándar USA: "))
    except:
        print("El valor ingresado no es válido")
        esValido = False
    if esValido:
        break

kp100l = (100 * GALLON_US_IN_LITERS) / (MILE_IN_KILOMETERS * mpg)
print("{0} mpg equivale a {1:.2f} L/100Km".format(mpg, kp100l))


