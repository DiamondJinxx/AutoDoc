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
    def __init__(self, fileFilers:list, csvFile:bool): # укажем параметр фильтра файлов
        super().__init__()
        self.__csvFile = csvFile                               # используем форму лдя выбора пути к файлу?
        if fileFilers is None: fileFilers = ("*.csv","*.json") # неболшое предохранения
        self.__dirsTree = QTreeView()
        self.__mainLayout = QVBoxLayout(self);
        self.__viewLayout = QHBoxLayout()
        self.__btnSelect = QPushButton()

        # Утстанавливаем нужный каталог
        self.__path = "/"
        self.__currentFilePath = ""
        self.__currentDirPath = "/"

        #модель файловой системы
        self.__dirsModel = QFileSystemModel()
        self.__dirsModel.setRootPath(self.__path) # задаем корневой каталог

        #фильтры отображения
        self.__dirsModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs) # 
        self.__dirsTree.setModel(self.__dirsModel) 

        # индекс корневого каталога в модели связываем с индексом КК в отображении
        self.__dirsTree.setRootIndex(self.__dirsModel.index(self.__path)) 
        self.__dirsTree.clicked.connect(self.on_clickOnDir)

        # кнопка
        self.__btnSelect.setText("Выбрать")
        self.__btnSelect.clicked.connect(self.on_btnSelectClicked)
        #настройки нормального отображения
        self.__dirsTree.setColumnWidth(0,250)

        #компановка элементов - первая часть
        self.__viewLayout.addWidget(self.__dirsTree)

        # если ищем файл, то создаем таблицу с файлами, иначе обходимся только дирректориями
        if csvFile is True:     # сделаем универсальность данного окн
            # Можно выставлять лапками,если наследуемся от Окна, но если от виджета,
            # но если наследуется от Виджета, то просто ставим все в Слой
            self.setGeometry(500,300, 1200, 700)
            self.setFixedSize(1200,700)
            self.__fileMask = ".csv" 
            self.__filesTable = QTableView()
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
            self.__viewLayout.addWidget(self.__filesTable) 
            
        # компановка элементов - 2 часть
        self.__mainLayout.addLayout(self.__viewLayout)
        self.__mainLayout.addWidget(self.__btnSelect)
        self.__mainLayout.setAlignment(Qt.AlignLeft)
        
        # оконо без таблицы файлов
        if csvFile is False:
            self.setGeometry(500,300, 700, 700)
            self.setFixedSize(700,700)

    #а как тут индекс передается вообще? что за магия? откуда он берется в функции, АЛО?!?!
    # ПЕРЕДАЕТСЯ ВМЕСТЕ С СИГНАЛОМ
    def on_clickOnDir(self, index):
        self.__currentDirPath = self.__dirsModel.fileInfo(index).absoluteFilePath()
        if self.__csvFile is True:
            self.__filesTable.setRootIndex(self.__fileModel.setRootPath(self.__currentDirPath))
        print(self.__currentDirPath)
    
    def on_selectionChanged(self, selectionIntems):
        #сигнал Выделения передает объект QItemSelected,
        # берем список индексов выделенных эементов 
        # и из списка берем первый элемент
        indexes = selectionIntems.indexes()
        index = indexes[0]
        self.__currentFilePath = self.__fileModel.filePath(index)
        print(self.__currentFilePath)
    
    def on_btnSelectClicked(self):
        if(self.__csvFile is True):
            # если мы выбираем файл, то проверки на файл
            if(len(self.__currentDirPath) <= 1):
                QMessageBox.information(self,"Ошибка","Вы забыли выбрать!",QMessageBox.Ok, QMessageBox.Ok)
            elif(self.__currentFilePath.find(self.__fileMask) == -1): # если файл с другим расширением
                QMessageBox.information(self,"Ошибка","Выбранный вами файл не имеет расширения "+ self.__fileMask,QMessageBox.Ok, QMessageBox.Ok) 
#                self.__currentFilePath=""
            else:
                self.close()
        else:
            # если мы выбираем папкуi
            if(len(self.__currentDirPath) <= 1):
                QMessageBox.information(self,"Ошибка","Вы забыли выбрать каталог!",QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.close()

    def getPath(self):
        if(self.__csvFile is True):
            return self.__currentFilePath
        else:
            return self.__currentDirPath
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
