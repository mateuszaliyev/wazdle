from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from core.theme import Theme


class Tile(QLabel):
    def __init__(self, letter):
        super().__init__(letter)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFixedSize(62, 62)
        self.setFont(Theme.fonts.sans(25))
        self.setColor(Theme.colors.background, Theme.colors.border)

    def setAbsent(self):
        self.setColor(Theme.colors.absent, Theme.colors.absent)

    def setColor(self, backgroundColor, borderColor):
        self.setStyleSheet((
            f"background-color: {backgroundColor};"
            f"border: 2px solid {borderColor};"
            f"color: {Theme.colors.foreground};"
        ))

    def setCorrect(self):
        self.setColor(Theme.colors.correct, Theme.colors.correct)

    def setDefault(self):
        self.setColor(Theme.colors.background, Theme.colors.border)

    def setPresent(self):
        self.setColor(Theme.colors.present, Theme.colors.present)
