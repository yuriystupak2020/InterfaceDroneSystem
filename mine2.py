from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, \
                            QStatusBar, QToolButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame
import sys
import io
import folium # pip install folium
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip installer PyQtWebEngine


class DroneMines(QMainWindow):
   def __init__(self):
      super(DroneMines, self).__init__()
      self.uicMain = uic.loadUi('mine2.ui', self)
      self.setStyleSheet("background-image: url(resources/images/back_image_mine_page.png);")
      self.move(150, 0)
      self.labelMap = self.findChild(QLabel, "labelMap")

      self.verticalLayoutMaps2 = self.findChild(QVBoxLayout, "verticalLayoutMaps2")
      self.setLayout(self.verticalLayoutMaps2)

      coordinate = (47.758114271652445, 37.11030376507498)
      m = folium.Map(title='Mine field',
                 zoom_start=13,
                 location=coordinate)
      # save data to data object
      data = io.BytesIO()
      m.save(data, close_file=False)

      webView = QWebEngineView()
      webView.setHtml(data.getvalue().decode())
      self.verticalLayoutMaps2.addWidget(webView)

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
    mines = DroneMines()
    mines.show()

    sys.exit(app.exec_())
