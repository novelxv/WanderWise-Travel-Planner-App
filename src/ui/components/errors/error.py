from PyQt5 import QtWidgets, QtGui, QtCore
class ErrorPopup(QtWidgets.QDialog):
    def __init__(self, error_message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setFixedSize(300, 150)  # Set fixed size for the popup
        self.setStyleSheet("""
            QDialog {
                background-color: #FFF9ED;
            }
            QLabel {
                color: black;
                font-size: 16px;
                font-weight: bold;
                text-align: center;
            }
            QPushButton {
                background-color: #C5E5C0;
                color: black;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 15px; 
            }
            QPushButton:hover {
                background-color: #96B791;
            }
            QPushButton:pressed {
                background-color: #FFBE00;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout()

        self.error_label = QtWidgets.QLabel(error_message)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)  # Align text to center
        self.error_label.setWordWrap(True)  # Enable word wrapping for long text
        layout.addWidget(self.error_label)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        layout.addItem(spacer_item)

        button_layout = QtWidgets.QHBoxLayout()

        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        button_layout.addWidget(self.ok_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    error_message = "You must enter 1000 characters 10 dreams and 1 ice cream."
    popup = ErrorPopup(error_message)
    popup.exec_()
    sys.exit(app.exec_())
