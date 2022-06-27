import math

def comFebre(temperaturas):
	return list(filter(lambda x: x > 37.8, temperaturas))


def itemize2(lista):
	return list(map(lambda x: '<li>' + x + '</li>', lista))


def bigCircles(n, raios):
	return list(filter(lambda x: math.pi * (x**2) > n, raios))


def quarentena(tuplas):
	return list(filter(lambda x: x[1] > 37.8, tuplas))
						

def idadesEm(idades, atual):
	return list(map(lambda x : atual - x, idades))


def onlyShorts(lista):
  return list(filter(lambda x: len(x) < 5, lista))


def changeNames(nomes):
	return list(map(lambda x: "Super " + x, filter(lambda x : x[0] == 'A', nomes)))
