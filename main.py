import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from random import randint


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.setGeometry(0, 0, 1000, 1000)
        self.need_to_paint = 0
        self.make_circles.clicked.connect(self.do_paint)

    def paintEvent(self, event):
        if self.need_to_paint:
            qp = QPainter()
            qp.begin(self)
            self.main(qp)
            qp.end()
        self.need_to_paint = 0

    def do_paint(self):
        self.need_to_paint = 1
        self.update()

    def main(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        count_of_circles = randint(3, 10)
        for i in range(count_of_circles):
            d = randint(20, 50)
            x, y = randint(d, 1000 - d), randint(d, 1000 - d)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())