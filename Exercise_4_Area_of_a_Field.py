"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

Hint: There are 43,560 square feet in an acre.
x acres = (ancho en pies * largo en pies) / 43560 pies cuadrados
"""

ACRE = 43560 #pies cuadrados

print('===== Calcular la superficie de un campo en acres ======')
 ancho = float(input('Ingrese el ancho en pies: '))
 largo = float(input('Ingrese el largo en pies: '))
 print('La superficie es ' + str( round((ancho*largo)/ACRE,2) ) + ' acres' )








