from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from core.theme import Theme


class Toast(QLabel):
    def __init__(self, text, parent):
        super().__init__(text, parent)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setFont(Theme.fonts.sans(12))
        self.setFixedHeight(50)
        self.setStyleSheet((
            f"background-color: {Theme.colors.toastBackground};"
            f"border-radius: 4px;"
            f"color: {Theme.colors.toastForeground};"
            f"padding: 16px;"
        ))

    def change(self, text=None):
        if (text != None):
            self.setText(text)

        self.adjustSize()
        self.move(self.parentWidget().rect().center().x() -
                  self.rect().center().x(), 65)
