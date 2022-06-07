from PyQt6.QtGui import QFont


class _Colors:
    gray300 = "#d7dadc"
    gray500 = "#818384"
    gray600 = "#565758"
    gray700 = "#3a3a3c"
    gray800 = "#272729"
    gray900 = "#1a1a1b"
    gray1000 = "#121213"

    green400 = "#6aaa64"
    green500 = "#538d4e"

    yellow500 = "#c9b458"
    yellow600 = "#b59f3b"


class _Fonts:
    clearSans = "Clear Sans"
    nytKarnakCondensed = "NYTKarnakCondensed"


class _ThemeColors:
    absent = _Colors.gray700
    background = _Colors.gray1000
    border = _Colors.gray700
    correct = _Colors.green500
    foreground = _Colors.gray300
    present = _Colors.yellow600


class _ThemeFonts:
    @staticmethod
    def display(fontSize=-1):
        return QFont(_Fonts.nytKarnakCondensed, fontSize)

    @staticmethod
    def sans(fontSize=-1):
        return QFont(_Fonts.clearSans, fontSize)


class Theme:
    colors = _ThemeColors
    fonts = _ThemeFonts
