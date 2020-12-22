import sys
from PyQt5.QtCore import Qt, QDir, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QApplication
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

class janela_vencedor(QWidget):
    def __init__(self, equipe_vencedora):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(800,400)

        titulo = QLabel("CAMPEAO DO VOLBSI 2019")
        titulo.setStyleSheet("color: yellow")
        titulo.setFont(QFont("Courier", 36))
        titulo.setAlignment(Qt.AlignHCenter)
        layout.addWidget(titulo)

        campeao = QLabel(f'\ {equipe_vencedora} /')
        campeao.setStyleSheet("color: white")
        campeao.setFont(QFont("Decorative", 48))
        campeao.setAlignment(Qt.AlignCenter)
        layout.addWidget(campeao)
        
        self.botao_sair = QPushButton("SAIR")
        self.botao_sair.setFont(QFont("Courier", 16))
        self.botao_sair.clicked.connect(quit)
        layout.addWidget(self.botao_sair)
        
        self.music = '/home/Documentos/projetos/volbsi/music.mp3'
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.music)))
        self.player.play()
        self.show()


app = QApplication(sys.argv)
screen = janela_vencedor("CORNOS FC")
screen.show()
sys.exit(app.exec_())
