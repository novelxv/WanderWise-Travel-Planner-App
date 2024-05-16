from PyQt5 import QtWidgets, QtGui, QtCore

class OvalButton(QtWidgets.QPushButton):
    def __init__(self, text, background_color, border_radius, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(627, 179)  # Set fixed size for the button
        self.background_color = QtGui.QColor(background_color)
        self.border_radius = border_radius
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.background_color.name()};
                color: white;
                border: 3px dashed white;
                padding: 50px;  /* Add padding to separate border from background */
                font-size: 40px;
                font-weight: bold;
                border-radius: {self.border_radius}px;
            }}
            QPushButton:hover {{
                background-color: {self.background_color.darker(150).name()};
            }}
            QPushButton:pressed {{
                background-color: {self.background_color.lighter(150).name()};
            }}
        """)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    button = OvalButton("Click Me", "#263B4E", 11)
    button.show()
    sys.exit(app.exec_())
