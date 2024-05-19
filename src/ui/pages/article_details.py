import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from src.ui.components.backbutton.backbutton import BackButton
from src.controller.artikel_controller import ArtikelController

class ArticleDetailWindow(QtWidgets.QWidget):
    def __init__(self, article_id, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.article_id = article_id
        self.stacked_widget = main_window.stacked_widget if main_window else None
        self.article_controller = ArtikelController()
        self.article = self.article_controller.get_artikel_by_id(article_id)

        # Main window size
        if main_window:
            main_window_width = main_window.width()
            main_window_height = main_window.height()
            self.setFixedWidth(main_window_width)
            self.setFixedHeight(main_window_height)

        self.setWindowTitle("Article Detail")

        # Layout setup
        self.layout = QtWidgets.QVBoxLayout(self)

        self.back_button = BackButton()
        self.back_button.clicked.connect(lambda: self.main_window.stacked_widget.setCurrentIndex(1))
        self.layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        # Scroll area setup
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout.addWidget(scroll_area)
        self.setStyleSheet("background-color: transparent; border:none;")  # Set background color

        scroll_content = QtWidgets.QWidget()
        scroll_area.setWidget(scroll_content)

        # Layout for scroll content
        self.scroll_layout = QtWidgets.QVBoxLayout(scroll_content)
        self.scroll_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Title label
        self.title_label = QtWidgets.QLabel(self.article.judul)
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
        self.author_label = QtWidgets.QLabel("By " + self.article.penulis)
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
        self.image_label.setPixmap(QtGui.QPixmap("img/images/article" + str(self.article.artikel_id) + ".png").scaled(1164, 324, QtCore.Qt.IgnoreAspectRatio))
        self.scroll_layout.addWidget(self.image_label)

        # Description label
        self.description_label = QtWidgets.QLabel(self.article.konten)
        self.description_label.setAlignment(QtCore.Qt.AlignCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setFixedWidth(1164)
        self.description_label.setStyleSheet("""
            QLabel {
                font: 22px;
                padding: 5px;
            }
        """)
        self.scroll_layout.addWidget(self.description_label)

        # Stretch to push content to the top
        self.scroll_layout.addStretch()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    article_detail_window = ArticleDetailWindow([], main_window)
    main_window.setCentralWidget(article_detail_window)
    main_window.show()
    sys.exit(app.exec_())
