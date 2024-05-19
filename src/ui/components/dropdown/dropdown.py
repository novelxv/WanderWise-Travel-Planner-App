from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class DropDown(QtWidgets.QWidget):
    def __init__(self, option_type: str, button_text: str, parent=None):
        super().__init__(parent)
        self.option_type = option_type
        self.button_text = button_text
        self.selected_option = None
        self.initUI()

    def initUI(self):
        self.layout = QtWidgets.QHBoxLayout()
        
        # Dropdown button
        self.dropdown_button = QtWidgets.QPushButton(self.button_text)
        self.dropdown_button.setIcon(QtGui.QIcon("img/icons/triangle.png"))
        self.dropdown_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.dropdown_button.setFixedSize(760, 57)
        self.dropdown_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dropdown_button.setStyleSheet("""
            QPushButton {
                text-align: left; 
                border: 1px solid #D9DDEA;
                border-radius: 5px;
                padding: 5px 10px;
                background-color: white;
                font-size: 20px;
            }
            QPushButton::hover {
                background-color: #FFBE00;
            }
        """)
        self.dropdown_button.clicked.connect(self.show_menu)
        self.layout.addWidget(self.dropdown_button)

        # Options menu
        self.option_menu = QtWidgets.QMenu(self)
        self.option_menu.setStyleSheet("""
            QMenu {
                border: 1px solid #D9DDEA;
                border-radius: 5px;
                background-color: #FFF9ED;
                font-size: 20px;
            }
            QMenu::item {
                background-color: transparent;
                padding: 5px 20px;
            }
            QMenu::item:selected { 
                background-color: #FFBE00;
            }
        """)

        if self.option_type == "transport":
            options = ["Car", "Bus", "Taxi", "Walking", "Motorcycle", "Online Transport"]
        elif self.option_type == "category":
            options = ["Idea", "Plan", "Booked", "Done"]
        for option in options:
            self.option_menu.addAction(option).triggered.connect(lambda checked, option=option: self.set_button_text(option))

        self.setLayout(self.layout)
        self.apply_shadow_effect()
    
    def apply_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(3, 3)
        self.dropdown_button.setGraphicsEffect(shadow)

    def show_menu(self):
        button_rect = self.dropdown_button.rect()
        menu_size = self.option_menu.sizeHint()
        menu_width = menu_size.width()
        pos = self.mapToGlobal(QtCore.QPoint(button_rect.right() - menu_width, button_rect.bottom()))
        pos.setY(pos.y() + 10)  # Adjust the y-coordinate to lower the menu slightly
        pos.setX(pos.x() + 10)  # Adjust the x-coordinate to move the menu slightly to the left
        self.option_menu.exec_(pos)

    def set_button_text(self, text):
        self.dropdown_button.setText(text)
        self.selected_option = text