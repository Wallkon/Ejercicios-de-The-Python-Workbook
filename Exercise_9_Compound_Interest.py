"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.

Acabas de abrir una cuenta de ahorro que da 4% anual. El interés se paga al final del año y
se suma al total de la cuenta.
El programa lee el monto depositado en la cuenta y debe mostrar el total de la cuenta después de 1,
2 y 3 años.
El monto debe estar redondeado a 2 decimales.
Fórmula de interés compuesto: M = C(1+i)^n
M: capital final / C: Capital inicial / n: período / i: tasa de interés en tanto por 1
"""

INTERES_ANUAL = 0.04
capital_inicial = 0.0
while True:
    esValido = True
    try:
        capital_inicial = float(input("ingrese el monto a depositar: "))
    except:
        print("El valor ingresado no es válido")
        esValido = False
    if esValido:
        break

print("El valor de su invversión será")
print("A 1 año: {:.2f}".format( (capital_inicial*(1+INTERES_ANUAL) ** 1) ) )
print("A 2 años: {:.2f}".format( (capital_inicial*(1+INTERES_ANUAL) ** 2) ) )
print("A 3 años: {:.2f}".format( (capital_inicial*(1+INTERES_ANUAL) ** 3) ) )

