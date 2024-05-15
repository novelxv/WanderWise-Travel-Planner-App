from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt

class FormBox(QWidget):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        self.setFixedSize(int(0.5*parent.width()), int(0.1 * parent.height()))
        
        self.field = QTextEdit()
        self.field.setPlaceholderText(placeholder)
        # self.field.setFont()
        self.field.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.field.setTextColor(Qt.black)
        self.field.setObjectName('field')
        self.field.setFixedSize(int(0.8 * self.width()), int(0.8 * self.height()))
        self.field.setStyleSheet("""
            #field { 
                padding: 10px; 
                border: 1px;
                border-radius: 5px;
                background-color: #FFFFFF;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.field)
        layout.setSpacing(0)
        self.setLayout(layout)