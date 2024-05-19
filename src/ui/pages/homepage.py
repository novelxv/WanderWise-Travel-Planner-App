from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QApplication, QSpacerItem, QPushButton, QSizePolicy
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

# Import the OvalButton class
from src.ui.components.hellobutton.hellobutton import OvalButton
from src.controller.destinasi_controller import DestinasiController

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI(parent)

    def initUI(self, parent):
        self.setWindowTitle('Home Page')
        self.setGeometry(300, 100, 1500, 600)  # Adjust window position and size
        self.stacked_widget = parent.stacked_widget
        self.last_page_idx = parent.last_page_idx
        
        # Set background image
        self.pixmap = QPixmap('img/icons/HomePage.png')

        layout = QVBoxLayout()
        app = QApplication.instance()
        # Create QLabel for background image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.pixmap)
        self.background_label.setGeometry(int((self.width() - self.pixmap.width()) / 2), int((self.height() - self.pixmap.height()) / 2), self.pixmap.width(), self.pixmap.height())
        self.background_label.setScaledContents(True)

        # Add spacer to move the buttons up
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Add buttons
        custom_button1 = OvalButton("See All Destination Here!", "#263B4E", 11)
        layout.addWidget(custom_button1, alignment=Qt.AlignCenter)
        custom_button1.clicked.connect(self.on_see_destination_click)

        custom_button2 = OvalButton("See Articles Here!", "#263B4E", 11)
        layout.addWidget(custom_button2, alignment=Qt.AlignCenter)
        custom_button2.clicked.connect(self.on_see_articles_click)

        # Add bottom spacer to create a gap
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def on_see_articles_click(self):
        self.stacked_widget.setCurrentIndex(1)

    def on_see_destination_click(self):
        destinasi = DestinasiController()
        n_dest = len(destinasi.get_all_destinasi())
        print(n_dest)
        if n_dest == 0:
            self.stacked_widget.setCurrentIndex(2)
        else:
            self.stacked_widget.setCurrentIndex(3)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.background_label.setGeometry(int((self.width() - self.pixmap.width()) / 2), int((self.height() - self.pixmap.height()) / 2), self.pixmap.width(), self.pixmap.height())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())
