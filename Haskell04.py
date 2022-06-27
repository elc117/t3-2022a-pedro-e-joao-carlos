def faixaIdoso(x):
	match x:
            case x if x<60:
                return "ND"
            case x if x<=64:
                return "IDO64"
            case x if x<=69:
                return "IDO69"
            case x if x<=74:
                return "IDO74"
            case x if x <=79:
                return "IDO79"
            case x if x >=80:
                return "IDO80"


def classifiIdosos(idosos):
	return [(x[0],x[1],faixaIdoso(x[1])) for x in idosos]


def strColor(rgb):
	return "rgb" + str(rgb)


def genCircs(n, ponto, raio):
	return [(ponto[0] + x, ponto[1],raio) for x in range(n*5) if x%5==0]


def genReds(n):
	return [(x,0,0) for x in range(10*n) if x%10==0]