import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QWidget, QLabel
    )
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray, QBuffer, QImage, QPainter

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Meh...")

        value = 0
        binary_values = []
        for y in range(320):
            for x in range(640):
                if (y * 320 + x) % 10 == 0:
                    if value == 0:
                        value = 1
                    else:
                        value = 0
                binary_values.append(value)

        byte_array = QByteArray(bytes(binary_values))

        buffer = QBuffer(byte_array)
        buffer.open(QBuffer.ReadOnly)

        pixmap = QPixmap()
        pixmap.loadFromData(buffer.data())

        label = QLabel()
        label.setPixmap(pixmap)

        self.setCentralWidget(label)
        self.resize(640, 320)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


