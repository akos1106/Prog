# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'peoplevXKvFK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#én
from mTT import Worker
from mTT import MissingDataException,EmailFormatException,PhoneNumberFormatException
import re

class Ui_MainWindow(object):

    #ÉN
    myWorkersList=[]


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 161, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 161, 51))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 161, 51))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 161, 51))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 161, 51))
        self.inName = QLineEdit(self.centralwidget)
        self.inName.setObjectName(u"inName")
        self.inName.setGeometry(QRect(80, 20, 661, 31))
        self.inID = QLineEdit(self.centralwidget)
        self.inID.setObjectName(u"inID")
        self.inID.setGeometry(QRect(100, 70, 641, 31))
        self.inAddress = QLineEdit(self.centralwidget)
        self.inAddress.setObjectName(u"inAddress")
        self.inAddress.setGeometry(QRect(90, 120, 651, 31))
        self.inPhone = QLineEdit(self.centralwidget)
        self.inPhone.setObjectName(u"inPhone")
        self.inPhone.setGeometry(QRect(150, 170, 591, 31))
        self.inPhone.setAutoFillBackground(False)
        self.inEmail = QLineEdit(self.centralwidget)
        self.inEmail.setObjectName(u"inEmail")
        self.inEmail.setGeometry(QRect(70, 220, 671, 31))
        self.buttonAdd = QPushButton(self.centralwidget)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setGeometry(QRect(10, 280, 101, 41))
        self.buttonEdit = QPushButton(self.centralwidget)
        self.buttonEdit.setObjectName(u"buttonEdit")
        self.buttonEdit.setGeometry(QRect(140, 280, 101, 41))
        self.buttonModify = QPushButton(self.centralwidget)
        self.buttonModify.setObjectName(u"buttonModify")
        self.buttonModify.setGeometry(QRect(270, 280, 101, 41))
        self.buttonDelete = QPushButton(self.centralwidget)
        self.buttonDelete.setObjectName(u"buttonDelete")
        self.buttonDelete.setGeometry(QRect(400, 280, 101, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 330, 161, 51))
        self.outPersons = QListWidget(self.centralwidget)
        self.outPersons.setObjectName(u"outPersons")
        self.outPersons.setGeometry(QRect(10, 380, 731, 251))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 763, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #ÉN
        self.buttonAdd.clicked.connect(self.addNewWorker)
        self.buttonEdit.clicked.connect(self.editButtonClicked)
        self.buttonModify.clicked.connect(self.addNewWorker)
        self.buttonDelete.clicked.connect(self.deleteWorker)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Name:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">ID code:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Address:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Phone number:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Email:</span></p></body></html>", None))
        self.inPhone.setText("")
        self.inPhone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+36301234567", None))
        self.buttonAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.buttonEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.buttonModify.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.buttonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">List of persons:</span></p></body></html>", None))

        #én
        self.reloadData()

    #ÉN
    def clearInputs(self):
        self.inID.setText("")
        self.inName.setText("")
        self.inAddress.setText("")
        self.inPhone.setText("")
        self.inEmail.setText("")

    def addNewWorker(self):
        try:
            name=self.inName.text()
            id=self.inID.text()
            address=self.inAddress.text()
            phone_number=self.inPhone.text()
            email=self.inEmail.text()

            if name=="":
                raise MissingDataException("name")
            if not id:
                raise MissingDataException("id")
            if not address:
                raise MissingDataException("address")
            if not phone_number:
                raise MissingDataException("phone_number")
            if not email:
                raise MissingDataException("email")

            mail="valami@valami.hu"
            if re.match('a+',mail):
                print("yes")



        except MissingDataException as e:
            msg = QMessageBox()
            msg.setText(e.__str__())
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()

        except PhoneNumberFormatException:
            msg = QMessageBox()
            msg.setText("Nem jó formátum a telefonszám")
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()

        except EmailFormatException:
            msg = QMessageBox()
            msg.setText("Nem jó formátum az email")
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()

        else:
            if not self.inID.isReadOnly():
                tmpWorker=Worker(name,id,address,phone_number,email)

                if tmpWorker not in self.myWorkersList:
                    self.myWorkersList.append(tmpWorker)
                    self.outPersons.clear()
                    self.saveToFile()

                    for worker in self.myWorkersList:
                        self.outPersons.addItem(worker.__str__())

                    self.inID.setReadOnly(False)

                else:
                    msg=QMessageBox()
                    msg.setText("Ez az adat már szerepel az adatbázisban")
                    msg.setWindowTitle("Warning")
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.exec()

            else:
                for worker in self.myWorkersList:
                    if worker.id==id:
                        worker.name=name
                        worker.phone_number=phone_number
                        worker.email=email
                        worker.address=address

                self.outPersons.clear()
                self.saveToFile()

                for worker in self.myWorkersList:
                    self.outPersons.addItem(worker.__str__())

            self.clearInputs()




    def editButtonClicked(self):
        worker =self.outPersons.currentItem()
        if not worker:
            msg = QMessageBox()
            msg.setText("Nem választott ki adatot")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.exec()
        else:
            worker=worker.text()
            worker_li=worker.split(',')

            self.inName.setText(worker_li[0])
            self.inID.setText(worker_li[1])
            self.inAddress.setText(worker_li[2])
            self.inPhone.setText(worker_li[3])
            self.inEmail.setText(worker_li[4])
            self.inID.setReadOnly(True)     #IDt nem tudjuk átírni


    def deleteWorker(self):
        worker = self.outPersons.currentItem()
        if not worker:
            msg = QMessageBox()
            msg.setText("Nem választott ki adatot a törléshez")
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
        else:
            worker = worker.text()
            worker_li = worker.split(',')
            workerid=worker_li[1]
            for worker in self.myWorkersList:
                if worker.id==workerid:
                    self.myWorkersList.remove(worker)
                    break

            self.outPersons.clear()
            self.saveToFile()

            for worker in self.myWorkersList:
                self.outPersons.addItem(worker.__str__())

    def saveToFile(self):
        f=open("dadatabseee.txt","w")
        for w in self.myWorkersList:
            print(w.__str__(),file=f)
        f.close()


    def reloadData(self):
        f=open("dadatabseee.txt","r")
        for line in f:
            linee=line.rstrip().split(",")
            tmpworker=Worker(linee[0],linee[1],linee[2],linee[3],linee[4])
            self.myWorkersList.append(tmpworker)

        for worker in self.myWorkersList:
            self.outPersons.addItem(worker.__str__())

#én
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())