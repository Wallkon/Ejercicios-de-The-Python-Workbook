"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.

En ciertas zonas existen contenedores de reciclaje de botellas.
Algunos reciben botellas de 1 litro o menos y pagan $0.10 por botella
Otros reciben botellas de más de 1 litro y pagan $0.25 por botella
El programa debe permitir ingresar el número de contenedores de cada tipo.

El programa debe calcular cuánto se debe recibir por botella devuelta
Por botellas de menos de 1 litro se paga $0.10
Por botellas de más de 1 litro se paga $0.25
La salida debe llevar el signo dólar y mostrar 2 decimales.
"""

VALOR_BOTELLA_CHICA = 0.10
VALOR_BOTELLA_GRANDE = 0.25

num_botellas_chicas = int(input('Cantidad de botellas chicas: '))
num_botellas_grandes = int(input('Cantidad de botellas grandes: '))

total_por_botellas_chicas = num_botellas_chicas * VALOR_BOTELLA_CHICA
total_por_botellas_grandes = num_botellas_grandes * VALOR_BOTELLA_GRANDE

print("Recibirá, por botellas chicas: ${:.2f}".format(total_por_botellas_chicas))
print("Recibirá, por botellas grandes: ${:.2f}".format(total_por_botellas_grandes))

