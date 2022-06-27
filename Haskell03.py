def add10toAll(lista):
	return [x + 10 for x in lista]
	

def multN(n, lista):
	return [x*n for x in lista]


def applyExpr(lista):
	return [3*x + 2 for x in lista]


def addSuffix(suffix, list):
	return [x + suffix for x in list]


def selectgt5(lista):
	return [x for x in lista if x>5]


def sumOdds(list):
	return sum([x for x in list if x%2 == 1])


def selectExpr(lista):
	return [x for x in lista if x%2 == 0 and x < 50 and x > 20]


def countShorts(lista):
	return len([x for x in lista if len(x) < 5])


def selectSnd(lista):
	return[x[1] for x in lista]


def calcExpr(lista):
	return [(x**2)/2 for x in lista if (x**2)/2 > 10]


def trSpaces(word):
	return [x if x != ' ' else '-' for x in word ]
	

def dotProd(lista1, lista2):
  return sum([x[0]*x[1] for x in zip(lista1, lista2)])