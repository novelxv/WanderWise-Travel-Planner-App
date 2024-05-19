from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class FormBox(QWidget):
    def __init__(self, placeholder, parent=None, width = 400):
        super().__init__(parent)
        self.setFixedSize(width, int(0.1 * parent.height()))
        
        self.field = QTextEdit()
        self.field.setPlaceholderText(placeholder)
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
                font-size: 20px;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.field)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.apply_shadow_effect()

    def apply_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(3, 3)
        self.field.setGraphicsEffect(shadow)
    
    def setText(self, text):
        self.field.setText(text)

    def getText(self):
        return self.field.toPlainText()