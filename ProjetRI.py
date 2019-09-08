# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\naila\Desktop\M2\RI\Projet\ProjetRI\IHM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QFileDialog
import sys
from math import log
from math import sqrt
from os import listdir
from os.path import isfile, join
from nltk import TweetTokenizer
import numpy

import os;
import subprocess as sp

class Ui_MainWindow(object):
    freq=[]
    poids=[]
    nbfile=0
    onlyfiles=[]
    stylesheet = """ 
        QTabBar::tab:selected {background: #BBD2E1;}
        QTabWidget>QWidget>QWidget{background:    #d6dbdf;}
        """
    path=0 
    listpertinent=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../Downloads/select_ok_accept_15254.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 206, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 206, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 206, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 201, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setAccessibleDescription("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 281, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 30, 201, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(310, 140, 281, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 90, 71, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../Downloads/Zoom-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 50, 291, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(50, 171, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 50, 181, 91))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_5.addWidget(self.comboBox)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 140, 241, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setGeometry(QtCore.QRect(330, 70, 201, 192))
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../../Downloads/1496970295-12_84763.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../../Downloads/equalsign_81021.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(330, 50, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 50, 171, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(320, 90, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 110, 211, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(20, 90, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(320, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 190, 201, 171))
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../check-box-png-11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_5.setGeometry(QtCore.QRect(320, 110, 201, 192))
        self.tableWidget_5.setAlternatingRowColors(True)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon2)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon3)
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #self.statusbar.setWindowIcon(QIcon("C:/Users/naila/Downloads/kisspng-search-engine-optimization-google-images-web-page-vector-material-bulb-5a99437072a7b1.2055588815199937124696.png"))
        self.statusbar.setStyleSheet("QStatusBar{color: black;}")
        MainWindow.setStatusBar(self.statusbar)
        self.comboBox.addItem("Produit Interne")
        self.comboBox.addItem("Coef de Dice")
        self.comboBox.addItem("Cosinus")
        self.comboBox.addItem("Jaccard")
        self.comboBox_2.addItem("Produit Interne")
        self.comboBox_2.addItem("Coef de Dice")
        self.comboBox_2.addItem("Cosinus")
        self.comboBox_2.addItem("Jaccard")

        MainWindow.setStyleSheet(Ui_MainWindow.stylesheet)
    
        
        
###########################APPPEL DES FONCTIONS        
        
       
        self.pushButton_6.clicked.connect(lambda:self.selection())
        self.pushButton.clicked.connect(lambda:self.indexmot())
        self.pushButton_2.clicked.connect(lambda:self.indexdoc(Ui_MainWindow.freq,Ui_MainWindow.poids))
        self.pushButton_3.clicked.connect(lambda:self.boolenModel(Ui_MainWindow.freq,Ui_MainWindow.onlyfiles))
        self.pushButton_7.clicked.connect(lambda:self.probModel())

        self.comboBox_4.currentTextChanged.connect(self.openfile)
        self.pushButton_4.clicked.connect(lambda:self.choixformVec())
        self.pushButton_5.clicked.connect(lambda:self.choixformprob())
        #self.tableWidget_3.itemSelectionChanged.connect(lambda:self.ouvrir())
        

        
 
        
        
#######################Fin appel des fonctions  
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The finder"))
        self.pushButton_6.setText(_translate("MainWindow", "Selectionner"))
        self.label_14.setText(_translate("MainWindow", "Selectionnez un dossier:"))
        self.label.setText(_translate("MainWindow", "Recherche par terme:"))
        self.label_2.setText(_translate("MainWindow", "Resultat:"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fréquence"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Poids"))
        self.label_3.setText(_translate("MainWindow", "Recherche dans un document:"))
        self.label_4.setText(_translate("MainWindow", "Resultat:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Terme"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fréquence"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Poids"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Recherche Simple"))
        self.label_5.setText(_translate("MainWindow", "Entrez votre requette booléenne:"))
        self.label_6.setText(_translate("MainWindow", "Resultat de la recherche:"))
        self.pushButton_3.setText(_translate("MainWindow", "Lancer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recherche Booléenne"))
        self.label_7.setText(_translate("MainWindow", "Choisissez une formule:"))
        self.label_8.setText(_translate("MainWindow", "Entrez votre requette:"))
        self.pushButton_4.setText(_translate("MainWindow", "Lancer"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fichier"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Similarité"))
        self.label_9.setText(_translate("MainWindow", "Résultat de la recherche:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Recherche Vectorielle"))
        self.label_10.setText(_translate("MainWindow", "Phase1: Recherche vectorielle:"))
        self.label_11.setText(_translate("MainWindow", "Choisissez une formule:"))
        self.label_13.setText(_translate("MainWindow", "Resultat de la recherche:"))
        self.pushButton_5.setText(_translate("MainWindow", "Lancer"))
        self.label_12.setText(_translate("MainWindow", "Entrez votre requette:"))
        self.label_15.setText(_translate("MainWindow", "Phase2: Recherche probabiliste:"))
        self.pushButton_7.setText(_translate("MainWindow", "Relancer"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fichier"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Choix"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fichier"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Similarité"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Recherche Probabiliste"))

        
###################################Mes fonctions
        
#############################slectionner un dossier
    def probModel(self):
       somme=0
       Ui_MainWindow.listpertinent.clear()
       allRows=self.tableWidget_3.rowCount()
       for row in range(0,allRows):
            if (self.tableWidget_3.cellWidget(row,1).isChecked()):
                 Ui_MainWindow.listpertinent.append(self.tableWidget_3.item(row,0).text())
             
       vec=self.textEdit_4.toPlainText()
       vecreq=[]
       vecreq=vec.split()
       listProb={}
       for file in Ui_MainWindow.onlyfiles:
            somme=0
            for mot in vecreq:
                list=self.indexmotSimple(mot)
               ## print(list)
                if  file in list :
                    list=self.indexmotSimple(mot)
                    n=float(len(list))
                    
                    
                    r=float(self.calculLONG(Ui_MainWindow.freq,mot,Ui_MainWindow.listpertinent))
                    
                    N=float(len(Ui_MainWindow.onlyfiles))
                    
                    R=float(len(Ui_MainWindow.listpertinent))
                   
                    somme=somme+(log(((r+0.5)/(R-r+0.5))/((n-r+0.5)/(N-n-R+r+0.5)))*Ui_MainWindow.poids[mot,file])
            listProb[file]=round(somme,2) 
       
       listProb=self.orderdesc(listProb) 
       self.remplir(listProb,self.tableWidget_5)    
            
        
        
    
    def openfile(self):
       if self.comboBox_4.currentText()  != None and self.comboBox_4.currentText() !=' ' and self.comboBox_4.currentText() !='':
            file=str(self.comboBox_4.currentText())
            string=Ui_MainWindow.path+'/'+file
            programName = "notepad.exe"
            sp.Popen([programName, string])
            
       
    def choixformVec (self):
        self.tableWidget_4.clearContents()
        nom= self.comboBox.currentText()
        
        req=self.textEdit_3.toPlainText()
        req=req.split()

        if str(nom) == 'Produit Interne' :
            list=self.innerProduct(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir(list,self.tableWidget_4)
            
        if nom == 'Coef de Dice':
            list=self.coefDice(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir(list,self.tableWidget_4)
        if nom == 'Cosinus':
            list=self.cosinus(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            
            self.remplir(list,self.tableWidget_4)
        if nom == 'Jaccard':
            list=self.jacob(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir(list,self.tableWidget_4)
            
            
    def choixformprob (self):
        self.tableWidget_3.clearContents
        nom= self.comboBox_2.currentText()
        req=self.textEdit_4.toPlainText()
        req=req.split()

        if str(nom) == 'Produit Interne' :
            list=self.innerProduct(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir2(list,self.tableWidget_3)

        if nom == 'Coef de Dice':
            list=self.coefDice(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir2(list,self.tableWidget_3)
        if nom == 'Cosinus':
            list=self.cosinus(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir2(list,self.tableWidget_3)
        if nom == 'Jaccard':
            list=self.jacob(req,Ui_MainWindow.onlyfiles,Ui_MainWindow.poids)
            self.remplir2(list,self.tableWidget_3)
                
    '''            
    def ouvrir(self):
        
             print('55555555555555555555555555222222222222222222222') 
             r=self.tableWidget_4.cellPressed()
             print(r)
            ## list.append(r)
             print('55555555555555555555555555')    
    '''        
        
        
    def selection(self):
            
            Ui_MainWindow.path= str(QFileDialog.getExistingDirectory(None, "Select Directory")) 
            print(Ui_MainWindow.path)
            self.lineEdit.setText(Ui_MainWindow.path)
            Ui_MainWindow.freq,Ui_MainWindow.nbfile,Ui_MainWindow.onlyfiles=self.calcule_freq(Ui_MainWindow.path)  
            Ui_MainWindow.poids=self.calculpoids(Ui_MainWindow.freq,Ui_MainWindow.nbfile)
            self.comboBox_3.clear()
            self.tableWidget_3.clearContents()
            self.tableWidget_5.clearContents()
            self.comboBox_3.addItems(Ui_MainWindow.onlyfiles)
            print(Ui_MainWindow.freq)        
            return (Ui_MainWindow.freq,Ui_MainWindow.poids,Ui_MainWindow.nbfile,Ui_MainWindow.onlyfiles)
        
##############################calcule la frequence
    def calcule_freq(self,path):
        
        freq = {}
        listCar = {'.', ',', '!', '?', '\''}
        stoplist=Motvide.stepwords
        os.chdir(path)
       
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print(onlyfiles)
        n =len(onlyfiles)
        k = 0
        while k < n:
          
            f = open(onlyfiles[k], 'r')
            t = f.read()
            t = t.lower()
            i = 0
    
            while i < len(t):
                if t[i] in listCar:
                    t = t.replace(t[i], " ")
                i += 1
            a = t.split()
            ##nb = len(a)
            for w in a:
                if not w in stoplist and len(w) > 1:
                    if not (w, onlyfiles[k]) in freq:
                        freq[w, onlyfiles[k]] = a.count(w)
                       #  print(w, freq[w, onlyfiles[k]])
            k += 1
        f.close()
        
        ##print(freq)
        
        return (freq,len(onlyfiles),onlyfiles)
    
###########################calcul de poids
    def calculpoids(self,freq,lenOnlyfiles):
            ni = {}
            for (w, d) in freq:
                    if not w in ni:
                            ni[w] = 1
                    else:
                            ni[w] += 1
            # calcul de la fréquence max de chaque document
            max = {}
            for(w, d) in freq:
                    if not d in max:
                            max[d] = freq[w, d]
                    else:
                            if freq[w, d] > max[d]:
                                    max[d] = freq[w, d]
            # calcul du fichier inverse avec poids TF*IDF
            poids={}
            for (w, d) in freq:
               poids[w, d] = round((float(freq[w, d])/max[d]) * numpy.log10((float(lenOnlyfiles)/ni[w])+1),2)     
               round(poids[w, d],2)
            list=sorted(poids.items(), key=lambda kv: kv[1])
            poids=reversed(list)
            poids=dict(poids)
            print(poids)
            return (poids)  
        
        
#2 eme fonc donner un mot et donne la freq dans chaque doc
    def indexmot(self):
        self.tableWidget_2.clearContents()
        w=self.textEdit.toPlainText()
        self.tableWidget_2.setRowCount(0)
        w = w.lower()
        for(a, b) in Ui_MainWindow.poids:
           if a == w:
               rowPosition = self.tableWidget_2.rowCount()
               self.tableWidget_2.insertRow(rowPosition)
               self.tableWidget_2.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(b))
               self.tableWidget_2.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(Ui_MainWindow.freq[w,b])))
               self.tableWidget_2.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(Ui_MainWindow.poids[w,b])))
                            
               ##item.setCheckable(True)####el hamdoullah
               
               
            
    def indexmotSimple(self, w):
        
        list=[]
        w = w.lower()
        for(a, b) in Ui_MainWindow.freq:
               #print(a) 
              # print(b)
              
               if a == w:
                   list.append(b)
        
        return list 

    def calculLONG (self,freq,mot,list):
        longueur=0
        for  file in list:
           if (mot,file) in freq :
               longueur+=1
        return longueur
#################################les deux fonctions d acces de base
##1er fonc donner un doc et retorne la freq pr chque mot

    def indexdoc(self,freq, poids):
         self.tableWidget.clearContents()
         d=self.comboBox_3.currentText()
         
         self.tableWidget.setRowCount(0)
         for (a, b) in poids:
            if b == d:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(a))
                self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(freq[a,d])))
                self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(poids[a,d])))
              

###############################fonction boolen
    
    
    def boolenModel(self,freq,onlyfiles):
       
       self.comboBox_4.clear()
       self.comboBox_4.addItem(' ')
       requete=self.plainTextEdit_2.toPlainText() 
       requete=requete.lower()
          
       req = TweetTokenizer().tokenize(requete)
        
       for file in onlyfiles:
          
         reqtemp=[] 
         for mot in req:
            mot.lower() 
            if(mot in ['and','or','(',')','not']): 
                reqtemp.append(mot)
                reqtemp.append(' ')
            else:
                listfile=self.indexmotSimple( mot)
                if (file in listfile): 
                    reqtemp.append('1')
                    reqtemp.append(' ')
                else: 
                    reqtemp.append('0') 
                    reqtemp.append(' ')
         evaluation= eval(''.join(reqtemp))                 
         if (evaluation==1): 
            
             self.comboBox_4.addItem(file) 
 ###########################calcul inner product   

    def innerProduct(self,vecreq,onlyfiles,poids):
                  
         list={}
         for filename in onlyfiles:
             file = open(filename, 'r')
             file = file.read()
             file = file.lower()
             file = file.split()
             
             innerpro=0
             for mot in vecreq:
                 mot=mot.lower()
                 
                 if(mot in file):
                    innerpro= innerpro + poids[mot,filename] 
                 
             list[filename]=round(innerpro,2)
         list=self.orderdesc(list)    
         return list   

              
             
            
     
    def remplir(self,list,tableWidget):
        
          self.tableWidget.setRowCount(0)
          tableWidget.clearContents()
          
          for f in list:
              
              if list[f]!=0 : 
                  
                  rowPosition = self.tableWidget.rowCount()
                  tableWidget.insertRow(rowPosition)
                  tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(f))
                  tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(list[f])))
                                
             
         
    def remplir2(self,list,tableWidget):
          ##import tkinter *
          self.tableWidget.setRowCount(0)
          tableWidget.clearContents()
          for f in list:
              if list[f]!=0 : 
                  rowPosition = self.tableWidget.rowCount()
                  tableWidget.insertRow(rowPosition)
                  tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(f))
                  self.check = QtWidgets.QCheckBox(tableWidget)
                  ##self.check.setText('12/1/12')
                  tableWidget.setCellWidget(rowPosition,1, self.check)

        
    #######################ordonner les fichier
    def orderdesc (self,list):
       
       list=sorted(list.items(), key=lambda kv: kv[1])
       list=dict(list)
       return list
        
        
    #####################################si existe
    def exist(self,mot,poids):
       mot=mot.lower()
       bool=False
       for(w, d) in Ui_MainWindow.freq:
                        if (mot==w):
                             bool=True
                             break
       return bool 
    
    ####################################coefDiCE
    def coefDice(self,vecreq,onlyfiles,poids):
         
             listcoef={}
             listcoef=self.innerProduct(vecreq,onlyfiles,poids)
             for file in onlyfiles:
                 sommefile=0
                 sommereq=0 
                 
                 for mot in vecreq:
                     if(self.exist(mot,poids)):
                           sommereq+=1
                 for(w, d) in poids:
                     if (d==file):          
                        sommefile=sommefile+(poids[w,file]**2) 
                 if (sommereq==0 and sommefile==0): 
                      listcoef[file]=0
                 else:
                      listcoef[file]=round((2*listcoef[file])/(sommereq+sommefile),2)
                      
             listcoef=self.orderdesc(listcoef)  
             return listcoef
    
    #######################################mesure de cosinus
    def cosinus(self,vecreq,onlyfiles,poids):
             listcos={}
             listcos=self.innerProduct(vecreq,onlyfiles,poids)
             for file in onlyfiles:
                 sommefile=0
                 sommereq=0 
                 
                 for mot in vecreq:
                     if(self.exist(mot,poids)):
                          sommereq+=1
                         
                 for(w, d) in poids:
                     if (d==file):          
                        sommefile=sommefile+(poids[w,file]**2) 
                 if (sommereq==0 or sommefile==0): 
                     listcos[file]=0
                 else:
                     listcos[file]=round((2*listcos[file])/(sqrt(sommereq*sommefile)),2)
                     
             listcos=self.orderdesc(listcos)  
             return listcos
    ###################################################JACOB
    def jacob(self,vecreq,onlyfiles,poids):
             listjac={}
             listjac=self.innerProduct(vecreq,onlyfiles,poids)
                     
             for file in onlyfiles:
                 sommefile=0
                 sommereq=0 
                 
                 for mot in vecreq:
                     if(self.exist(mot,poids)):
                          sommereq+=1
                         
                 for(w, d) in poids:
                     if (d==file):          
                        sommefile=sommefile+(poids[w,file]**2) 
                 if (sommereq+sommefile-listjac[file]==0): 
                     listjac[file]=0
                 else:
                     listjac[file]=round(listjac[file]/(sommereq+sommefile-listjac[file]),2)
                     ## round(listjac,2)
                        
             
             listjac=self.orderdesc(listjac)  
             return listjac         
                   
    

    


