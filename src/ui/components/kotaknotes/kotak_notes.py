from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class NotesWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setMinimumWidth(300)
        
        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.main_layout)
        
        # Container for Notes and lines
        self.notes_container = QtWidgets.QWidget()
        self.notes_layout = QtWidgets.QVBoxLayout()
        self.notes_layout.setContentsMargins(10, 10, 10, 10)
        self.notes_layout.setSpacing(10)
        self.notes_container.setLayout(self.notes_layout)
        
        # Note label
        self.note_label = QtWidgets.QLabel("Notes:")
        self.note_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.note_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: black;
            }
        """)
        self.notes_layout.addWidget(self.note_label)
        
        # Add five lines
        for _ in range(5):
            line = QtWidgets.QWidget()
            line.setFixedHeight(2)
            line.setStyleSheet("background-color: black;")
            self.notes_layout.addWidget(line)
        
        self.main_layout.addWidget(self.notes_container)
        
        # Text area
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setPlaceholderText("Enter your notes here...")
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                border: none;
                font-size: 14px;
                margin-top: 5px;
            }
        """)
        self.text_edit.textChanged.connect(self.adjustSizeBasedOnText)
        self.main_layout.addWidget(self.text_edit)
        
        # Set stylesheet for the widget
        self.setStyleSheet("""
            QWidget {
                background-color: #D3D3D3;
                border-radius: 11px;
                padding: 10px;
            }
        """)

    def adjustSizeBasedOnText(self):
        document = self.text_edit.document()
        document.setTextWidth(self.text_edit.viewport().width())
        text_height = document.size().height()
        new_height = text_height + 160  # Additional space for margins, label, and lines
        self.setMinimumHeight(new_height)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    notes_widget = NotesWidget()
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(notes_widget)
    main_window.setGeometry(796, 549, 499, 292)
    main_window.setWindowTitle("Notes Widget Example")
    main_window.show()
    sys.exit(app.exec_())
