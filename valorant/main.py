from PyQt5 import QtCore, QtGui, QtWidgets
import os
import utils
import config
import hashlib
from utils import add as ad

class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)
class LoginWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("LogInWindow")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
       
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 281, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.disableButton)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Log In")
        self.pushButton.setEnabled(False)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 150, 111, 20))
        self.label.setObjectName("label")
        self.label.setText("Enter Master Key : ")


        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Log In")

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('Invalid Password. Please Try Again.')
        self.msg.setWindowTitle("Error")
        

        self.pushButton.clicked.connect(self.check_password)
   


    def disableButton(self):
        if len(self.lineEdit.text())>5:
            self.pushButton.setEnabled(True)

    def check_password(self):
        password = self.lineEdit.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db = utils.dbconfig.dbconfig()
        cursor = db.cursor()
        query = "SELECT * FROM secrets"
        cursor.execute(query)
        result = cursor.fetchall()[0]
        if hashed_password != result[0]:
            self.msg.exec_()
            return


        self.goto("main")


class ConfigureWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("SingnUpWindow")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
       
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 150, 281, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.disableButton)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Submit")
        self.pushButton.setEnabled(False)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 150, 111, 20))
        self.label.setObjectName("label")
        self.label.setText("Enter Master Key : ")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 200, 281, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.disableButton)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 131, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Re Enter Master Key : ")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Sing UP")

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('Passwords do not match')
        self.msg.setWindowTitle("Error")
        

        self.pushButton.clicked.connect(self.configure)
   


    def disableButton(self):
        if len(self.lineEdit.text())>5 and len(self.lineEdit_2.text())>5:
            self.pushButton.setEnabled(True)

    def configure(self):
        
        if self.lineEdit.text() != self.lineEdit_2.text():
            self.msg.exec_()
            return
        config.make(self.lineEdit.text())

        



        self.goto("main")


class MainWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Valorant Launcher")
        self.UiComponents()

    def add_entry(self):
        if self.lineEdit.text() != self.lineEdit_2.text():
            self.msg.setInformativeText("Passwords do not match")
            self.msg.exec_()
            return
        res = ad.addEntry(self.lineEdit_1.text(), self.lineEdit.text())
        if res == False:
            self.msg.setInformativeText("Username Already Exists")
            self.msg.exec_()
            return
        else:
            self.msg_1.exec_()
            return



    def disableButton(self):
        if len(self.lineEdit.text()) and len(self.lineEdit_2.text()) and len(self.lineEdit_1.text()) :
            self.pushButton.setEnabled(True)

    def UiComponents(self):

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(250, 100, 281, 22))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.textChanged.connect(self.disableButton)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(250, 150, 281, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.disableButton)

        
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 200, 281, 22))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textChanged.connect(self.disableButton)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(210, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Add")
        self.pushButton.setEnabled(False)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 150, 170, 20))
        self.label.setObjectName("label")
        self.label.setText("Enter Valorant Password : ")

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(40, 100, 170, 20))
        self.label_1.setObjectName("label")
        self.label_1.setText("Enter Valorant Username : ")

        

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 170, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Re Enter Valorant Password : ")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Add new account")

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('Passwords do not match')
        self.msg.setWindowTitle("Error")

        self.msg_1 = QtWidgets.QMessageBox()
        self.msg_1.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_1.setText("Success")
        self.msg_1.setInformativeText('Account Added')
        self.msg_1.setWindowTitle("Done")
        

        self.pushButton.clicked.connect(self.add_entry)

      
       

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        if config.checkConfig():
            self.f=0
        else:
            self.f=1
        
        super().__init__(parent)
        self.setFixedSize(640, 480)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        if self.f:
            self.register(ConfigureWindow(), "configure")
        else:
            self.register(LoginWindow(), "login")

        self.register(MainWindow(), "main")
        if self.f:
            self.goto("configure")
        else:
            self.goto("login")


    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())