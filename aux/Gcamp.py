from random import randrange

class campeonato:
    def __init__(self):
        self.l = ["Flamengo","Vasco","Curitiba","Palmeiras","São Paulo","Santos"]
        self.x = {}
        for y in self.l:
            self.x[y] = 0
        self.calendario = [0, 5, 1, 4, 2, 3], [0, 4, 5, 3, 1, 2], [0, 3, 4, 2, 5, 1], [0, 2, 3, 1, 4, 5], [0, 1, 2, 5, 3, 4]
        self.aux1 = 0
        for g in range(2):
            for h in range(5):
                self.aux1 = h
                self.rodada1()
                input()
    def rodada1(self):
        vencedor = self.partida(self.l[self.calendario[self.aux1][0]], self.l[self.calendario[self.aux1][1]])
        print("\n\t\033[1;33m", self.l[self.calendario[self.aux1][0]], '\033[1;31mx\033[1;32m', self.l[self.calendario[self.aux1][1]],'\n\033[1;31mVencedor: \033[1;97m ', vencedor)
        vencedor2 = self.partida(self.l[self.calendario[self.aux1][2]], self.l[self.calendario[self.aux1][3]])
        print("\n\t\033[1;33m", self.l[self.calendario[self.aux1][2]], '\033[1;31mx\033[1;32m', self.l[self.calendario[self.aux1][3]],'\n\033[1;31mVencedor: \033[1;97m ', vencedor2)
        vencedor3 = self.partida(self.l[self.calendario[self.aux1][4]], self.l[self.calendario[self.aux1][5]])
        print("\n\t\033[1;33m", self.l[self.calendario[self.aux1][4]], '\033[1;31mx\033[1;32m', self.l[self.calendario[self.aux1][5]],'\n\033[1;31mVencedor: \033[1;97m ', vencedor3)
        print("\033[0;0m",end="")
        self.x[vencedor] += 3
        self.x[vencedor2] += 3
        self.x[vencedor3] += 3
    def partida(self,i1, i2):   
        r = randrange(2)
        if r == 1:
            return i2
        else:
            return i1

a = campeonato()