# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:48:29 2021

@author: a.shamarov
"""
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import numpy
import pickle

class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()

    
  
    # method for components
    def UiComponents(self):
  
        # creating a QCalendarWidget object
        self.calender = QCalendarWidget(self)
  
        # setting geometry to the calender
        self.calender.setGeometry(10, 10, 400, 200)
  
        # creating a label
        label = QLabel(self)
        self.items = ("Приседания", "Пресс", "Поднимание Жопки")
        item = []
        self.calender.clicked.connect(self.showDialog)
        # method to increase the count value
    def showDialog(self):
        text1, ok = QInputDialog.getText(self, 'Упражнения', 'Приседания')
        text2, ok = QInputDialog.getText(self, 'Упражнения', 'Пресс')
        text3, ok = QInputDialog.getText(self, 'Упражнения', 'Поднимание Жопки')
        
        date = self.calender.selectedDate()
        dates = date.toString('dd-MM-yyyy')
        # if ok and item:
        print (dates, text1, text2, text3)
        
        tren1 = 40
        tren2 = 60
        tren3 = 40
        tren1_1 = int(text1) / int(tren1) * 100
        tren1_2 = int(text2) / int(tren2) * 100
        tren1_3 = int(text3) / int(tren3) * 100
        print ("{0:.0f}%".format(tren1_1), "{0:.0f}%".format(tren1_2), "{0:.0f}%".format(tren1_3))
        a = [tren1_1, tren1_2, tren1_3]
        final = numpy.mean(a)
        if int(final) > 100:
            final = 100
        print ("{0:.0f}%".format(final))
        if int(final) == 100:
            print ("Умница мое солнце")
        elif int(final) < 100 and int(final) >= 60:
            print ("Молодец что стараешься")
        elif int(final) < 60 and int(final) >= 30:
            print ("Ты конечно жопка но все равно молодец")
        elif int(final) < 30 and int(final) > 0:
            print ("Ты почти холодец, но все равно стараешься")
        elif int(final) == 0:
            print ("Ты жопа и холодец")
        # dumpi = (dates, ("{0:.0f}%".format(tren1_1), "{0:.0f}%".format(tren1_2), "{0:.0f}%".format(tren1_3)), final)
        # with open('dumpi.pickle', 'ab', 3) as f:
        #     pickle.dump(dumpi, f)
        # data_cam = []
        # try:
        #         with open('dumpi.pickle', 'rb', 3) as f:
        #             while True:
        #                 try:
        #                     data_cam_temp = pickle.load(f)
        #                     data_cam.append(data_cam_temp)
        #                 except EOFError:
        #                     break
        #                 # print("data_cam", data_cam_temp [0:3:2][:])
        # except:
        #     pass
        # print (data_cam)
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())