from PyQt5 import QtCore, QtGui, QtWidgets


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
        
        if True:
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


        self.goto("main")


class MainWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Valorant Launcher")
        self.UiComponents()

    def login(self):
        pass

    def UiComponents(self):
        self.backButton = QtWidgets.QPushButton("BackButton", self)
        self.backButton.setGeometry(QtCore.QRect(5, 5, 100, 20))
        self.backButton.clicked.connect(self.login)

      
       

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self.f=0
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