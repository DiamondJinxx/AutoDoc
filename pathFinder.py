#!/usr/bin/python3

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class pathFinder(QtWidgets.QMainWindow):
    ''' класс для окна запроса пути до файлов с отображеним дерева каталогов и файлов
    используем модели, чтобы разграничить данные и их отображение
    '''
    def __init__(self, fileFilers:list): # укажем параметр фильтра файлов
        super().__init__()
        if fileFilers is None: fileFilers = ("*.csv","*.json") # неболшое предохранения
        self.dirsTree = QtWidgets.QTreeView(self)
        self.filesTable = QtWidgets.QTableView(self)
        # Можно выставлять лапками,если наследуемся от Окна, но если от виджета,
        # но если наследуется от Виджета, то просто ставим все в Слой
        self.setGeometry(500,300, 1200, 1200)
        self.dirsTree.setGeometry(0,0,600,600)
        self.filesTable.setGeometry(600,0,600,600)
        self.setFixedSize(1200,700)
        # Утстанавливаем нужный каталог
        self.path = "/"
        
        #модель файловой системы
        self.dirsModel = QtWidgets.QFileSystemModel()
        self.dirsModel.setRootPath(self.path) # задаем корневой каталог
        #фильтры отображения
        self.dirsModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs) # 
        self.dirsTree.setModel(self.dirsModel) 
        # индекс корневого каталога в модели связываем с индексом КК в отображении
        self.dirsTree.setRootIndex(self.dirsModel.index(self.path)) 
#        self.dirsTree.clicked.connect(self.on_clickOnDir)

        # модель файлов
        self.fileModel = QtWidgets.QFileSystemModel()
        # берем фильтры из списка - в одной случаем нам интересует csv & xls
        self.fileModel.setNameFilters(fileFilers)
        self.filesTable.setModel(self.fileModel)
        self.filesTable.setRootIndex(self.fileModel.index(self.path))
        #  selectionModel() возвращает obj типа QItemSelectionMode
        # и обрабатываем сигнал selectionChanged 
#        self.fileTable.selectionModel().selectionChanged.conect(self.on_selectionChanged)
        self.filesTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)



    def on_clickOnDir():
        
''' мой код, который почему-то не хочет нормально отобразить представления, нашел в инете похожее, переписываем и разбираем

        super().__init__()
        self.setGeometry(500, 500, 500, 600)
        self.setFixedSize(500, 600)
        self.path = ""

        lay       = QHBoxLayout()
        mdlDir    = QFileSystemModel(self) # Сделаем 2 отображения - деревом и таблицей, чтобы 
        mdlFile   = QFileSystemModel(self) # применять разные фильтры
        dirTree   = QTreeView()
        fileTable = QTableView() 

        mdlDir.setFilter(QDir.NoDotAndDotDot)
        dirTree.setModel(mdlDir)
        fileTable.setModel(mdlFile)
        lay.addWidget(dirTree)
        lay.addWidget(fileTable)
        self.setLayout(lay)
'''
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    filters = ("*.csv","*.txt","*.xls")
    path = pathFinder(filters)
    path.show()
    sys.exit(app.exec_())
