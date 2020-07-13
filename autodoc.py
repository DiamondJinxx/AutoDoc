#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pathFinder import pathFinder

class Autodoc(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message box',"Are you ute to quite?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('НеБольшаяУтилитка')
        #компановщики
        self.__vlay = QVBoxLayout(self)
        self.__vInLay = QVBoxLayout() # вертикальный для ввода
        self.__vOutLay = QVBoxLayout() # вертикальный для вывода
        self.__inHlay = QHBoxLayout() # горизонтальный для позиций входного файла
        self.__outHlay = QHBoxLayout() # горизонтальный длля позиций результирующего файла
        # управляющие элементы
        self.__out    = QLabel("Укажите папку, в которую поместить документ")
        self.__source = QLabel("Укажите файл формата .csv")
        self.__btnOutPath    = QPushButton("Выбрать папку")
        self.__btnSourcePath = QPushButton("Выбрать файл")
        self.__btnConv       = QPushButton("Создать документ")
        self.__outPath       = QLineEdit()
        self.__sourcePath    = QLineEdit()
        # установка отступов


       # print(self.__vlay.spacing())
        #self.__vInLay.addStretch()
#        self.__vOutLay.addStretch()
        # компановка 
        self.__vInLay.addWidget(self.__source)
        self.__inHlay.addWidget(self.__sourcePath)
        self.__inHlay.addWidget(self.__btnSourcePath)
        self.__vInLay.addLayout(self.__inHlay)
        
        self.__vOutLay.addWidget(self.__out)
        self.__outHlay.addWidget(self.__outPath)
        self.__outHlay.addWidget(self.__btnOutPath)
        self.__vOutLay.addLayout(self.__outHlay)
        
        self.__vlay.addLayout(self.__vInLay)
        self.__vlay.addLayout(self.__vOutLay)
        self.__vlay.addWidget(self.__btnConv)

        #коннекты
        self.__btnSourcePath.clicked.connect(self.on_btnSourcePathClick)
        self.__btnOutPath.clicked.connect(self.on_btnOutPathClick)



    def on_btnSourcePathClick(self):
        filters = ("*.csv","*.txt","*.xls")
        self.dlg = pathFinder(filters,True)
        self.dlg.exec_()
        self.fileIn = self.dlg.getPath()
        self.__sourcePath.setText(self.fileIn)

    def on_btnOutPathClick(self):
        filters = ("*.csv","*.txt","*.xls")
        self.dlg = pathFinder(filters,False)
        self.dlg.exec_()
        self.fileOut = self.dlg.getPath()
        self.__outPath.setText(self.fileOut)

    def on_btnConvClick(self):
        pass
    '''
        self.__widgets = QGridLayout(self)
        self.__out    = QLabel("Укажите папку, в которую поместить документ")
        self.__source = QLabel("Укажите файл формата .csv")
        self.__outPath       = QLineEdit()
        self.__sourcePath    = QLineEdit()
        self.__btnOutPath    = QPushButton("Выбрать файл")
        self.__btnSourcePath = QPushButton("Выбрать папку")
        self.__widgets.addWidget(self.__out, 0, 0)
        self.__widgets.addWidget(self.__outPath, 0, 1)
        self.__widgets.addWidget(self.__btnOutPath, 0, 2)
        self.__widgets.addWidget(self.__source, 1, 0)
        self.__widgets.addWidget(self.__sourcePath, 1, 1)
        self.__widgets.addWidget(self.__btnSourcePath, 1, 2)
'''
'''
        self.lay = QHBoxLayout(self)
        layl = QVBoxLayout()
        layr = QVBoxLayout()
        path = "/"
        treeWidget = QTreeView()
        dirModel = QFileSystemModel(self)
        fileModel = QFileSystemModel(self)
#        treeWidget.setGeometry(500,500,400,300)
#       treeWidget.setModel(dirModel)

        self.sourcePath = QLineEdit(self)
        self.lbl = QLabel('Text here', self )
        self.qbtn = QPushButton('Change Line', self )
        self.titleText = QLineEdit(self)
        self.lbl1 = QLabel('Измени название окна', self )
        self.qbtn1 = QPushButton('Change Title', self )
        layl.addWidget(self.lbl)
        layl.addWidget(self.qbtn)
        layl.addWidget(self.sourcePath)
        layr.addWidget(self.lbl1)
        layr.addWidget(self.qbtn1)
        layr.addWidget(self.titleText)
        self.lay.addWidget(treeWidget)
        self.lay.addLayout(layl)
        self.lay.addLayout(layr)
        treeWidget.resize(300,300)
#        self.c = Comunicate()
#        self.setLayout(lay) - можно и не указывать,
# так как при указании self в конструкторе компановщика он сам присоединится
#
#        self.qbtn.resize(100, 32)
 #       self.qbtn.move(50, 50)
        self.qbtn.clicked.connect(self.click_method)
        self.qbtn1.clicked.connect(self.click_method1)
    
    def click_method(self):
        if(len(self.sourcePath.text()) != 0):
            self.lbl.setText(self.sourcePath.text())
#            self.lay.layl.lbl.setText(self.sourcePath.text()) # не работает, нужен либо метод возващающий дочерний элемент, либо определять все как поля класса
        else: 
            self.lbl.setText("Type a text in text editor")

    def click_method1(self):
        filters = ("*.csv","*.txt","*.xls")
        self.dlg = pathFinder(filters)
        self.dlg.exec_()
        self.fileIn = self.dlg.getFilePath()
        self.lbl.setText(self.fileIn)

        #такой вариант кажись расценивается как мусор и отправляется на помойку
        # по этой причине ничего не отображается, нужно задать как поле объекта класса
#        dlg = pathFinder(filters)
#       dlg.show()
#        print("I'm clicked")

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Autodoc()
    ex.show()
    sys.exit(app.exec_())
