#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
'''
class Comunicate(QtCore.QObject):
    filePathChanged = QtCore.pyqtSignal(str)
'''
class pathFinder(QDialog):
    ''' класс для окна запроса пути до файлов с отображеним дерева каталогов и файлов
    используем модели, чтобы разграничить данные и их отображение
    '''    
       
    def __init__(self, fileFilers:list): # укажем параметр фильтра файлов
        super().__init__()
        if fileFilers is None: fileFilers = ("*.csv","*.json") # неболшое предохранения
        self.__dirsTree = QTreeView()
        self.__filesTable = QTableView()
        self.__mainLayout = QVBoxLayout(self);
        self.__viewLayout = QHBoxLayout()
        self.__btnSelect = QPushButton()
        # Можно выставлять лапками,если наследуемся от Окна, но если от виджета,
        # но если наследуется от Виджета, то просто ставим все в Слой
        self.setGeometry(500,300, 1200, 700)
        self.setFixedSize(1200,700)
        # Утстанавливаем нужный каталог
        self.__path = "/"
        
        #модель файловой системы
        self.__dirsModel = QFileSystemModel()
        self.__dirsModel.setRootPath(self.__path) # задаем корневой каталог
        #фильтры отображения
        self.__dirsModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs) # 
        self.__dirsTree.setModel(self.__dirsModel) 
        # индекс корневого каталога в модели связываем с индексом КК в отображении
        self.__dirsTree.setRootIndex(self.__dirsModel.index(self.__path)) 
        self.__dirsTree.clicked.connect(self.on_clickOnDir)

        # модель файлов
        self.__fileModel = QFileSystemModel()
        # берем фильтры из списка - в одной случаем нам интересует csv & xls
        self.__fileModel.setNameFilters(fileFilers)
        self.__filesTable.setModel(self.__fileModel)
        self.__filesTable.setRootIndex(self.__fileModel.index(self.__path))
        #  selectionModel() возвращает obj типа QItemSelectionMode
        # и обрабатываем сигнал selectionChanged 
        self.__filesTable.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.__filesTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        # кнопка
        self.__btnSelect.setText("Выбрать")
        self.__dirsTree.setColumnWidth(0,250)
        #компановка элементов
        self.__viewLayout.addWidget(self.__dirsTree)
        self.__viewLayout.addWidget(self.__filesTable)
        self.__mainLayout.addLayout(self.__viewLayout)
        self.__mainLayout.addWidget(self.__btnSelect)
        self.__mainLayout.setAlignment(Qt.AlignLeft)

        #а как тут индекс передается вообще? что за магия? откуда он берется в функции, АЛО?!?!
    def on_clickOnDir(self, index):
        path = self.__dirsModel.fileInfo(index).absoluteFilePath()
        self.__filesTable.setRootIndex(self.__fileModel.setRootPath(path))
        print(path)
    
    def on_selectionChanged(self, selectionIntems):
        #сигнал Выделения передает объект QItemSelected,
        # берем список индексов выделенных эементов 
        # и из списка берем первый элемент
        indexes = selectionIntems.indexes()
        index = indexes[0]
        self.__curentFilePath = self.__fileModel.filePath(index)
        print(self.__curentFilePath)
    
    def getFilePath(self):
        return self.__curentFilePath
''' мой код, который почему-то не хочет нормально представления, нашел в инете похожее, переписываем и разбираем

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
'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    filters = ("*.csv","*.txt","*.xls")
    path = pathFinder(filters)
    path.show()
    sys.exit(app.exec_())
'''
