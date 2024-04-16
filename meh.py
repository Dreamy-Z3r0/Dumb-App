from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QByteArray, QBuffer
import sys

# Assuming binary_values is your list of binary values
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

# Convert list of binary values to bytes
data_bytes = bytes(binary_values)

# Create QByteArray from bytes
byte_array = QByteArray(data_bytes)

# Create QBuffer from QByteArray
buffer = QBuffer(byte_array)
buffer.open(QBuffer.ReadOnly)

# Create QPixmap from QBuffer
pixmap = QPixmap()
pixmap.loadFromData(buffer.data())

# Create a PyQt5 application
app = QApplication(sys.argv)

# Create a QWidget and set its layout
widget = QWidget()
layout = QVBoxLayout()
widget.setLayout(layout)

# Create a QLabel, set its pixmap, and add it to the layout
label = QLabel()
label.setPixmap(pixmap)
layout.addWidget(label)

# Show the widget
widget.show()

# Start the application
sys.exit(app.exec_())
