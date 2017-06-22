from math import pi,sqrt

def area(r, shape_constant):
	assert r>0,'Length must be positive'
	return r*r*shape_constant


def area_circle(r):
	return area(r, pi)

def area_square(r):
	return area(r, 1)

def area_hexagon(r):
	return area(r, 1.5*sqrt(3))