class Motvide():

    stepwords=['a',
 'à',
 'â',
 'abord',
 'afin',
 'ah',
 'ai',
 'aie',
 'ainsi',
 'allaient',
 'allo',
 'allô',
 'allons',
 'après',
 'assez',
 'attendu',
 'au',
 'aucun',
 'aucune',
 'aujourd',
 "aujourd'hui",
 'auquel',
 'aura',
 'auront',
 'aussi',
 'autre',
 'autres',
 'aux',
 'auxquelles',
 'auxquels',
 'avaient',
 'avais',
 'avait',
 'avant',
 'avec',
 'avoir',
 'ayant',
 'b',
 'bah',
 'beaucoup',
 'bien',
 'bigre',
 'boum',
 'bravo',
 'brrr',
 'c',
 'ça',
 'car',
 'ce',
 'ceci',
 'cela',
 'celle',
 'celle-ci',
 'celle-là',
 'celles',
 'celles-ci',
 'celles-là',
 'celui',
 'celui-ci',
 'celui-là',
 'cent',
 'cependant',
 'certain',
 'certaine',
 'certaines',
 'certains',
 'certes',
 'ces',
 'cet',
 'cette',
 'ceux',
 'ceux-ci',
 'ceux-là',
 'chacun',
 'chaque',
 'cher',
 'chère',
 'chères',
 'chers',
 'chez',
 'chiche',
 'chut',
 'ci',
 'cinq',
 'cinquantaine',
 'cinquante',
 'cinquantième',
 'cinquième',
 'clac',
 'clic',
 'combien',
 'comme',
 'comment',
 'compris',
 'concernant',
 'contre',
 'couic',
 'crac',
 'd',
 'da',
 'dans',
 'de',
 'debout',
 'dedans',
 'dehors',
 'delà',
 'depuis',
 'derrière',
 'des',
 'dès',
 'désormais',
 'desquelles',
 'desquels',
 'dessous',
 'dessus',
 'deux',
 'deuxième',
 'deuxièmement',
 'devant',
 'devers',
 'devra',
 'différent',
 'différente',
 'différentes',
 'différents',
 'dire',
 'divers',
 'diverse',
 'diverses',
 'dix',
 'dix-huit',
 'dixième',
 'dix-neuf',
 'dix-sept',
 'doit',
 'doivent',
 'donc',
 'dont',
 'douze',
 'douzième',
 'dring',
 'du',
 'duquel',
 'durant',
 'e',
 'effet',
 'eh',
 'elle',
 'elle-même',
 'elles',
 'elles-mêmes',
 'en',
 'encore',
 'entre',
 'envers',
 'environ',
 'es',
 'ès',
 'est',
 'et',
 'etant',
 'étaient',
 'étais',
 'était',
 'étant',
 'etc',
 'été',
 'etre',
 'être',
 'eu',
 'euh',
 'eux',
 'eux-mêmes',
 'excepté',
 'f',
 'façon',
 'fais',
 'faisaient',
 'faisant',
 'fait',
 'feront',
 'fi',
 'flac',
 'floc',
 'font',
 'g',
 'gens',
 'h',
 'ha',
 'hé',
 'hein',
 'hélas',
 'hem',
 'hep',
 'hi',
 'ho',
 'holà',
 'hop',
 'hormis',
 'hors',
 'hou',
 'houp',
 'hue',
 'hui',
 'huit',
 'huitième',
 'hum',
 'hurrah',
 'i',
 'il',
 'ils',
 'importe',
 'j',
 'je',
 'jusqu',
 'jusque',
 'k',
 'l',
 'la',
 'là',
 'laquelle',
 'las',
 'le',
 'lequel',
 'les',
 'lès',
 'lesquelles',
 'lesquels',
 'leur',
 'leurs',
 'longtemps',
 'lorsque',
 'lui',
 'lui-même',
 'm',
 'ma',
 'maint',
 'mais',
 'malgré',
 'me',
 'même',
 'mêmes',
 'merci',
 'mes',
 'mien',
 'mienne',
 'miennes',
 'miens',
 'mille',
 'mince',
 'moi',
 'moi-même',
 'moins',
 'mon',
 'moyennant',
 'n',
 'na',
 'ne',
 'néanmoins',
 'neuf',
 'neuvième',
 'ni',
 'nombreuses',
 'nombreux',
 'non',
 'nos',
 'notre',
 'nôtre',
 'nôtres',
 'nous',
 'nous-mêmes',
 'nul',
 'o',
 'o|',
 'ô',
 'oh',
 'ohé',
 'olé',
 'ollé',
 'on',
 'ont',
 'onze',
 'onzième',
 'ore',
 'ou',
 'où',
 'ouf',
 'ouias',
 'oust',
 'ouste',
 'outre',
 'p',
 'paf',
 'pan',
 'par',
 'parmi',
 'partant',
 'particulier',
 'particulière',
 'particulièrement',
 'pas',
 'passé',
 'pendant',
 'personne',
 'peu',
 'peut',
 'peuvent',
 'peux',
 'pff',
 'pfft',
 'pfut',
 'pif',
 'plein',
 'plouf',
 'plus',
 'plusieurs',
 'plutôt',
 'pouah',
 'pour',
 'pourquoi',
 'premier',
 'première',
 'premièrement',
 'près',
 'proche',
 'psitt',
 'puisque',
 'q',
 'qu',
 'quand',
 'quant',
 'quanta',
 'quant-à-soi',
 'quarante',
 'quatorze',
 'quatre',
 'quatre-vingt',
 'quatrième',
 'quatrièmement',
 'que',
 'quel',
 'quelconque',
 'quelle',
 'quelles',
 'quelque',
 'quelques',
 "quelqu'un",
 'quels',
 'qui',
 'quiconque',
 'quinze',
 'quoi',
 'quoique',
 'r',
 'revoici',
 'revoilà',
 'rien',
 's',
 'sa',
 'sacrebleu',
 'sans',
 'sapristi',
 'sauf',
 'se',
 'seize',
 'selon',
 'sept',
 'septième',
 'sera',
 'seront',
 'ses',
 'si',
 'sien',
 'sienne',
 'siennes',
 'siens',
 'sinon',
 'six',
 'sixième',
 'soi',
 'soi-même',
 'soit',
 'soixante',
 'son',
 'sont',
 'sous',
 'stop',
 'suis',
 'suivant',
 'sur',
 'surtout',
 't',
 'ta',
 'tac',
 'tant',
 'te',
 'té',
 'tel',
 'telle',
 'tellement',
 'telles',
 'tels',
 'tenant',
 'tes',
 'tic',
 'tien',
 'tienne',
 'tiennes',
 'tiens',
 'toc',
 'toi',
 'toi-même',
 'ton',
 'touchant',
 'toujours',
 'tous',
 'tout',
 'toute',
 'toutes',
 'treize',
 'trente',
 'très',
 'trois',
 'troisième',
 'troisièmement',
 'trop',
 'tsoin',
 'tsouin',
 'tu',
 'u',
 'un',
 'une',
 'unes',
 'uns',
 'v',
 'va',
 'vais',
 'vas',
 'vé',
 'vers',
 'via',
 'vif',
 'vifs',
 'vingt',
 'vivat',
 'vive',
 'vives',
 'vlan',
 'voici',
 'voilà',
 'vont',
 'vos',
 'votre',
 'vôtre',
 'vôtres',
 'vous',
 'vous-mêmes',
 'vu',
 'w',
 'x',
 'y',
 'z',
 'zut']
    
####################################MAIN##############################################              
    
if __name__ == "__main__":
      
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
   
    MainWindow.show()
    sys.exit(app.exec_())
    
