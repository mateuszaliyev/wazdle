from json import loads
from random import choice

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from core.settings import Settings
from core.theme import Theme

from widgets.row import Row


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.currentRow = 0
        self.gameOver = False
        self.rows = [Row() for i in range(Settings.tries)]
        self.toast = None

        self.words = self.getWords(Settings.language)

        self.word = self.getNewWord()

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

    def getNewWord(self):
        return choice(self.words[f"{Settings.letters}"][:1000]).upper()

    def getWords(self, language):
        dataFile = open(f"src\\data\\{Settings.language}.json", "r")
        data = loads(dataFile.read())
        dataFile.close()

        return data

    def handleGameOver(self, success):
        self.gameOver = True

        if self.toast != None and success == False:
            self.toast.change(self.word)
            self.toast.show()

    def handleNewGame(self):
        if self.toast != None:
            self.toast.hide()
            self.toast.change("")

        self.currentRow = 0
        self.word = self.getNewWord()

        for row in self.rows:
            row.reset()

        self.gameOver = False

    def handleSubmit(self, guess):
        isInWordList = False

        for word in self.words[f"{Settings.letters}"]:
            if guess == word.upper():
                isInWordList = True

        if not isInWordList:
            self.toast.change("Not in word list")
            self.toast.show()
            return

        self.toast.hide()
        self.toast.change("")
        self.reveal(guess)

        if guess == self.word:
            self.handleGameOver(True)
            return

        if self.currentRow < Settings.tries - 1:
            self.currentRow += 1
            return

        self.handleGameOver(False)

    def onKeyPress(self, key):
        if self.gameOver and key == Qt.Key.Key_Return.value:
            self.handleNewGame()
            return

        if key == Qt.Key.Key_Backspace.value:
            self.toast.hide()
            self.toast.change("")

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

    def setToast(self, toast):
        self.toast = toast
