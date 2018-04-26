"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
Widgets = 75 grs
Gizmo = 112 grs
Leer cuántos widgets y Gizmos contiene un pedido, y calcular el peso total del pedido.
"""

PESO_WIDGET_GRS = 75
PESO_GIZMO_GRS = 125

while True:
    esValido = True
    try:
        cant_widgets = int(input("Ingrese la cantidad de widgets: "))
    except:
        print("El número ingresado no es válido")
        esValido = False
    if esValido:
        break

while True:
    esValido = True
    try:
        cant_gizmos = int(input("Ingrese la cantidad de gizmos: "))
    except:
        print("El número ingresado no es válido")
        esValido = False
    if esValido:
        break

peso_total_widgets = PESO_WIDGET_GRS * cant_widgets
peso_total_gizmos = PESO_GIZMO_GRS * cant_gizmos
peso_pedido = peso_total_widgets + peso_total_gizmos

print("El peso total del pedido es {0} grs".format(peso_pedido))

