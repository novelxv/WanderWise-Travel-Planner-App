import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtGui import QPixmap

from src.ui.components.backbutton.backbutton import BackButton

class ArticleDetailWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Article Detail")
        self.setGeometry(20, 50, 1200, 900)  # Adjust window size to fit content

        # Central widget
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Back button setup
        self.back_button = BackButton()
        self.back_button.setFixedSize(60, 60)  # Increased size of the back button
        self.layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.back_button.move(50, 50)  # Move to the right

        # Scroll area setup
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout.addWidget(scroll_area)
        self.setStyleSheet("background-color: #FFF9ED; border:none;")  # Set background color

        scroll_content = QtWidgets.QWidget()
        scroll_area.setWidget(scroll_content)

        # Layout for scroll content
        self.scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        self.scroll_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Title label
        self.title_label = QtWidgets.QLabel("5 Things you need to bring for any travel plans")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setWordWrap(True) 
        self.title_label.setFixedWidth(950) 
        self.title_label.setStyleSheet("""
            QLabel {
                font: bold 48px;
                padding: 20px;
            }
        """)
        self.scroll_layout.addWidget(self.title_label, alignment=QtCore.Qt.AlignCenter)  # Align center

        # Author label
        self.author_label = QtWidgets.QLabel("By John Doe")
        self.author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label.setStyleSheet("""
            QLabel {
                font:  24px;
                padding: 10px;
            }
        """)
        self.scroll_layout.addWidget(self.author_label)

        # Image label
        self.image_label = QtWidgets.QLabel()
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setPixmap(QtGui.QPixmap("img/images/ex_article.png").scaled(1164, 324, QtCore.Qt.IgnoreAspectRatio))
        self.scroll_layout.addWidget(self.image_label)

        # Description label
        self.description_label = QtWidgets.QLabel("""What pops into your head when you hear the word "traveling"? Do you think to yourself, "going on vacation," "luxury hotels," "way too expensive," or even "absolutely not"? Traveling can be a very polarizing topic for many people. Some love it and will travel anywhere in the world no matter what, and some only want to take a week off at a resort in Fiji!""")
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setFixedWidth(1164)
        self.description_label.setStyleSheet("""
            QLabel {
                font: 32px;
                padding: 5px;
            }
        """)
        self.scroll_layout.addWidget(self.description_label)

        # Stretch to push content to the top
        self.scroll_layout.addStretch()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ArticleDetailWindow()
    window.show()
    sys.exit(app.exec_())
