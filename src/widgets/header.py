from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout, QWidget

from core.theme import Theme


class Header(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("Wazdle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setContentsMargins(0, 3, 0, 3)
        title.setFont(Theme.fonts.display(28))
        title.setStyleSheet((
            f"border: solid {Theme.colors.border};"
            "border-bottom-width: 1px;"
            f"color: {Theme.colors.foreground};"
        ))

        layout = QHBoxLayout()
        layout.addWidget(title)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
