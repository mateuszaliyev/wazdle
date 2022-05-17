from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from core.theme import Theme


class Tile(QLabel):
    def __init__(self, letter):
        super().__init__(letter)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(62, 62)
        self.setFont(Theme.fonts.sans(25))
        self.setStyleSheet((
            f"border: 2px solid {Theme.colors.border};"
            f"color: {Theme.colors.foreground};"
        ))
