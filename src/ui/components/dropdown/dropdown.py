from PyQt5 import QtWidgets, QtGui, QtCore
# from ui.utils import getFont

# dropdown input button. To change currently showed text use the following:
# drop_down = DropDown(option_type="transport", button_text = "Select Option")
class DropDown(QtWidgets.QWidget):
    def __init__(self, option_type: str, button_text: str, parent=None):
        super().__init__(parent)
        self.option_type = option_type
        self.button_text = button_text
        self.initUI()

    def initUI(self):
        self.layout = QtWidgets.QHBoxLayout()
        
        # Dropdown button
        self.dropdown_button = QtWidgets.QPushButton()
        self.dropdown_button.setCursor(QtCore.Qt.PointingHandCursor)
        # self.option_menu.setFont(getFont("Regular", 10))
        self.dropdown_button.setStyleSheet("""
            QPushButton {
                text-align: left; 
                box-shadow: 3px 3px 5px rgba(0, 0.5, 0, 0);
            }
        """)
        self.dropdown_button.setIcon(QtGui.QIcon("/img/icons/Dropdown.png")) 
        self.dropdown_button.setIconSize(QtCore.QSize(24, 24))
        self.dropdown_button.clicked.connect(self.show_menu)
        self.dropdown_button.setText(self.button_text)
        self.layout.addWidget(self.dropdown_button)

        # Options menu
        self.option_menu = QtWidgets.QMenu(self)
        self.option_menu.setStyleSheet("""
            QMenu {
                border: 1px solid #D9DDEA;
                box-shadow: 3px 3px 5px rgba(0, 0.5, 0, 0);
                border-radius: 5px;
                background-color: #FFF9ED;
            }
            QMenu::item {
                border-radius: 15px;
                background-color: #FFF9ED;
                color:black;
                padding: 5px 16px 5px 12px;
            }
            QMenu::item:hover, QMenu::item:selected { 
                background-color: #FFBE00;
                color: black; }
        """)
        self.option_menu.setObjectName("option_menu")

        if self.option_type == "transport":
            self.option_menu.addAction("Car").triggered.connect(lambda: self.set_button_text("Car"))
            self.option_menu.addAction("Bus").triggered.connect(lambda: self.set_button_text("Bus"))
            self.option_menu.addAction("Taxi").triggered.connect(lambda: self.set_button_text("Taxi"))
            self.option_menu.addAction("Walking").triggered.connect(lambda: self.set_button_text("Walking"))
            self.option_menu.addAction("Motorcycle").triggered.connect(lambda: self.set_button_text("Motorcycle"))
            self.option_menu.addAction("Online Transport").triggered.connect(lambda: self.set_button_text("Online Transport"))
        elif self.option_type == "category":
            self.option_menu.addAction("Idea").triggered.connect(lambda: self.set_button_text("Idea"))
            self.option_menu.addAction("Plan").triggered.connect(lambda: self.set_button_text("Plan"))
            self.option_menu.addAction("Booked").triggered.connect(lambda: self.set_button_text("Booked"))
            self.option_menu.addAction("Done").triggered.connect(lambda: self.set_button_text("Done"))

        self.setLayout(self.layout)


    def show_menu(self):
        button_rect = self.dropdown_button.rect()
        menu_size = self.option_menu.sizeHint()
        menu_width = menu_size.width()
        menu_height = menu_size.height()
        pos = self.mapToGlobal(QtCore.QPoint(button_rect.right() - menu_width, button_rect.bottom()))
        pos.setY(pos.y() + 80)  # Adjust the y-coordinate to lower the menu slightly
        pos.setX(pos.x() + 10)  # Adjust the x-coordinate to move the menu slightly to the left
        self.option_menu.exec_(pos)

        
    def set_button_text(self, text):
        self.dropdown_button.setText(text)