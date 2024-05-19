import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SavingsWidget(QWidget):
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

    def format_rupiah(self, nominal):
        nominal_str = str(nominal)[::-1]
        ribuan = [nominal_str[i:i + 3] for i in range(0, len(nominal_str), 3)]
        hasil = '.'.join(ribuan)[::-1]
        return "Rp " + hasil


class ProgressBarWidget(QWidget):
    def __init__(self, now, goal):
        super().__init__()

        # Set up the main layout
        layout = QVBoxLayout()

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(int(now / goal * 100))  # Set initial value
        self.progress_bar.setTextVisible(False)  # Hide the percentage text

        # Set the stylesheet for the progress bar to match the desired design
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid black;
                border-radius: 8px;
                background: white;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #48C9B0;
                border-radius: 8px;
                margin: 0px;
            }
        """)

        # Add the progress bar to the layout
        layout.addWidget(self.progress_bar)

        # Set layout to the main window
        self.setLayout(layout)


class BudgetingWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        # Title
        title_label = QLabel("Your Budgeting")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)

        # Create a horizontal line
        line = QLabel()
        line.setFixedHeight(2)
        line.setStyleSheet("background-color: #000000;")

        # Savings and Target layouts
        savings_target_layout = QHBoxLayout()

        savings_widget = SavingsWidget("Your Savings", 100000000)
        target_widget = SavingsWidget("Your Target", 120000000)

        savings_target_layout.addWidget(savings_widget)
        savings_target_layout.addWidget(target_widget)

        edit_button_saving = QPushButton("✏ Edit")
        edit_button_saving.setFont(QFont("Arial", 12, QFont.Bold))
        edit_button_saving.setStyleSheet("background-color: #FFA500; color: black; border: 1px solid black; border-radius: 10px; padding: 5px;")
        edit_button_saving.setFixedSize(100, 30)

        edit_button_goals = QPushButton("✏ Edit")
        edit_button_goals.setFont(QFont("Arial", 12, QFont.Bold))
        edit_button_goals.setStyleSheet("background-color: #FFA500; color: black; border: 1px solid black; border-radius: 10px; padding: 5px;")
        edit_button_goals.setFixedSize(100, 30)

        edit_button = QHBoxLayout()
        edit_button.addWidget(edit_button_saving)
        edit_button.addWidget(edit_button_goals)

        # Goals Label
        goals_label = QLabel("Goals to reach your destination:\n20.000.000")
        goals_label.setFont(QFont("Arial", 24, QFont.Bold))
        goals_label.setAlignment(Qt.AlignCenter)

        # Progress Bar
        progress_bar_widget = ProgressBarWidget(100000000, 120000000)

        # Add widgets to the main layout
        main_layout.addWidget(title_label)
        main_layout.addWidget(line)
        main_layout.addLayout(savings_target_layout)
        main_layout.addLayout(edit_button)
        main_layout.addWidget(goals_label)
        main_layout.addWidget(progress_bar_widget)
        main_layout.addStretch()

        # Set background color for page2
        self.setStyleSheet("background-color: #FFF9ED;")

        # Set layout to the main window
        self.setLayout(main_layout)

        # Set window properties
        self.setWindowTitle("Your Budgeting")
        self.setGeometry(100, 100, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BudgetingWindow()
    window.show()
    sys.exit(app.exec_())
