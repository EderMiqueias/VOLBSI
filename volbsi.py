#!/bin/python
#-*-coding:utf8;-*-
try:
    from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QApplication, QPushButton, QFrame, QMessageBox, QMainWindow
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont#, QImage, QPalette, QBrush, QIcon
    from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
    pyqtexiste = True
except:
    pyqtexiste = False

import sys
from datetime import datetime
from threading import Thread
from os import system
from random import randrange
from operator import itemgetter


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
        self.dict_equipes = dict_equipes
        self.dict_jogadores = {}
        self.jogadores_disponiveis = 0
        self.total_jogadores = 0
        self.config()
        self.menu()
    def menu(self):
        while True:
            print("\033[1;33m\nMENU DE GERENCIAMENTO DE CLUBES DA VOLBSI")
            print('\033[1;32m01 - Criar nova Equipe')
            print('02 - Importar Equipe')
            print('03 - Exportar Equipe')
            print('04 - Cadastrar Jogadores')
            print('05 - Listar Equipes')
            print('06 - Listar Jogadores')
            print('00 - ENCERRAR PROCESSO')
            print("\033[1;31m",end='')

            optt = qint("--> ")
            print("\033[1;97m",end='')
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
            nome_equipe = input('Informe o nome da equipe: ')
            ano_fundacao = str(qint('Informe o ano de fundação da equipe: '))
            cidade = input('Informe de que cidade é sua equipe: ')
            tecnico = input("Informe o nome do tecnico: ")
            lista = []
            print("\nAgora adicione as IDs dos jogadores")
            while True:
                if len(lista) == 6: break
                id_jogador = "#"+input('Insira a ID do Jogador :').lower()
                if not id_jogador in self.dict_jogadores:
                    print("\nNao Ha Nenhum Jogador Cadastrado Com Essa ID")
                elif self.dict_jogadores[id_jogador][5] == 'None':
                    lista.append(id_jogador)
                    self.dict_jogadores[id_jogador][5] = nome_equipe
                    print("OK")
                else:
                    print("\nEste Jogador Ja Esta Em Um Time Chamado", self.dict_jogadores[id_jogador][5])
            self.dict_equipes[nome_equipe] = [nome_equipe,ano_fundacao,cidade,tecnico,[]]
            for x in lista: self.dict_equipes[nome_equipe][4].append(x)
            print("Equipe Cadastrada Com Sucesso!\n")
        else:
            print("\n6 Equipes Ja Estao Cadastrados, Ou Não Há Jogadores Disponiveis Suficientes Para Cadastrar Um Time.")

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
                print("\nEquipes Disponiveis:")
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
                    for x in range(6):
                        save2.write(self.dict_equipes[nova_equipe][4][x])
                        if x != 5: save2.write(",")
                        self.atualizar_equipe_jogador(self.dict_equipes[nova_equipe][4][x], nova_equipe)
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
            print(self.total_jogadores)
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
        ##nome;ano de fundaçao;cidade;técnico
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


