"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2
"""

while True:
    esValido = True
    try:
        n = int(input("Ingrese el n: "))
    except:
        print("El valor ingresado no es válido")
        esValido = False

    if esValido:
        break

suma = int( ( n * (n+1) ) / 2 )
print("La sumatoria de los {0} primeros números es {1}".format(n, suma))

