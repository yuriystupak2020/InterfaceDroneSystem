from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, \
                            QStatusBar, QToolButton
import sys
# import main

class Modes(QMainWindow):
   def __init__(self):
      super(Modes, self).__init__()
      self.uicMain = uic.loadUi('modes.ui', self)
      #self.setStyleSheet("background-color: #b8b2b2;")
      self.move(250, 0)

      self.setStyleSheet("background-image: url(resources/images/back_image_mine_page.png);")

      self.show()

      self.toolButtonModes = self.findChild(QToolButton, "toolButtonHome")
      self.toolButtonModes.clicked.connect(self.home)


   def home(self):
      print("home page!!!")
      self.close()




"""
      Це зосталось від Телло дрона керування
      # self.textBat = self.findChild(QPlainTextEdit, "textBat")
      # self.textWiFi = self.findChild(QPlainTextEdit, "textWiFi")
      # self.textWiFi = self.findChild(QPlainTextEdit, "textWiFi")
      #
      # self.progressBarBat = self.findChild(QProgressBar, "progressBarBat")
      # self.progressBarWiFi = self.findChild(QProgressBar, "progressBarWiFi")
      # self.progressBarWiFi = self.findChild(QProgressBar, "progressBarWiFi")
      #
      # self.labelReply = self.findChild(QLabel, "Order")
      # self.labelOrder = self.findChild(QLabel, "Order")
"""
stylesheet = """
    MainWindow {
        background-image: url("resources/images/back_image_mine_page.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)

    modes = Modes()
    modes.show()

    sys.exit(app.exec_())
