"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.

Español:
El programa lee el valor de un plato de restaurant, y calculará el impuesto y la propina.
El impuesto será de 19% y la propina de 10%
La salida debe mostrar el valor del plato, el impuesto, la propina y el total.
Formatear la salida para mostrar 2 decimales.
"""

IMPUESTO_PORCIENTO = 19
PROPINA_PORCIENTO = 10

valor_plato = float(input("Ingrese el valor de plato: "))

impuesto = (valor_plato * IMPUESTO_PORCIENTO) / 100
propina = (valor_plato * PROPINA_PORCIENTO) / 100
total = valor_plato + impuesto + propina

print("Plato = ${:.2f}".format(valor_plato))
print("Impuesto = ${:.2f}".format(impuesto))
print("Propina = ${:.2f}".format(propina))
print("Total ${:.2f}".format(total))



