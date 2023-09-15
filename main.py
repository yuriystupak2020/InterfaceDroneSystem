from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, \
                            QStatusBar, QToolButton, QDesktopWidget, QProgressBar
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint


import sys
import modes
import mine2
import drone_sound
import tank

#import video_camera


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.uicMain = uic.loadUi('main.ui', self)

      self.initUI()

      self.toolButtonModes = self.findChild(QToolButton, "toolButtonModes")
      self.toolButtonModes.clicked.connect(self.modes)

      self.toolButtonMines = self.findChild(QToolButton, "toolButtonMines")
      self.toolButtonMines.clicked.connect(self.mines)

      self.toolButtonSoundMode = self.findChild(QToolButton, "toolButtonSoundMode")
      self.toolButtonSoundMode.clicked.connect(self.sound_mode)

      self.toolButtonCar = self.findChild(QToolButton, "toolButtonCar")
      self.toolButtonCar.clicked.connect(self.tank)
      self.toolButtonDrone = self.findChild(QToolButton, "toolButtonDrone")
      self.toolButtonDrone.clicked.connect(self.tank)
      self.toolButtonTank = self.findChild(QToolButton, "toolButtonTank")
      self.toolButtonTank.clicked.connect(self.tank)
      self.toolButtonArta = self.findChild(QToolButton, "toolButtonArta")
      self.toolButtonArta.clicked.connect(self.tank)
      self.toolButtonMortar = self.findChild(QToolButton, "toolButtonMortar")
      self.toolButtonMortar.clicked.connect(self.tank)
      self.toolButtonTank = self.findChild(QToolButton, "toolButtonTank")
      self.toolButtonTank.clicked.connect(self.tank)
      self.toolButtonSoldier = self.findChild(QToolButton, "toolButtonSoldier")
      self.toolButtonSoldier.clicked.connect(self.tank)


      # self.toolButtonInfrared = self.findChild(QToolButton, "toolButtonInfrared")
      # self.toolButtonInfrared.clicked.connect(self.camera_window)

      # self.toolButtonVisibility = self.findChild(QToolButton, "toolButtonVisibility")
      # self.toolButtonVisibility.clicked.connect(self.invisible_window)


   def initUI(self):
       #self.flagScreen = False
       self.setWindowTitle("DroneSystemUkraine")

       #self.resize(self.height(), self.height())
       self.setStyleSheet("background-image: url(resources/images/back_image_mine_page.png);")
       #self.setStyleSheet("background-color: #939393;")
       # self.setWindowFlags(Qt.FramelessWindowHint)
       # self.setAttribute(Qt.WA_TranslucentBackground)
       self.center()
       self.show()


   def center(self):
       qr = self.frameGeometry()
       cp = QDesktopWidget().availableGeometry().center()
       self.showMaximized()
       #qr.moveCenter(cp)
       self.move(qr.topLeft())


   def modes(self):
       print("modes!!!")
       modes.Modes()

   def mines(self):
       print("mines!!!")
       mine2.DroneMines()

   def sound_mode(self):
       print("sound_mode!!!")
       drone_sound.DroneSound()

   def tank(self):
       print("tank!!!")
       tank.Tank()



   # def camera_window(self):
   #     #self.video_camera = video_camera.Window()
   #     w = video_camera.Window()
   #     w.show()




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
# stylesheet = """
#     MainWindow {
#         background-image: url("resources/images/back_image_mine_page.png");
#         background-repeat: no-repeat;
#         background-position: center;
#     }
# """


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #app.setStyleSheet(stylesheet)
    demo = MainWindow()

    sys.exit(app.exec_())
