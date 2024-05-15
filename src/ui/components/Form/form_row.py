from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont, QFontDatabase
from ui.components.Form.form_box import *
# from ui.utils import getFont

class Form(QWidget):
    def __init__(self, required, title, placeholder, parent=None):
        super().__init__(parent)
        self.setFixedWidth(parent.width())
        self.required = required
        
        # Question text field container
        self.text_input_container = QHBoxLayout()
        self.text_input_field = FormBox(placeholder, parent)
        # self.text_input_container.setContentsMargins(0,0,0,0)
        # self.text_input_container.addStretch()
        self.text_input_container.addWidget(self.text_input_field)
        # self.text_input_container.addStretch()
    

        # Question title container
        self.title_container = QHBoxLayout()
        self.title_container.setContentsMargins(0,0,0,0)
        title_text = QLabel()
        title_text.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title_text.setFixedSize(self.text_input_field.width(), int(0.04 * parent.height()))
        # title_text.setFont(QFont("Montserrat"))
        # title_text.setPixmap(getFont("Location"))

        title_text.setText(title)
        title_text.setObjectName('title_text')
        title_text.setStyleSheet("""
            #title_text { 
                color: black;
                margin: 0px;
            }
        """)

        # self.title_container.addStretch()
        self.title_container.addWidget(title_text)
        # self.title_container.addStretch()

        layout = QVBoxLayout()
        layout.addLayout(self.title_container)
        layout.addLayout(self.text_input_container)
        layout.setContentsMargins(0,0,0,2)
        layout.setSpacing(0)

        self.setFixedHeight(title_text.height() + self.text_input_field.height())
        self.setLayout(layout)
