import os
import sys
import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont, QFontDatabase

# CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
CURRENT_DIRECTORY = os.getcwd()
# def addText(pixmap, w, h, name):
#     painter = QtGui.QPainter(pixmap)
#     font = QtGui.QFont("Montserrat_Alternates")
#     font.setPointSize(36)
#     position = QtCore.QRect(0, 0, w, h)
#     painter.setFont(font)
#     painter.drawText(position, QtCore.Qt.AlignCenter, name)
#     painter.end()
#     return pixmap

# def create_pixmap(text):
#     pixmap = QtGui.QPixmap(512 * QtCore.QSize(1, 1))
#     pixmap.fill(QtCore.Qt.white)
#     return addText(pixmap, 512, 512, text)

def load_font(font_path):
    list = [font for font in os.listdir(font_path) if font.endswith(".ttf")]
    if list:
        for font in list:
            QFontDatabase.addApplicationFont(os.path.join(font_path, font))

def getFont(text):
    font_path = os.path.join(CURRENT_DIRECTORY, "assets", "fonts", "Montserrat_Alternates", "OFL.txt")

    print(font_path)
    with open(font_path, "r") as r:
        result = r.read()

    pattern = re.compile("\'(.*)\'")
    fonts_list = pattern.findall(result)

    list = [font for font in os.listdir(font_path) if font.endswith(".ttf")]
    if list:
        for font in list:
            QFontDatabase.addApplicationFont(os.path.join(font_path, font))

    if fonts_list:

    # id = QtGui.QFontDatabase.addApplicationFont(font_path)
    # if QtGui.QFontDatabase.applicationFontFamilies(id) == -1:
    #     print("problem loading font")
    #     sys.exit(-1)
    # return create_pixmap(text)