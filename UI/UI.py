import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,150)
    w.move(30,30)
    w.setWindowTitle('Simple Window')
    w.show()

    sys.exit(app.exec_())