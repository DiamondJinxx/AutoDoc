#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QMessageBox, QVBoxLayout,QHBoxLayout, QWidget, QFileSystemModel, QLineEdit, QTreeView
from PyQt5.QtCore import QCoreApplication


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
        self.setWindowTitle('Переменное название')
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
        self.setWindowTitle(self.titleText.text())
#        print("I'm clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Autodoc()
    ex.show()
    sys.exit(app.exec_())
