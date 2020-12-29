
import sys
import datetime




#Sample1
'''
def Main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.setWindowTitle('QtSample')
    w.setWindowIcon(QIcon('pythonlogo.png'))
    w.show()
    sys.exit(app.exec_())
'''

#Sample2
'''
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()

        timer = QTimer(self)

        timer.timeout.connect(self.time_draw)
        timer.start(1000)


    def time_draw(self):
        d = datetime.datetime.today()
        daystr = d.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(daystr)
'''

#Sample3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUI()

    def InitUI(self):
        exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exit_action = QAction(exit_gui, '&Exit', self)
        exit_action.setShortcut('ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(qApp.quit)

        qtinfo_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        qtinfo_action = QAction(qtinfo_gui, '&AboutQt', self)
        qtinfo_action.setShortcut('Ctrl+I')
        qtinfo_action.setStatusTip('Show Qt Info')
        qtinfo_action.triggered.connect(qApp.aboutQt)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&Info')
        filemenu.addAction(qtinfo_action)
        filemenu.addAction(exit_action)

        menubar.setNativeMenuBar(False)  # for mac

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

def Main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Main()