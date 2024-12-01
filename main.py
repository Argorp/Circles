import sys

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from random import randint
from UI import Ui_Form


def make_color() -> QColor:
    r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
    return QColor(r, g, b)


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        count_of_circles = randint(3, 10)
        for i in range(count_of_circles):
            qp.setBrush(make_color())
            d = randint(20, 50)
            x, y = randint(d, 1000 - d), randint(d, 1000 - d)
            qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())