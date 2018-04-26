"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
"""

from math import log10

while True:
    esValido = True
    try:
        a = int(input("Ingrese el a: "))
    except:
        print("El valor no es válido")
        esValido = False
    if esValido:
        break

while True:
    esValido = True
    try:
        b = int(input("Ingrese el b: "))
        if (b == 0):
            print("b no puede ser cero")
            raise Exception
    except:
        print("El valor no es válido")
        esValido = False
    if esValido:
        break

print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("El resto de {0} / {1} = {2}".format(a, b, a%b))
print("log {0} = {1}".format(a, log10(a)))
print("{0} ^ {1} = {2}".format(a, b, a**b))
