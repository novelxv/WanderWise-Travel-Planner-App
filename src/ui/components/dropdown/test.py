import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QDialog
from dropdown import DropDown  # Replace 'your_module' with the module where you defined DropdownButton

class TestDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dropdown Button Test")
        self.setGeometry(100, 100, 400, 200)
        self.setLayout(QVBoxLayout())

        # Create DropdownButtons with different option types
        drop_down = DropDown(option_type="transport", button_text = "WOWOOW")
        # drop_down.initUI("Select Option")  # Pass button text here


        # Add DropdownButtons to the layout
        self.layout().addWidget(drop_down)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = TestDialog()
    dialog.show()
    sys.exit(app.exec_())
