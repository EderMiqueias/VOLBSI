lista = []
print("\nAgora adicione as IDs dos jogadores")
while True:
    if len(lista) == 6: break
        id_jogador = "#"+input('Insira a ID do jogador :').lower()
        if not id_jogador in self.dict_jogadores:
            print("\nNao ha nenhum jogador cadastrado com essa ID")
        elif self.dict_jogadores[id_jogador][5] == 'None':
            lista.append(id_jogador)
            self.dict_jogadores[id_jogador][5] = nome_equipe
            print("OK")
        else:
            print("\nEste jogador ja esta em um time chamado", self.dict_jogadores[id_jogador][5])
        for x in lista: clube_importado.append(x)