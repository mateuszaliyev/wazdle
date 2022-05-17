from PyQt6.QtWidgets import QVBoxLayout, QWidget

from core.settings import Settings

from widgets.row import Row


class Board(QWidget):
    def __init__(self):
        super().__init__()

        self.currentRow = 0

        self.rows = [Row() for i in range(Settings.tries)]

        layout = QVBoxLayout()
        layout.setSpacing(5)

        for row in self.rows:
            row.onSubmit(self.handleSubmit)
            layout.addWidget(row)

        self.setLayout(layout)

    def handleSubmit(self):
        self.currentRow += 1

    def onKeyPress(self, key):
        self.rows[self.currentRow].onKeyPress(key)
