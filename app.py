import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#import pandas as pd 
import datetime
import time
#from pandas_datareader import data, wb
from pandas_datareader import data as web
import matplotlib.pyplot as plt 
from matplotlib import style

 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'DN-finance'
        self.left = 520
        self.top = 200
        self.width = 305
        self.height = 400

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumSize(305, 400) 

        # Create textbox
        self.code = QLabel(self)
        self.code.setText('Code of stock:')
        self.code.move(48, 20)
        self.code.resize(200, 30)
        self.textbox = QLineEdit(self)
        self.textbox.move(150, 20)
        self.textbox.resize(130,30)
        #textboxdaystart
        self.dayname = QLabel(self)
        self.dayname.resize(150, 30)
        self.dayname.setText('dd/mm/yyyy start:')
        self.dayname.move(20, 60)
        self.day = QLineEdit(self)
        self.day.move(150, 60)
        self.day.resize(30,30)

        self.month = QLineEdit(self)
        self.month.move(190, 60)
        self.month.resize(30,30)

        self.year = QLineEdit(self)
        self.year.move(230, 60)
        self.year.resize(50,30)

        self.dayend = QLabel(self)
        self.dayend.resize(300, 30)
        self.dayend.setText('dd/mm/yyyy   end:')
        self.dayend.move(20, 100)
        # check dayend1:
        self.checkbox1 = QCheckBox("TODAY",self)
        self.checkbox1.move(150, 100)
        # check dayend2:
        self.checkbox2 = QCheckBox("Choose a day:",self)
        self.checkbox2.resize(200, 30)
        #self.checkbox2.toggle()
        self.checkbox2.move(150, 120)

        
        self.day2 = QLineEdit(self)
        self.day2.move(150, 150)
        self.day2.resize(30,30)

        self.month2 = QLineEdit(self)
        self.month2.move(190, 150)
        self.month2.resize(30,30)

        self.year2 = QLineEdit(self)
        self.year2.move(230, 150)
        self.year2.resize(50,30)

        # checkbox xuat file du lieu
        self.getfile = QLabel("Get file:",self)
        self.getfile.move(90, 190)

        self.csv = QCheckBox('CSV file - .csv',self)
        self.csv.resize(150, 20)
        self.csv.move(150, 195)

        self.html = QCheckBox('HTML file - .html',self)
        self.html.resize(150, 20)
        self.html.move(150, 215)

        self.xlsx = QCheckBox('EXCEL file - .xlsx',self)
        self.xlsx.resize(150, 20)
        self.xlsx.move(150, 235)

        self.filename = QLabel("File name: ",self)
        self.filename.move(75, 265)

        self.filename = QLineEdit(self)
        self.filename.move(150, 265)
        self.filename.resize(130,30)


        # do thi:
        self.plot = QLabel("Plot:",self)
        self.plot.move(90, 305)

        self.close = QCheckBox('Adj Close',self)
        self.close.resize(150, 20)
        self.close.move(150, 310)

        self.volume = QCheckBox('Volume',self)
        self.volume.resize(150, 20)
        self.volume.move(150, 330)


        # Create a button in the window
        self.button = QPushButton('Apply', self)
        self.button.move(210,360)
        self.button.resize(70, 30)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    #def on_check(self):
    #    if self.checkbox1.isChecked() and self.checkbox2.isChecked():
    #        self.msg = QMessageBox()
    #        self.msg.setIcon(QMessageBox.Critical)
    #        self.msg.setText('Choose one box!')
    #        self.msg.setStandardButtons(QMessageBox.Ok)
    #        self.show()

        
    @pyqtSlot()
    def on_click(self):
        
        # lay thoi gian bat dau:
        textboxValue = self.textbox.text()
        tbday = self.day.text()
        tbmonth = self.month.text()
        tbyear = self.year.text()
        start = datetime.datetime(int(tbyear), int(tbmonth), int(tbday))
        # done!
        if self.checkbox1.isChecked():
            #get today:
            s = time.asctime(time.localtime(time.time()))
            s = s.split()
            dic = {'Jan':1, 'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
            end = datetime.datetime(int(s[4]), dic[s[1]], int(s[2])) #today
        elif self.checkbox2.isChecked():
            #lay thoi gian ket thuc duoc nhap
            dayend = self.day2.text()
            monthend = self.month2.text()
            yearend = self.year2.text()
            end = datetime.datetime(int(yearend), int(monthend) , int(dayend))
    

        # hai ngay cuoi tuan se khong co du lieu
        
        df = web.DataReader(textboxValue, "yahoo", start, end) # san chung khoan nasdaq

        print('RESULT:')
        print(df)

        s = self.filename.text()

        if self.csv.isChecked():
            df.to_csv(s)
        elif self.html.isChecked():
            df.to_html(s)
        elif self.xlsx.isChecked():
            df.to_excel(s)

        if self.close.isChecked():
            df['Adj Close'].plot()
            plt.xlabel('Day')
            plt.ylabel('Point')
            plt.title('Ket qua khi dong cua')
            plt.show()
        else:
            df['Volume'].plot()
            plt.xlabel('Day')
            plt.ylabel('$$$')
            plt.title('Volume')
            plt.show()

    
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
