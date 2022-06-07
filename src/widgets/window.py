from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget

from core.settings import Settings
from core.theme import Theme

from widgets.header import Header
from widgets.game import Game
from widgets.toast import Toast


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 550)

        self.setWindowTitle("Wążdle")
        self.setWindowIcon(QIcon("assets\icon.svg"))

        self.setStyleSheet((
            f"background-color: {Theme.colors.background}"
        ))

        QFontDatabase.addApplicationFont("assets\\clear-sans-bold.ttf")
        QFontDatabase.addApplicationFont("assets\\nyt-karnak-condensed.ttf")

        self.header = Header()
        self.game = Game()

        self.main = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.game)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.main.setLayout(mainLayout)
        self.main.setSizePolicy(
            QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.header)
        layout.addWidget(self.main)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.toast = Toast("", self)
        self.toast.hide()
        self.game.setToast(self.toast)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape.value:
            self.close()

        self.game.onKeyPress(event.key())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.toast.change()
