
import sys
import datetime
#from PyQt5 import QtGui
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


def Main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


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


if __name__ == '__main__':
    Main()