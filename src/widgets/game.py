from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from core.theme import Theme

from widgets.board import Board


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.board = Board()

        layout = QVBoxLayout()
        layout.addWidget(self.board)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def onKeyPress(self, key):
        self.board.onKeyPress(key)
