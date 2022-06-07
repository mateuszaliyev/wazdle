from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from core.settings import Settings

from widgets.tile import Tile


class Row(QWidget):
    def __init__(self):
        super().__init__()

        self.currentTile = 0
        self.handleSubmit = None

        self.tiles = [Tile("") for i in range(Settings.letters)]

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        for tile in self.tiles:
            layout.addWidget(tile)

        self.setLayout(layout)

    def onKeyPress(self, key):
        if self.currentTile > 0 and key == Qt.Key.Key_Backspace.value:
            self.currentTile -= 1
            self.tiles[self.currentTile].setText("")
            return

        if self.currentTile == Settings.letters and key == Qt.Key.Key_Return.value:
            guess = ""

            for tile in self.tiles:
                guess += tile.text()

            if self.handleSubmit is not None:
                self.handleSubmit(guess)

            return

        if self.currentTile < Settings.letters and (key > 64 and key < 91 or key > 96 and key < 123):
            self.tiles[self.currentTile].setText(chr(key).upper())
            self.currentTile += 1
            return

    def onSubmit(self, callback):
        self.handleSubmit = callback

    def reset(self):
        self.currentTile = 0

        for tile in self.tiles:
            tile.setDefault()
            tile.setText("")
