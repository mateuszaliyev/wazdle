from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget

from core.settings import Settings
from core.theme import Theme

from widgets.header import Header
from widgets.game import Game


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 500)

        self.setWindowTitle("Wążdle")
        self.setWindowIcon(QIcon("assets\icon.svg"))

        self.setStyleSheet((
            f"background-color: {Theme.colors.background}"
        ))

        QFontDatabase.addApplicationFont("assets\\clear-sans-bold.ttf")
        QFontDatabase.addApplicationFont("assets\\nyt-karnak-condensed.ttf")

        self.header = Header()
        self.game = Game()

        layout = QVBoxLayout()
        layout.addWidget(self.header)
        layout.addWidget(self.game)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape.value:
            self.close()

        self.game.onKeyPress(event.key())
