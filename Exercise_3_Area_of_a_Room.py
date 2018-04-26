"""
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

print('======== CÁLCULO DE ÁREA ==========')

######### DECIDIR METROS O PIES ###########
print('Ingrese la unidad de medida:  1: Metros     2: Pies')

while True:
	opcion = input()
	if (opcion == '1' or opcion == '2'):
		break
	else:
		print('La opción no es válida')

if (opcion == '1'):
	unidad = 'm2'
else:
	unidad = 'ft2'

######### INGRESAR ANCHO Y LARGO #############
print('Ingrese valores enteros o decimales positivos')

while True:
	ancho = input('Ancho: ')
	
	valido = True
	try:
		ancho_float = float(ancho)
	except:
		print('El valor no es válido')
		valido = False

	if valido:
		break

while True:
	largo = input('Largo: ')
	
	valido = True
	try:
		largo_float = float(largo)
	except:
		print('El valor no es válido')
		valido = False

	if valido:
		break

area = ancho_float * largo_float
print('El área es: ' + str(area) + unidad)







