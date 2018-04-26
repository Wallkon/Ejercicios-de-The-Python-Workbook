"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.

Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.

Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians.

Esta página puede servir, pero no da el mismo resultado:
http://keisan.casio.com/exec/system/1224587128
"""

import math

AVG_RADIUS_HEARTH_KILOMETERS = 6371.01

t1_grades = float(input("ingrese t1: "))
g1_grades = float(input("ingrese g1: "))
t2_grades = float(input("ingrese t2: "))
g2_grades = float(input("ingrese g2: "))

t1_rads = math.radians(t1_grades)
g1_rads = math.radians(g1_grades)
t2_rads = math.radians(t2_grades)
g2_rads = math.radians(g2_grades)

#distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
distancia = AVG_RADIUS_HEARTH_KILOMETERS * math.acos(math.sin(t1_rads) * math.sin(t2_rads) * math.cos(t2_rads) * math.cos(g1_rads - g2_rads) )
print("La distancia es de {} km".format(distancia))
