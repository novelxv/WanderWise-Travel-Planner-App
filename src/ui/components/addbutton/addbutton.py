from PyQt5 import QtWidgets, QtGui, QtCore

class FloatingAddButton(QtWidgets.QPushButton):
    def __init__(self, parent, icon_path="img/icons/add.png", position=(10, 10)):
        super().__init__(parent)
        self.icon_path = icon_path
        self.position = position
        self.setIcon(QtGui.QIcon(self.icon_path))  # Set the icon
        self.setIconSize(QtCore.QSize(25, 25))  # Set the icon size

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: #FF5D00;  /* Button color */
                border-radius: 20px;  /* Make it circular */
                border: none;
            }}
            QPushButton:hover {{
                background-color: #cc4a00;  /* Darker color on hover */
            }}
            QPushButton:pressed {{
                background-color: #993800;  /* Even darker color when pressed */
            }}
        """)
        self.setFixedSize(40, 40)  # Set the fixed size for the button

    def setFloatingPosition(self):
        parent = self.parent()
        if parent:
            self.move(parent.width() - self.width() - self.position[0], parent.height() - self.height() - self.position[1])
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setFloatingPosition()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Window setup
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Floating Add Button Example")
    window.setGeometry(100, 100, 400, 300)

    # Floating add button
    add_button = FloatingAddButton(window, position=(10, 10))
    window.resizeEvent = lambda event: add_button.setFloatingPosition()

    window.show()
    sys.exit(app.exec_())