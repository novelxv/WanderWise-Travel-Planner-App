import sys
import signal
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

class ConfirmationDialog(QDialog):
    def __init__(self, labelText):
        super().__init__()
        self.labelText = labelText
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pop-up Confirmation Dialog")
        self.setGeometry(100, 100, 600, 450)  
        self.setFixedSize(600, 450)  

        # Background Image
        bgLabel = QLabel(self)
        pixmap = QPixmap('img/icons/pop_up_box.png')  
        bgLabel.setPixmap(pixmap)
        bgLabel.setFixedSize(800, 500)  
        bgLabel.move(0, 0) 

        # Label
        label = QLabel(self.labelText, self)
        label.setStyleSheet("font-size: 25px;") 
        label.move(160, 210) 

        # Yes Button
        yesButton = QPushButton(self)
        yesIcon = QPixmap('img/icons/yes_button.png') 
        yesButton.setIcon(QIcon(yesIcon))
        yesButton.setIconSize(QSize(300, 100))  
        yesButton.setFixedSize(300, 100)
        yesButton.setStyleSheet("background-color: transparent; border: none;")  
        yesButton.move(-7, 340)  
        yesButton.clicked.connect(self.accept)

        # No Button
        noButton = QPushButton(self)
        noIcon = QPixmap('img/icons/no_button.png')  
        noButton.setIcon(QIcon(noIcon))
        noButton.setIconSize(QSize(300, 100)) 
        noButton.setFixedSize(300, 100)
        noButton.setStyleSheet("background-color: transparent; border: none;")  
        noButton.move(260, 340)  
        noButton.clicked.connect(self.reject)

    def run(self):
        return self.exec_()

signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ConfirmationDialog("Delete this itinerary?")
    res = dialog.run()
    if res == QDialog.Accepted:
        print("Yes clicked")
    else:
        print("No clicked")
    sys.exit(app.exec_())