class gerenciar_campeonato:
    def __init__(self):
        self.l = []
        for c in dict_equipes:
            self.l.append(c)
        self.x = {}
        for y in self.l:
            self.x[y] = 0
        self.calendario = [0, 5, 1, 4, 2, 3], [0, 4, 5, 3, 1, 2], [0, 3, 4, 2, 5, 1], [0, 2, 3, 1, 4, 5], [0, 1, 2, 5, 3, 4]
        self.nrodada = 0
        self.rodada = 0
        self.campeao = None
        self.menu()

    def simular_rodada(self):
        self.rodada = self.nrodada
        if self.rodada > 4:
            self.rodada += -5
        vencedor = self.partida(self.l[self.calendario[self.rodada][0]], self.l[self.calendario[self.rodada][1]])
        print("\n\t", self.l[self.calendario[self.rodada][0]], 'x', self.l[self.calendario[self.rodada][1]],' \nVencedor: ', vencedor)
        vencedor2 = self.partida(self.l[self.calendario[self.rodada][2]], self.l[self.calendario[self.rodada][3]])
        print("\n\t", self.l[self.calendario[self.rodada][2]], 'x', self.l[self.calendario[self.rodada][3]],'\nVencedor: ', vencedor2)
        vencedor3 = self.partida(self.l[self.calendario[self.rodada][4]], self.l[self.calendario[self.rodada][5]])
        print("\n\t", self.l[self.calendario[self.rodada][4]], 'x', self.l[self.calendario[self.rodada][5]],'\nVencedor: ', vencedor3)
        self.x[vencedor] += 3
        self.x[vencedor2] += 3
        self.x[vencedor3] += 3
        self.rodada -= -1
        self.nrodada -= -1
        aux = 1
        for w in (sorted(self.x.items(), key=itemgetter(1), reverse=True)):
            if aux == 1:
                self.campeao = w[0]
            aux -= -1

    def partida(self,i1, i2):
        r = randrange(2)
        if r == 1:
            return i2
        else:
            return i1

    def tabela(self):
        aux = 1
        print("\n\tTabela\nN° Equipe\tpts\n")
        for w in (sorted(self.x.items(), key=itemgetter(1), reverse=True)):
            print(str(aux)+"°",w[0],'\t',w[1])
            aux += 1

    def menu(self):
            while self.nrodada < 10:
                print("\n\033[1;33mMENU DE GERENCIAMENTO DE CAMPEONATO")
                print('\033[1;32m01 - Simular',str(self.nrodada+1)+'ª','Rodada')
                print('02 - Exibir Tabela')
                optt = qint("\n\033[1;31m--> ")
                print("\033[1;97m",end="")
                if optt == 1:
                    self.simular_rodada()
                elif optt == 2:
                    self.tabela()
                else:
                    print('\nOpção Invalida, Digite Uma Das Opções a Cima!')
            else:
                arq = open(".champ",'w')
                arq.write(self.campeao)
                arq.close()
                while True:
                    print("\n\t\033[1;33mFim Da Temporada")
                    print("\033[1;32m01 - Exibir Tabela")
                    print("00 - Encerrar")
                    opc = qint("\033[1;31m-->")
                    print("\033[1;97m",end="")
                    if opc == 1:
                        self.tabela()
                    elif opc == 0:
                        break
                    else:
                        print("Opcao Invalida.")
                input("\033[1;31mAperter ENTER Para Encerrar o Campeonato e Abrir a Janela de Campeao VOLBSI")
                print("\n\033[1;32mSaindo...\nProcesso Encerrado")


def caixa_de_aviso():
    mensagem = QMessageBox()
    mensagem.setText("Ja Existe Um Processo sendo Executado!")
    mensagem.setInformativeText("Volte ao Sub Menu Que Esta Sendo Executado e Encerre Todos Os Processos.")
    mensagem.setIcon(QMessageBox.Information)
    mensagem.setStandardButtons(QMessageBox.Close)
    return mensagem

def caixa_de_erro():
    mensagem = QMessageBox()
    mensagem.setText("Ainda Nao Ha 6 times Cadastrados")
    mensagem.setInformativeText("Volte ao Menu de 'Gerenciamento de Equipes' e Conclua Todos os Cadastros.")
    mensagem.setIcon(QMessageBox.Information)
    mensagem.setStandardButtons(QMessageBox.Close)
    return mensagem


class welcomeWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowTitle("BEM VINDO AO VOLBSI")
        self.haveThread = False
        self.caixa = caixa_de_aviso()
        self.caixa2 = caixa_de_erro()
        
        self.frame = QFrame()
        self.frame.setLineWidth(5)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setFrameShape(QFrame.Panel)

        self.titulo = QLabel("VOLBSI")
        self.titulo.setFont(QFont("Courier", 100))
        self.titulo.setAlignment(Qt.AlignCenter|Qt.AlignHCenter)

        self.layout_botoes = QGridLayout()

        self.botao_gerenciar = QPushButton("Abrir Gerenciamento de Equipes")
        self.botao_gerenciar.setFont(QFont("Courier", 32, QFont.Bold))
        self.botao_gerenciar.setStyleSheet("color: green")
        self.botao_gerenciar.setToolTip("Gerencie os times e os jogadores antes de iniciar o campeonato.")
        self.botao_gerenciar.setWhatsThis("SISTEMA DE CAMPEONATO DE VÔLEI CRIADO PELOS ALUNOS DO PRIMEIRO PERIODO DE BSI DA UAST. Clique aqui para iniciar.")
        self.botao_gerenciar.clicked.connect(self.gerenciamento_equipes)

        self.botao_comecar = QPushButton("Iniciar Campeonato")
        self.botao_comecar.setFont(QFont("Courier", 32, QFont.Bold))
        self.botao_comecar.setToolTip("Inicie o campeonato de volei da VOLBSI.")
        self.botao_comecar.setStyleSheet("color: yellow")
        self.botao_comecar.setWhatsThis("SISTEMA DE CAMPEONATO DE VÔLEI CRIADO PELOS ALUNOS DO PRIMEIRO PERIODO DE BSI DA UAST. Clique aqui para iniciar.")
        self.botao_comecar.clicked.connect(self.gerenciamento_campeonato)

        self.botao_sair = QPushButton("SAIR")
        self.botao_sair.setFont(QFont("Courier", 32, QFont.Bold))
        self.botao_sair.setToolTip("Encerra o sistema")
        self.botao_sair.setStyleSheet("color: red")
        self.botao_sair.clicked.connect(self.sair)

        self.hiden_button = QPushButton("hide")
        self.hiden_button.clicked.connect(self.hiden_button_action)

        self.layout_botoes.setAlignment(Qt.AlignBottom|Qt.AlignCenter)
        self.layout_botoes.addWidget(self.botao_gerenciar,0,0)
        self.layout_botoes.addWidget(self.botao_comecar,1,0)
        self.layout_botoes.addWidget(self.botao_sair,2,0)

        self.dh = QLabel(f"{data}    {sistema_operacional}")
        self.dh.setFont(QFont("Times", 14))
        self.dh.setAlignment(Qt.AlignBottom|Qt.AlignLeft)

        self.nomes = QLabel("by Eder Miqueias, João Batista e Lucas de Lima")
        self.nomes.setFont(QFont("Times", 18))
        self.nomes.setAlignment(Qt.AlignBottom|Qt.AlignRight)

        self.layout.addWidget(self.titulo, 0,0)
        self.layout.addWidget(self.frame,0,0)
        self.layout.addLayout(self.layout_botoes, 1,0)
        self.layout.addWidget(self.dh, 2,0)
        self.layout.addWidget(self.nomes, 2,0)

    def mythread(self,whichThread):
        print("\033[1;31mA Janela De Menu Principal Sera Minimizada.\033[0;0m ")
        if whichThread == 'e':
            g_equipes = gerenciar_equipes()
            self.haveThread = False
            if sistema_operacional != 'LINUX':
                print("Abra a Janela Principal")
            else:
                self.showMaximized()
        else:
            g_campeonato = gerenciar_campeonato()
            self.haveThread = False
            self.hiden_button.click()

    def gerenciamento_equipes(self):
        if self.haveThread:
            self.caixa.exec_()
            self.showMinimized()
        else:
            self.thread_gerenciar = Thread(target=self.mythread, args=('e'))
            self.haveThread = True
            self.thread_gerenciar.start()
            self.showMinimized()

    def gerenciamento_campeonato(self):
        if self.haveThread:
            self.caixa.exec_()
            self.showMinimized()
        else:
            if len(dict_equipes) < 6:
                self.caixa2.exec_()
            else:
                self.thread_gerenciar = Thread(target=self.mythread, args=('c'))
                self.haveThread = True
                self.thread_gerenciar.start()
                self.showMinimized()

    def hiden_button_action(self):
        if sistema_operacional == 'LINUX':
            system("python player.py")
        else:
            print("Fin do Campeonato Sr Usuario de RWindows")

    def sair(self):
        if self.haveThread:
            self.caixa.exec_()
            self.showMinimized()
        else:
            quit()


if pyqtexiste:
    if sistema_operacional == 'LINUX':
        system('clear')
    else:
        system('cls')
    print("Iniciando VOLBSI...")
    app = QApplication(sys.argv)
    janela_boasVindas = welcomeWindow()
    janela_boasVindas.setMinimumSize(700,400)
    janela_boasVindas.showMaximized()
    app.exec_()
else:
    print("VOCE PRECISA INSTALAR A BIBLIOTECA PyQt5")
    print("NO CMD OU NO TERMINAL USE:\npip install PyQt5")