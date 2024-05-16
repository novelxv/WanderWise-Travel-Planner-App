from PyQt5 import QtWidgets, QtGui, QtCore

class OvalButton(QtWidgets.QPushButton):
    def __init__(self, text, color, border_radius, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(200, 100)  # Set fixed size for the button
        self.color = QtGui.QColor(color)
        self.border_radius = border_radius
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color.name()};
                color: black;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                border-radius: {self.border_radius}px; 
            }}
            QPushButton:hover {{
                background-color: {self.color.darker(150).name()};
            }}
            QPushButton:pressed {{
                background-color: {self.color.lighter(150).name()};
            }}
        """)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

class OvalButtonIcon(QtWidgets.QPushButton):
    def __init__(self, text, icon, color, border_radius, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(200, 80)  # Set fixed size for the button
        self.color = QtGui.QColor(color)
        self.border_radius = border_radius
        self.setIcon(QtGui.QIcon(icon))
        self.setIconSize(QtCore.QSize(40,40))  # Set icon size
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.color.name()};
                color: black;
                border: 5px solid;
                padding-left: 20px;  /* Adjust padding for icon */
                padding-right: 20px;
                font-size: 20px;
                font-weight: bold;
                border-radius: {self.border_radius}px;
            }}
            QPushButton:hover {{
                background-color: {self.color.darker(150).name()};
            }}
            QPushButton:pressed {{
                background-color: {self.color.darker(200).name()};
            }}
        """)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    button = OvalButtonIcon("Edit", "img/icons/Pencil.png","#FF5D00", 20)

    # button = OvalButtonIcon("TEST", "img/icons/trash-can.png", "#C5E5C0", 20)
    button.show()
    sys.exit(app.exec_())
