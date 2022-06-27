import math


def sum_squares(x, y):
  return x**2 + y**2


def isElderly(idade):
  return idade > 65


def htmlItem(x):
	return  '<li>' + x + "</li>"


def startsWithA(string):
  return string[0] == 'A' or 'a'


def isVowel(x):
	vowels = ['A','E','I','O','U','a','e','i','o','u']
	return x in vowels
	

def hasEqHeads(x, y):
  return x[0] == y[0]
  

def itemize(lista):
	return list(map(htmlItem, lista))


def onlyElderly(lista):
  return list(filter(isElderly, lista))


def onlyVowels(lista):
	return list(filter(isVowel, lista))


def identifySpaces(char):
  if char == ' ':
    return 1
  else:
    return 0

def countSpaces(lista):
  return sum(map(identifySpaces, lista))


def onlyLongWords(lista):
	return list(filter(lambda x : len(x) > 10, lista))


def onlyEven(lista):
	return list(filter(lambda x : x % 2 == 0, lista))


def onlyBetween60and80(lista):
	return list(filter(lambda x : x > 60 and x < 80, lista))


def calcAreas(lista):
	return list(map(lambda x : math.pi * (x**2), lista))
						#necessario -> import math

def charFound(c, string):
	return c in string
