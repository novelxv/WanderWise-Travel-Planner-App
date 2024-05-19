from PyQt5.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

# Import kelas tombol yang baru Anda buat
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
        self.pixmap = QPixmap('img/bg/Homepage2.png')
        self.updateBackground()

        layout = QVBoxLayout()

        # Create spacer to push content to the center
        spacer_top = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_top)

        # Add button
        custom_button1 = OvalButton("See All Destination Here!", "#263B4E", 11)
        layout.addWidget(custom_button1, alignment=Qt.AlignCenter)
        custom_button1.clicked.connect(self.on_see_destination_click)

        custom_button2 = OvalButton("See Articles Here!", "#263B4E", 11)
        layout.addWidget(custom_button2, alignment=Qt.AlignCenter)
        custom_button2.clicked.connect(self.on_see_articles_click)

        # Create spacer to push content to the center
        spacer_bottom = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_bottom)

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
        self.updateBackground()

    def updateBackground(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(self.pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setPalette(palette)
