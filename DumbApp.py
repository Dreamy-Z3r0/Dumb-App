import sys
from container import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        self.index = 0

        super(MainWindow, self).__init__()
        self.setWindowTitle("Don't get bored...")

        self.label = QLabel()
        self.setCentralWidget(self.label)

        # Create a QTimer
        self.timer = QTimer()
        self.timer.setInterval(50)  # Trigger every 1 second (1000 ms)

        # Connect the QTimer timeout signal to our update function
        self.timer.timeout.connect(self.update_label)

        # Start the timer
        self.timer.start()

        # Update the time display immediately
        self.update_label() 

    def update_label(self):
        pixmap = QPixmap()
        pixmap.loadFromData(frames[self.index])
        self.label.setPixmap(pixmap)

        self.index += 1
        if self.index == len(frames):
            self.index = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()