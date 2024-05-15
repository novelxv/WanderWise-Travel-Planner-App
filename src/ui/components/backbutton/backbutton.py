from PyQt5 import QtWidgets, QtGui, QtCore

class BackButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setIcon(QtGui.QIcon("img/icons/back_arrow.png"))  # Set the icon
        self.setIconSize(QtCore.QSize(24, 24))  # Set icon size
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFA200;  /* Button color */
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #cc8200;  /* Darker color on hover */
            }
            QPushButton:pressed {
                background-color: #996100;  /* Even darker color when pressed */
            }
        """)
        self.setFixedSize(40, 40)  # Set the fixed size for the button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    button = BackButton()
    button.show()
    sys.exit(app.exec_())
