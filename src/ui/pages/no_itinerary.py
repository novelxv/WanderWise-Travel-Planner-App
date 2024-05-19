import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from src.ui.components.backbutton.backbutton import BackButton

class ItinerariesPage(QWidget):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.stacked_widget = main_window.stacked_widget

        # Set up the main layout
        main_layout = QVBoxLayout()
        # main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(20)

        # Back Button
        back_button = BackButton()

        # Title
        self.title_label = QLabel("ALL ITINERARIES")
        self.title_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
                background: none;
                padding-top: 40px;
                padding-bottom: 40px;
            }
        """)

        # Container for title
        title_container = QVBoxLayout()
        title_container.addWidget(self.title_label)
        title_container.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # No Destination Label
        no_destination_label = QLabel("No Itinerary")
        no_destination_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                color: #000080;
                background: none;

            }
        """)
        no_destination_label.setAlignment(Qt.AlignCenter)

        # Subtext Label
        subtext_label = QLabel("Let's add some!")
        subtext_label.setFont(QFont("Arial", 18))
        subtext_label.setAlignment(Qt.AlignCenter)

        # Add Destination Button
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add An Itinerary")
        add_button.setFont(QFont("Arial", 10, QFont.Bold))
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #FFA500;
                color: black;
                border: 2px solid black;
                border-radius: 20px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FFC107;
            }
            QPushButton:pressed {
                background-color: #FF8C00;
            }
        """)
        add_button.setFixedSize(250, 60)
        button_layout.addWidget(add_button)
        button_layout.setAlignment(Qt.AlignCenter)

        # Add widgets to the main layout
        main_layout.addWidget(back_button)
        main_layout.addLayout(title_container)
        main_layout.addSpacing(200)
        main_layout.addWidget(no_destination_label)
        main_layout.addWidget(subtext_label)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        # Set layout to the main window
        self.setLayout(main_layout)

        # Set window properties
        self.setWindowTitle("All Itinerary")
        # self.setGeometry(100, 100, 800, 600)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ItinerariesPage()
#     window.show()
#     sys.exit(app.exec_())
