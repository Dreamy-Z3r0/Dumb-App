import sys
from container import *
from functools import partial

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QLabel, QPushButton,
    QVBoxLayout
)
from PyQt5.QtGui import QPixmap, QFontMetrics
from PyQt5.QtCore import QTimer
import PyQt5.QtCore as QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a QTimer
        self.timer = QTimer()

        # Load main window contents
        self.Welcome_Menu()
        

    def Welcome_Menu(self):
        self.setWindowTitle('Dumb App')

        layout = QVBoxLayout()

        self.label = QLabel('DUMB APP')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        layout.addWidget(self.label)

        buttons = []
        buttonLabels = []

        buttonLabels.append('Snake game')
        buttonLabels.append('Surprisingly suspicious')
        
        for i, buttonLabel in enumerate(buttonLabels):
            buttons.append(QPushButton(buttonLabel))
            buttons[-1].setCheckable(True)
            buttons[-1].clicked.connect(partial(self.WelcomeMenu_ButtonRoutines,buttonLabel))

            layout.addWidget(buttons[-1])

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.adjustSize()

    def WelcomeMenu_ButtonRoutines(self, buttonLabel):
        if buttonLabel == 'Main':
            try:
                self.timer.stop()
            except:
                pass
            finally:
                self.Welcome_Menu()
        else:
            if buttonLabel == 'Surprisingly suspicious':
                self.Sus_Window()
            else:
                pass

    def Snake_Game(self):
        self.setWindowTitle('Snake Game')

        layout = QVBoxLayout()

    def Sus_Window(self):
        self.setWindowTitle("Don't get bored...")
        self.index = 0

        layout = QVBoxLayout()

        button = QPushButton('Back')
        font_metrics = QFontMetrics(button.font())
        textWidth = font_metrics.width(button.text())
        textHeight = font_metrics.height()

        button.setFixedWidth(textWidth + 20)
        button.setFixedHeight(textHeight + 10)

        button.setCheckable(True)
        button.clicked.connect(partial(self.WelcomeMenu_ButtonRoutines, 'Main'))
        layout.addWidget(button)

        self.update_label()
        layout.addWidget(self.label)

        # Stop timer (if running)
        try:
            self.timer.stop()
        except:
            pass

        # Update refresh rate -> 20Hz
        self.timer.setInterval(50)

        # Connect the QTimer timeout signal
        self.timer.timeout.connect(self.update_label)

        # Start the timer
        self.timer.start()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

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