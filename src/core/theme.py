from PyQt6.QtGui import QFont


class _Colors:
    gray500 = "#818384"
    gray600 = "#565758"
    gray700 = "#3a3a3c"
    gray800 = "#272729"
    gray900 = "#1a1a1b"
    gray1000 = "#121213"

    green400 = "#6aaa64"
    green500 = "#538d4e"

    white = "#ffffff"


class _Fonts:
    clearSans = "Clear Sans"
    nytKarnakCondensed = "NYTKarnakCondensed"


class _ThemeColors:
    background = _Colors.gray1000
    border = _Colors.gray700
    foreground = _Colors.white


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
