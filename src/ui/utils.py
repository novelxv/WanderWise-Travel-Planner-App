from PyQt5 import QtGui
import io
import os
import shutil
from PIL import Image, ImageCms
from PyQt5.QtGui import QFontDatabase

from PyQt5.QtGui import QFontDatabase, QFont
def getFont(font_family, font_size, font_weight="Regular"):
    """Get font based on font family, size, and weight"""
    # Construct the font file path based on the font family and weight
    font_path = f"img/fonts/{font_family}/{font_family}-{font_weight}.ttf"
    print(font_path)
    # Add the font to the application font database
    font_id = QFontDatabase.addApplicationFont(font_path)

    # Get the font family name
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    if font_families:
        font_family_name = font_families[0]
    else:
        # Handle error loading font
        print(f"Error loading font: {font_path}")
        return None

    # Create a QFont object using the font family
    font = QFont(font_family_name)

    # Set the font size
    font.setPointSize(font_size)

    # Set the font weight
    if font_weight.lower() == "bold":
        font.setWeight(QFont.Bold)
    else:
        font.setWeight(QFont.Normal)

    return font
