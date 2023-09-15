import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic



class Tank(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 900, 650
        self.setMinimumSize(self.window_width, self.window_height)
        self.move(250, 0)
        self.uicMain = uic.loadUi('tank.ui', self)
        self.setStyleSheet("background-image: url(resources/images/back_image_mine_page.png);")

        self.show()
        # layout = QVBoxLayout()
        # self.setLayout(layout)


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)


    myApp = Tank()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

