from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

from core.settings import Settings
from core.theme import Theme

from widgets.header import Header


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
        header = Header()

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
