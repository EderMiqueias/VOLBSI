try:
    from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QApplication, QPushButton, QFrame, QMessageBox
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont#, QImage, QPalette, QBrush, QIcon
    pyqtexiste = True
except:
    pyqtexiste = False

import sys
from datetime import datetime
from threading import Thread
from os import system

sistema_operacional = sys.platform
sistema_operacional = sistema_operacional.upper()
data = datetime.now()
data = data.strftime('%d/%m/%Y')
dict_equipes = {}

def qint(quest):
    while True:
        q1 = input(quest)
        try:
            q1 = int(q1)
            break
        except:
            print("Insira apenas numeros inteiros")
    return q1
def qfloat(quest):
    while True:
        q1 = input(quest)
        try:
            q1 = float(q1)
            break
        except:
            print("Insira apenas numeros")
    return q1

class gerenciar_equipes:
    def __init__(self):
        self.config()
        self.dict_equipes = dict_equipes
        self.menu()
    def menu(self):
        while True:
            print("\033[1;33m\nMENU DE GERENCIAMENTO DE CLUBES DA VOLBSI")
            print('\033[1;32m01 - Criar novo Clube')
            print('02 - Importar clube ')
            print('03 - Exportar clube')
            print('04 - Cadastrar Jogadores')
            print('05 - Listar Clubes')
            print('06 - Listar Jogadores')
            print('00 - ENCERRAR PROCESSO')
            
            optt = qint("\033[1;31m--> ")
            print("\033[0;0m",end='')
            if optt == 0:
                dict_equipes = self.dict_equipes
                print("\033[1;33mSaindo...\nProcesso Encerrado")
                break
            elif optt == 1:
                self.cadastrar_equipe()
            elif optt == 2:
                self.importar_clube()
            elif optt == 3:
                self.exportar_clube()
            elif optt == 4:
                self.cadastrar_jogadores()
            elif optt == 5:
                self.exibir_equipes()
            elif optt == 6:
                self.exibir_jogadores()
            else:
                print('\nOpção invalida, por favor digite alguma das opções a cima!')

    def cadastrar_equipe(self):
        if len(self.dict_equipes) < 6 and self.jogadores_disponiveis >= 6:
            nome_equipe = input('Informe O nome da equipe: ')
            ano_fundacao = str(qint('Informe O ano de fundação da equipe: '))
            cidade = input('Informe de que cidade é sua equipe: ')
            tecnico = input("Informe o nome do tecnico: ")
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
            self.dict_equipes[nome_equipe] = [nome_equipe,ano_fundacao,cidade,tecnico]
            for x in lista: self.dict_equipes[nome_equipe].append(x)
            print("\nEquipe cadastrada com sucesso!\n")
        else:
            print("\n6 clubes ja estao cadastrados, ou não há jogadores disponiveis suficientes para cadastrar um time.")

    def importar_clube(self):
        save = open("equipes.txt",'r')
        ha_times = save.readlines()
        save.close()
        if len(self.dict_equipes) < 6:
            if ha_times:
                arq_equipes = open('equipes.txt','r')
                dados_equipes = arq_equipes.readlines()
                arq_equipes.close
                dict_equipes_aux = {}
                print("\nTimes disponiveis:")
                for x in dados_equipes:
                    var = x.split(";")
                    var.remove(var[-1])
                    var[-1] = var[-1].split(",")
                    dict_equipes_aux[var[0]] = var
                    print(var[0])
                print("\nPara encerrar digite 'sair'")
                while True:
                    clube_importado = input("Informe o nome do clube: ")
                    if clube_importado == 'sair':
                        break
                    if clube_importado in dict_equipes_aux:
                        nova_equipe = dict_equipes_aux[clube_importado]
                        self.dict_equipes[nova_equipe[0]] = nova_equipe
                        print("\nEquipe",nova_equipe[0],"Importada Com Sucesso.")
                        break
                    else: print("Nenhum time com esse nome no arquivo 'equipes.txt'")
            else:
                print("\nO arquivo 'equipes.txt' esta vazio.")
        else:
            print("6 clubes ja estao cadastrados, hora de iniciar o campeonato.")

    def exportar_clube(self):
        if self.dict_equipes:
            save2 = open("equipes.txt",'a')
            while True:
                nova_equipe = input("\nNome do clube a ser exportado: ")
                if nova_equipe in self.dict_equipes:
                    for x in range(4):
                        save2.write(self.dict_equipes[nova_equipe][x])
                        save2.write(";")
                    for x in range(4, 10):
                        save2.write(self.dict_equipes[nova_equipe][x])
                        if x != 9: save2.write(",")
                        self.atualizar_equipe_jogador(self.dict_equipes[nova_equipe][x], nova_equipe)
                    save2.write(";\n")
                    save2.close()
                    break
                else:
                    print("\nNenhum time com esse nome.")
                    break
            print("\nEquipe exportada para oarquivo 'equipes.txt'.")
        else: print("-->ERRO<--\nNenhuma equipe cadastrada ainda.")

    def cadastrar_jogadores(self):
        while True:
            print("\nCadastrar jogadores")
            id_jogador = '#'+str(self.total_jogadores+1)
            self.total_jogadores += 1
            nome = input("Nome: ")
            idade = qint("Idade: ")
            altura = qfloat("Altura: ")
            peso = qfloat("Peso: ")
            arq_jog = open("jogadores.txt",'a')
            self.dict_jogadores[id_jogador] = [nome,idade,altura,peso,"None"]
            arq_jog.write(str(id_jogador+";"+nome+";"+str(idade)+";"+str(altura)+";"+str(peso)+";"+"None"+";"+"\n"))
            arq_jog.close()
            self.dict_jogadores[id_jogador] = [id_jogador,nome, idade, altura, peso, "None"]
            case = qint("\nDeseja continuar:\n01 - Sim\n00 - Nao\n--> ")
            if case != 1: break

    def exibir_equipes(self):
        if self.dict_equipes:
            for x in self.dict_equipes:
                print("\nNome:", x)
                print("Data de fundaçao:",self.dict_equipes[x][1])
                print("Casa local:",self.dict_equipes[x][2])
                print("Tecnico:",self.dict_equipes[x][3])
                print("Elenco:",end='')
                for y in self.dict_equipes[x][4]:
                    print(self.dict_jogadores[y][1],end=",")
                print()
        else: print("\n-->ERRO<--\nNenhum time cadastrado ainda.")

    def exibir_jogadores(self):
        if self.dict_jogadores:
            for x in self.dict_jogadores:
                print("\nNome:",self.dict_jogadores[x][1])
                print("Idade:",self.dict_jogadores[x][2])
                print("Altura:",self.dict_jogadores[x][3])
                print("Peso:",self.dict_jogadores[x][4])
                print("Equipe:",self.dict_jogadores[x][5])
                print("ID:",x)
        else: print("\n-->ERRO<--\nNenhum Jogador cadastrado ainda.")

    def config(self):
        try: save = open('jogadores.txt','r')
        except:
            save = open('jogadores.txt','w')
            save.close()
        try: save2 = open("equipes.txt",'r')
        except: save2 = open('equipes.txt','w')
        save2.close()
        save = open('jogadores.txt','r')
        dados_jogadores = save.readlines()
        save.close()
        #N nome idade numero altura peso equipe \n
        self.dict_jogadores = {}
        ##nome;ano de fundaçao;cidade;técnico
        self.dict_equipes = {}
        self.jogadores_disponiveis = 0
        self.total_jogadores = 0
        for x in dados_jogadores:
            var = x.split(";")
            var.remove(var[-1])
            if var[-1] == 'None':
                self.jogadores_disponiveis += 1
                self.total_jogadores += 1
            self.dict_jogadores[var[0]] = var

    def atualizar_equipe_jogador(self,id_jogador,nova_equipe):
        save = open('jogadores.txt','r')
        dados_jogadores = save.readlines()
        save.close()
        dict_jogadores_aux = {}
        print(id_jogador)
        for x in dados_jogadores:
            var = x.split(";")
            var.remove(var[-1])
            if var[0] == id_jogador:
                if var[-1] != "None":
                    print(var)
                    print("Jogador jah esta em escalado na equipe", var[-1])
                else:
                    var[-1] = nova_equipe
            dict_jogadores_aux[var[0]] = var
        arq_jog = open("jogadores.txt",'w')
        for x in dict_jogadores_aux:
            for y in range(len(dict_jogadores_aux[x])):
                arq_jog.write(dict_jogadores_aux[x][y])
                arq_jog.write(";")
            arq_jog.write("\n")
        arq_jog.close()
