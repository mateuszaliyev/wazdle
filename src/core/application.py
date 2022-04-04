import sys

from PyQt6.QtWidgets import QApplication
from widgets.window import Window


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.window = Window()
        self.window.show()

        sys.exit(self.exec())
