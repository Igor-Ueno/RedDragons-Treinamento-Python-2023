import math
import numpy as np

def media(a, b):
    return (a + b) / 2

def rotacionarVetores(x, theta):
    theta = (math.pi/180) * theta
    return [x[0] * math.cos(theta) - x[1] * math.sin(theta),
            x[0] * math.sin(theta) + x[1] * math.cos(theta)]

def projPontoCircunferenciaUnitariaOrigem(p):
    a = p[1] / p[0]
    x = math.sqrt(1 / (1 + a))
    y = math.sqrt(1 - x**2)
    if(p[0] < 0): x *= -1
    if(p[1] < 0): y *= -1
    return [x, y]

def projPontoCircunferencia(p, r, c):
    a = (p[1] - c[1]) / (p[0] - c[0])
    b = p[1] - a*p[0]
    pol = [ 1 + a**2,
            2*(a*b - c[0] - a*c[1]),
            b**2 + c[0]**2 + c[1]**2 - r**2 - 2*b*c[1]]
    raizes = bhaskara(pol)
    if(p[0] > c[0]):
        x = raizes[0]
    else:
        x = raizes[1]
    y = a*x + b
    return [x, y]

def delta(pol):
    return pol[1]**2 - 4 * pol[0] * pol[2]

def bhaskara(pol):
    x1 = (-pol[1] + math.sqrt(delta(pol))) / (2 * pol[0])
    x2 = (-pol[1] - math.sqrt(delta(pol))) / (2 * pol[0])
    return [x1, x2]

def verificaRotacao(vAntes, vDepois, ang):
    if((180/math.pi) * (np.arctan(vDepois[1]/vDepois[0]) - np.arctan(vAntes[1]/vAntes[0])) == ang):
        print('o vetor foi rotacionado corretamente')
    else:
        print('erro na rotação do vetor')