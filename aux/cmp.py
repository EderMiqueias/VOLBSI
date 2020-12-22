import random
def partida(i1, i2):   
    r = random.randrange(2)
    if r == 1:
        return i2
    else:
        return i1

t1 = "Flamengo"
p1 = 0
t2 = "Vasco"
p2 = 0
t3 = "Curitiba"
p3 = 0
t4 = "Palmeiras"
p4 = 0
x = {t1: p1, t2: p2, t3: p3, t4: p4}
l = [t1,t2,t3,t4]
'''
print(x)
vencedor = partida(l[0], l[1])
print(vencedor)
x[vencedor] += 3
print(x)
'''
times = {t1: p1, t2: p2, t3: p3, t4: p4}
def rodada():
      x1 = {t1: p1, t2: p2}
      x2 = {t3: p3, t4: p4}
      resultado = partida(x1[t1], x1[t2])
      resultado2 = partida(x2[t3], x2[t4])
      print(resultado,resultado2)
rodada()