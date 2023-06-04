from PyQt5 import QtCore, QtGui, QtWidgets
import os
import utils
import config
import hashlib
from utils import add as ad
from utils import retrieve as rtr
from functools import partial
import sqlite3
import random 
import time
import subprocess
from utils import dbconfig as dbc
basedir = os.path.dirname(__file__)

class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)
class LoginWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Valorant Account Launcher")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
       
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 360, 60))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont("Epilogue")
        font.setPointSize(12)
        font.setWeight(900)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText(" MASTER PASSWORD") 



        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 260, 360, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("    PROCEED")
        
        font = QtGui.QFont("Impact")
        font.setPointSize(12)
        font.setWeight(400)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("position: absolute;\n"

"/* Primary red */\n"
"\n"
"background: #FF4656;\n"
"border-radius: 4px; \n"
"color: #FFFFFF;\n"
"letter-spacing: 0.2em;\n"
"text-align: left;\n"
)

        # self.label = QtWidgets.QLabel(self)
        # self.label.setGeometry(QtCore.QRect(60, 150, 111, 20))
        # self.label.setObjectName("label")
        # self.label.setText("Enter Master Key : ")


        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 150, 50))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("LOG IN")
        self.label_3.setStyleSheet("position: absolute;\n"
"font-family: \'Impact\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 48px;\n"
"line-height: 59px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")


        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(140, 135, 360, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Use your Master Password to continue")
        self.label_4.setStyleSheet("position: absolute;\n"
"font-family: \'Epilogue\';\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #C7F459;\n"
"")



        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('Invalid Password. Please Try Again.')
        self.msg.setWindowTitle("Error")
        self.msg.setStyleSheet("color:white;background:#0F1923")

        

        self.pushButton.clicked.connect(self.check_password)
   


    

    def check_password(self):
        password = self.lineEdit.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db = dbc.dbconfig()
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
        self.setWindowTitle("Valorant Account Launcher")

    def initUI(self):
        self.UiComponents()

    def UiComponents(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        font = QtGui.QFont("Epilogue")
        font.setPointSize(12)
        font.setWeight(900)

       
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 360, 60))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPalette(palette)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText(" MASTER PASSWORD") 

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 260, 360, 60))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText(" RE-ENTER MASTER PASSWORD") 


        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 340, 360, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("    PROCEED")
        btn_font = QtGui.QFont("Impact")
        btn_font.setPointSize(12)
        btn_font.setWeight(400)
        self.pushButton.setFont(btn_font)
        self.pushButton.setStyleSheet("position: absolute;\n"

"/* Primary red */\n"
"\n"
"background: #FF4656;\n"
"border-radius: 4px; \n"
"color: #FFFFFF;\n"
"letter-spacing: 0.2em;\n"
"text-align: left;\n"
)




        


        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 250, 50))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("REGISTER")
        self.label_3.setStyleSheet("position: absolute;\n"
"font-family: \'Impact\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 48px;\n"
"line-height: 59px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")


        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(140, 135, 440, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Set Master Password, the only password you need to remeber.")
        self.label_4.setStyleSheet("position: absolute;\n"
"font-family: \'Epilogue\';\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #C7F459;\n"
"")





        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        
        self.msg.setWindowTitle("Error")
        self.msg.setStyleSheet("color:white;background:#0F1923")

        

        self.pushButton.clicked.connect(self.configure)
   


    def place_automate_file(self):
        content = '''set "username=%1"
set "password=%2"
        
:start
start "" "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
set "appWindowTitle=Riot Client Main"
:LOOP
timeout /t 1 >nul
powershell -command "$appWindow = (new-object -com wscript.shell).AppActivate('%appWindowTitle%'); if ($appWindow) { exit 0 } else { exit 1 }"
if %errorlevel% equ 1 (
    goto :LOOP
) else (
    powershell -command "(new-object -com wscript.shell).SendKeys('%username%')"
    powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
    powershell -command "(new-object -com wscript.shell).SendKeys('%password%')"
    powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
)
set "appWindowTitle=Riot Client Main"
timeout /t 1 >nul
powershell -command "$appWindow = (new-object -com wscript.shell).AppActivate('%appWindowTitle%'); if ($appWindow) { exit 0 } else { exit 1 }"
if %errorlevel% equ 1 (
    goto :LOOP
) else (
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
      powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
)
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{TAB}')"
powershell -command "(new-object -com wscript.shell).SendKeys('{ENTER}')"
'''
        if not os.path.exists("C:\\RiotLauncher\\"):
            print("h3")
            os.mkdir("C:\\RiotLauncher")

        try:
            print("h4")
            with open("C:\\RiotLauncher\\automate.bat", 'w+') as file_pointer:
                file_pointer.write(content)
        except Exception as e:
            print(e)
            pass


    def configure(self):

        
        if self.lineEdit.text() != self.lineEdit_2.text():
            self.msg.setInformativeText('Passwords do not match')
            self.msg.exec_()
            return
        if len(self.lineEdit.text()) < 7:
            self.msg.setInformativeText('Passwords must be mimum 7 characters')
            self.mesg.exec_()
            return

        config.make(self.lineEdit.text())
        self.place_automate_file()


        



        self.goto("main")

class MainWindow(PageWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.btn=[]
        self.initUI()

    #def retreive_user_account(self):


    def go_to_add(self):
        self.goto("add")
    def initUI(self):

        self.setWindowTitle("Valorant Account Launcher")
        self.UiComponents()
    def UiComponents(self):
        if config.checkConfig():
            self.result = rtr.retrieveEntries()
        else:
            self.result=[]
        
        self.label = QtWidgets.QLabel(self)
        self.label.setFixedSize(290, 20)
        self.label.setObjectName("label")
        self.label.setText("Click on the userID to login into Valorant.")
        self.label.setStyleSheet("position: absolute;\n"
"font-family: \'Epilogue\';\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #C7F459;\n"
"")



        self.add_user_btn = QtWidgets.QPushButton('    ADD NEW USER    ', self)
        self.add_user_btn.clicked.connect(self.go_to_add)
        self.add_user_btn.setFixedSize( 290, 60)
        btn_font = QtGui.QFont("Impact")
        btn_font.setPointSize(12)
        btn_font.setWeight(400)
        self.add_user_btn.setFont(btn_font)
        self.add_user_btn.setStyleSheet("position: absolute;\n"

"/* Primary red */\n"
"\n"
"background: #FF4656;\n"
"border-radius: 4px; \n"
"color: #FFFFFF;\n"
"letter-spacing: 0.2em;\n"
"text-align: left;\n"
)


        self.scroll = QtWidgets.QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QtWidgets.QWidget()                 # Widget that contains the collection of Vertical Box
        self.grid = QtWidgets.QGridLayout()  
        #self.grid.setSpacing(40)                               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.grid.addWidget(self.add_user_btn, 0, 0, 2, 2, QtCore.Qt.AlignTop)
        self.grid.addWidget(self.label,2, 0, 2, 2)


        #self.result = [(str(a),str(a)) for a in range(50)]
        x=2
        for c in range(len(self.result)):
            self.btn.append( QtWidgets.QPushButton('New Button', self))
            
            self.btn[-1].setText(self.result[c][0])
            self.btn[-1].setFont(btn_font)
            self.btn[-1].setFixedSize(290,120)
            self.btn[-1].setStyleSheet("position: absolute;\n"

    "/* Primary red */\n"
    "\n"
    "background: #FF4656;\n"
    "border-radius: 4px; \n"
    "color: #FFFFFF;\n"
    "letter-spacing: 0.2em;\n"
    "text-align: center;\n"
    )


            self.btn[-1].clicked.connect(partial(self.login_valorant, self.result[c]))

            


            i = self.grid.count()     # Subtract 1 for add_btn
            
            if i%2 == 0:
                x+=2
            
            if i%2==0:
                y=(i%2)
            else:
                y=(i % 2)+1
            self.grid.addWidget(self.btn[-1], x, y, 2,2) # Add 1 to row since add_btn is on first row



        self.widget.setLayout(self.grid)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.show()


        
       
    def login_valorant(self, creds):
        
        p = subprocess.Popen(["C:\\RiotLauncher\\automate.bat", creds[0], creds[1]], shell=True)
        o = p.communicate()
        p.wait()
       
        exit(0)

        
           
                




class AddNewUser(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Valorant Account Launcher")
        self.UiComponents()

    def add_entry(self):
        if len(self.lineEdit.text())==0 or len(self.lineEdit_1.text())==0 or len(self.lineEdit_2.text())==0:
            self.msg.setInformativeText("Please fill all fields")
            self.msg.exec_()
            return


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
            self.lineEdit_1.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit.setText("")
            return




    def go_back(self):
        self.goto("main")
    

    def UiComponents(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        font = QtGui.QFont("Epilogue")
        font.setPointSize(12)
        font.setWeight(900)

        self.lineEdit_1 = QtWidgets.QLineEdit(self)
        self.lineEdit_1.setGeometry(QtCore.QRect(140, 170, 360, 40))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_1.setPalette(palette)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setPlaceholderText(" USER NAME") 


        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setGeometry(QtCore.QRect(140, 230, 360, 40))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPalette(palette)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText(" PASSWORD") 

        
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 290, 360, 40))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPalette(palette)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setPlaceholderText(" RE ENTER PASSWORD") 

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 350, 360, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("    ADD")
        
        btn_font = QtGui.QFont("Impact")
        btn_font.setPointSize(12)
        btn_font.setWeight(400)
        self.pushButton.setFont(btn_font)

        self.pushButton.setStyleSheet("position: absolute;\n"

"/* Primary red */\n"
"\n"
"background: #FF4656;\n"
"border-radius: 4px; \n"
"color: #FFFFFF;\n"
"letter-spacing: 0.2em;\n"
"text-align: left;\n"
)


        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(140, 410, 360, 40))
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_1.setText("    BACK")
        btn_font = QtGui.QFont("Impact")
        btn_font.setPointSize(12)
        btn_font.setWeight(400)
        self.pushButton_1.setFont(btn_font)
        self.pushButton_1.setStyleSheet("position: absolute;\n"

"/* Primary red */\n"
"\n"
"background: #FF4656;\n"
"border-radius: 4px; \n"
"color: #FFFFFF;\n"
"letter-spacing: 0.2em;\n"
"text-align: left;\n"
)


       
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(140, 65, 360, 50))
        self.label.setObjectName("label_3")
        self.label.setText("ADD NEW ACCOUNT")
        self.label.setStyleSheet("position: absolute;\n"
"font-family: \'Impact\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 48px;\n"
"line-height: 59px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;\n"
"")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 360, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Enter your Valorant Account Login Credentials")
        self.label_4.setStyleSheet("position: absolute;\n"
"font-family: \'Epilogue\';\n"
"font-style: normal;\n"
"font-weight: 800;\n"
"font-size: 14px;\n"
"line-height: 14px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #C7F459;\n"
"")


        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('Passwords do not match')
        self.msg.setWindowTitle("Error")
        self.msg.setStyleSheet("color:white;background:#0F1923")


        self.msg_1 = QtWidgets.QMessageBox()
        self.msg_1.setIcon(QtWidgets.QMessageBox.Information)
        self.msg_1.setText("Success")
        self.msg_1.setInformativeText('Account Added')
        self.msg_1.setWindowTitle("Done")
        self.msg_1.setStyleSheet("color:white;background:#0F1923")

        

        self.pushButton.clicked.connect(self.add_entry)
        self.pushButton_1.clicked.connect(self.go_back)

      
       

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        if config.checkConfig():
            self.f=0
        else:
            self.f=1
        
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'logo.ico')))
        self.setFixedSize(640, 480)
        self.setStyleSheet("background: #0F1923;\n""")

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        if self.f:
            self.register(ConfigureWindow(), "configure")
        else:
            self.register(LoginWindow(), "login")

        self.register(AddNewUser(), "add")
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
            if name=="main":
                widget.UiComponents()
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":
    import sys
    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

