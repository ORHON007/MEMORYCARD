from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy Pepole')
main_win.resize(400,300)

qeustion = QLabel('Какая тема хакатона?')

bin_answer1 = QRadioButton('Скопировать популярную игру')
bin_answer2 = QRadioButton('imposter Gams')
bin_answer3 = QRadioButton('Котики')
bin_answer4 = QRadioButton('Покемоны')

layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layout_main.addWidget(qeustion,alignment = Qt.AlignCenter)
layoutH1.addWidget(bin_answer1,alignment = Qt.AlignCenter)
layoutH1.addWidget(bin_answer2,alignment = Qt.AlignCenter)
layoutH3.addWidget(bin_answer3,alignment = Qt.AlignCenter)
layoutH3.addWidget(bin_answer4,alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3) 

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет,тема хакатона скопировать популярную игру')
    victory_win.exec_()

bin_answer1.clicked.connect(show_win)
bin_answer2.clicked.connect(show_lose)
bin_answer3.clicked.connect(show_lose)
bin_answer4.clicked.connect(show_lose)

main_win.setLayout(layout_main)
main_win.show()
app.exec_()