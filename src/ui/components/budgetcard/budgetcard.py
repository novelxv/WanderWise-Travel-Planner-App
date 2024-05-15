import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SavingsWindow(QWidget):
    def __init__(self, word, nominal):
        super().__init__()

        # Set up the main layout
        layout = QVBoxLayout()
        # Set spacing to zero
        layout.setSpacing(0)

        # Create the "Your Savings" label
        self.savings_label = QLabel(word, self)
        self.savings_label.setFont(QFont("Arial", 20))
        self.savings_label.setStyleSheet("background-color: #C36F0C; color: black; padding: 10px; margin: 0; border: 2px solid black; border-top-left-radius: 10px; border-top-right-radius: 10px;")
        self.savings_label.setAlignment(Qt.AlignCenter)

        rupiah = self.format_rupiah(nominal)

        # Create the amount label
        self.amount_label = QLabel(rupiah, self)
        self.amount_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.amount_label.setStyleSheet("background-color: #FFE589; color: black; padding: 10px; margin: 0; "
                                        "border-left: 2px solid black; border-right: 2px solid black; border-bottom: 2px solid black;"
                                        "border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;")
        self.amount_label.setAlignment(Qt.AlignCenter)

        # Add widgets to layout
        layout.addWidget(self.savings_label)
        layout.addWidget(self.amount_label)

        # Set layout to the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Savings")
        self.setGeometry(100, 100, 300, 150)

    def format_rupiah(self, nominal):
        nominal_str = str(nominal)[::-1]
        ribuan = [nominal_str[i:i + 3] for i in range(0, len(nominal_str), 3)]
        hasil = '.'.join(ribuan)[::-1]
        return "Rp " + hasil

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SavingsWindow("Your Savings", 100000000)
    window.show()
    sys.exit(app.exec_())
