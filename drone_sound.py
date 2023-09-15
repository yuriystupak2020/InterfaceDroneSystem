from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, \
                            QStatusBar, QToolButton, QFrame
import sys

class DroneSound(QMainWindow):
   def __init__(self):
      super(DroneSound, self).__init__()
      self.uicMain = uic.loadUi('drone_sound.ui', self)
      #self.setStyleSheet("background-color: #b8b2b2;")
      self.setStyleSheet("background-image: url(resources/images/back_image_mine_page.png);")
      self.move(250, 0)

      self.frame_schemes = self.findChild(QFrame, "frame_schemes")
      self.frame_schemes.setStyleSheet("margin-top: 22px;image: url(resources/images/sound_drone_conf1.png);background: transparent;")

      self.show()


   #    self.toolButtonModes = self.findChild(QToolButton, "toolButtonServer")
   #    self.toolButtonModes.clicked.connect(self.land)
   #
   # def land(self):
   #     print("land!!!")




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



if __name__ == '__main__':
    app = QApplication(sys.argv)

    sound = DroneSound()
    sound.show()

    sys.exit(app.exec_())
