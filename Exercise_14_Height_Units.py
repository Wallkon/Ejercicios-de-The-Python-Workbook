"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

FOOT_IN_INCHES = 12  # 1 pie son 12 pulgadas
INCH_IN_CENT = 2.54  # 1 pulgada son 2.54 centímetros

pies = float(input("Ingrese la parte en pies de su estatura: "))
pulgadas = float(input("Ingrese la parte en pulgadas de su estatura: "))

pies_a_centímetros = pies * FOOT_IN_INCHES
pulgadas_a_centimetros = pulgadas * INCH_IN_CENT
estatura_en_centimetros = pies_a_centímetros + pulgadas_a_centimetros

print("Su estatura en centímetros es : {}".format(estatura_en_centimetros))

