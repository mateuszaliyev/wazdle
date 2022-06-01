from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from core.settings import Settings
from core.theme import Theme

from widgets.row import Row


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.currentRow = 0
        self.rows = [Row() for i in range(Settings.tries)]
        self.word = self.getNewWord(Settings.letters)

        self.board = QWidget()
        boardLayout = QVBoxLayout()
        boardLayout.setSpacing(5)

        for row in self.rows:
            row.onSubmit(self.handleSubmit)
            boardLayout.addWidget(row)

        self.board.setLayout(boardLayout)

        layout = QVBoxLayout()
        layout.addWidget(self.board)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def getNewWord(self, letters):
        return "PYTON"

    def handleSubmit(self, guess):
        self.reveal(guess)

        self.currentRow += 1

    def onKeyPress(self, key):
        self.rows[self.currentRow].onKeyPress(key)

    def reveal(self, guess):
        letterCount = {}

        for letter in self.word:
            if letter in letterCount:
                letterCount[letter] += 1
                continue

            letterCount[letter] = 1

        for index, tile in enumerate(self.rows[self.currentRow].tiles):
            if guess[index] == self.word[index]:
                tile.setCorrect()
                letterCount[guess[index]] -= 1

        for index, tile in enumerate(self.rows[self.currentRow].tiles):
            if guess[index] == self.word[index]:
                continue

            if guess[index] in self.word and letterCount[guess[index]] > 0:
                tile.setPresent()
                letterCount[guess[index]] -= 1
                continue

            tile.setAbsent()
