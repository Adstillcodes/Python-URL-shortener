# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(541, 250)
        '''palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)

        MainWindow.setPalette(palette)'''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(10, 20, 521, 41))
        self.url_input.setText("")
        self.url_input.setAlignment(QtCore.Qt.AlignCenter)
        self.url_input.setObjectName("url_input")
        self.butt = QtWidgets.QPushButton(self.centralwidget)
        self.butt.setGeometry(QtCore.QRect(10, 100, 521, 41))
        self.butt.setObjectName("butt")
        self.shortened_url = QtWidgets.QLabel(self.centralwidget)
        self.shortened_url.setGeometry(QtCore.QRect(6, 180, 531, 20))
        self.shortened_url.setText("")
        self.shortened_url.setObjectName("shortened_url")
        self.shortened_url.setAlignment(QtCore.Qt.AlignCenter)
        self.shortened_url.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51); color: rgb(255, 255, 255);")
        MainWindow.setWindowTitle(_translate("MainWindow", "URL Shortener"))
        self.butt.setText(_translate("MainWindow", "Make the URL shorter"))
        self.butt.clicked.connect(self.shorten)

    def shorten(self):
        try:
            short_url = tiny_url(self.url_input.text())
            if(len(short_url) >= len(self.url_input.text())):
                self.shortened_url.setText("Can not make the URL shorter")
            else:
                self.shortened_url.setText(short_url)
        except urllib.error.HTTPError:
            self.shortened_url.setText("Not a valid URL")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

