import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar, QFormLayout, QLineEdit, QDialog, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui.components.backbutton.backbutton import BackButton

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
    
    def update_amount(self, nominal):  
        rupiah = self.format_rupiah(nominal)
        self.amount_label.setText(rupiah)


class ProgressBarWidget(QWidget):
    def __init__(self, now, goal):
        super().__init__()

        # Set up the main layout
        layout = QVBoxLayout()

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        if goal < now:
            self.progress_bar.setValue(100)
        else:  
            self.progress_bar.setValue(int(now / goal * 100))
        # Set initial value
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

        # Create a label to show the percentage text
        self.percentage_label = QLabel(self)
        self.percentage_label.setAlignment(Qt.AlignCenter)
        self.update_percentage_label(now, goal)

        # Set the stylesheet for the percentage label
        self.percentage_label.setStyleSheet("""
            QLabel {
                font-family: Arial Bold;
                font-size: 24px;  
                color: black;
                background: transparent;
            }
        """)

        # Add the label on top of the progress bar using a QVBoxLayout
        overlay_layout = QVBoxLayout()
        overlay_layout.addWidget(self.percentage_label)
        overlay_layout.addWidget(self.progress_bar)
        layout.addLayout(overlay_layout)

        # Set layout to the main window
        self.setLayout(layout)

    def update_progress(self, now, goal):
        if goal < now:
            self.progress_bar.setValue(100)
        else:  
            self.progress_bar.setValue(int(now / goal * 100))

    def update_percentage_label(self, now, goal):
        if goal == 0:
            percentage = 100
        else:
            percentage = int(now / goal * 100)
        self.percentage_label.setText(f"{percentage}%")
        self.progress_bar.setValue(percentage)

class FormDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Nominal')
        self.setGeometry(100, 100, 300, 100)
        
        layout = QFormLayout()
        
        self.nominal_edit = QLineEdit()
        
        layout.addRow(QLabel('Nominal:'), self.nominal_edit)
        
        self.setStyleSheet("""
            QDialog {
                background-color: #FFE589;
            }
            QLabel {
                font-family: Arial Bold;
                font-size: 24px;
            }
            QLineEdit {
                background-color: #FFF9ED;
                font-family: Arial Bold;
                font-size: 24px;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
            }
        """)

        self.done_button = QPushButton('Done')
        self.done_button.setStyleSheet("background-color: #C36F0C")
        self.done_button.clicked.connect(self.validate_inputs)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.done_button)
        layout.addRow(button_layout)

        self.setLayout(layout)

    def validate_inputs(self):
        # Validate that the age field contains an integer
        nominal_text = self.nominal_edit.text()
        if not nominal_text.isdigit():
            QMessageBox.warning(self, 'Invalid Input', 'Nominal must be an integer.')
            return
        self.nominal_value = int(nominal_text)
        # If valid, accept the dialog
        self.accept()

class BudgetingWindow(QWidget):
    def __init__(self, destination, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.destination = destination
        self.stacked_widget = main_window.stacked_widget
        
        # Set up the main layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        # Back Button
        back_button = BackButton()

        # Title
        title_label = QLabel("Your Budgeting")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("margin-top: 50px")

        # Create a horizontal line
        line = QLabel()
        line.setFixedHeight(2)
        line.setStyleSheet("background-color: #000000")

        # Savings and Target layouts
        savings_target_layout = QHBoxLayout()

        self.savings_widget = SavingsWidget("Your Savings", destination.tabungan)
        self.target_widget = SavingsWidget("Your Target", destination.budget)

        savings_target_layout.addWidget(self.savings_widget)
        savings_target_layout.addWidget(self.target_widget)

        edit_button_saving = QPushButton("✏ Edit")
        edit_button_saving.setFont(QFont("Arial", 12, QFont.Bold))
        edit_button_saving.setStyleSheet("background-color: #FFA500; color: black; border: 1px solid black; border-radius: 10px; padding: 5px;")
        edit_button_saving.setFixedSize(100, 30)
        edit_button_saving.clicked.connect(self.show_edit_form_saving)

        edit_button_goals = QPushButton("✏ Edit")
        edit_button_goals.setFont(QFont("Arial", 12, QFont.Bold))
        edit_button_goals.setStyleSheet("background-color: #FFA500; color: black; border: 1px solid black; border-radius: 10px; padding: 5px;")
        edit_button_goals.setFixedSize(100, 30)
        edit_button_goals.clicked.connect(self.show_edit_form_goals)

        edit_button = QHBoxLayout()
        edit_button.addWidget(edit_button_saving)
        edit_button.addWidget(edit_button_goals)

        # Goals Label
        if destination.budget < destination.tabungan:
            goals = self.format_rupiah(0)
        else:
            goals = self.format_rupiah(destination.budget - destination.tabungan)
        self.goals_label = QLabel("Goals to reach your destination:\n" + goals)
        self.goals_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.goals_label.setAlignment(Qt.AlignCenter)
        self.goals_label.setStyleSheet("padding-top: 150px")

        # Progress Bar
        self.progress_bar_widget = ProgressBarWidget(destination.tabungan, destination.budget)

        # Add widgets to the main layout
        main_layout.addWidget(back_button)
        main_layout.addWidget(title_label)
        main_layout.addWidget(line)
        main_layout.addSpacing(50)
        main_layout.addLayout(savings_target_layout)
        main_layout.addLayout(edit_button)
        main_layout.addWidget(self.goals_label)
        main_layout.addWidget(self.progress_bar_widget)
        main_layout.addStretch()

        # Set background color for page2
        self.setStyleSheet("background-color: #FFF9ED;")

        # Set layout to the main window
        self.setLayout(main_layout)

        # Set window properties
        self.setWindowTitle("Your Budgeting")
        # self.setGeometry(100, 100, 1320, 1000)
    
    def format_rupiah(self, nominal):
        nominal_str = str(nominal)[::-1]
        ribuan = [nominal_str[i:i + 3] for i in range(0, len(nominal_str), 3)]
        hasil = '.'.join(ribuan)[::-1]
        return "Rp " + hasil
    
    def show_edit_form_saving(self):
        self.add_edit_form = FormDialog()
        self.add_edit_form.show()
        if self.add_edit_form.exec_() == QDialog.Accepted:
            self.destination.tabungan = self.add_edit_form.nominal_value
            self.update_ui()
    
    def show_edit_form_goals(self):
        self.add_edit_form = FormDialog()
        self.add_edit_form.show()
        if self.add_edit_form.exec_() == QDialog.Accepted:
            self.destination.budget = self.add_edit_form.nominal_value
            self.update_ui()

    def update_ui(self):
        self.savings_widget.update_amount(self.destination.tabungan)  # Update savings amount
        self.target_widget.update_amount(self.destination.budget)  # Update target amount
        if self.destination.budget < self.destination.tabungan:
            goals = self.format_rupiah(0)
        else:
            goals = self.format_rupiah(self.destination.budget - self.destination.tabungan)
        self.goals_label.setText("Goals to reach your destination:\n" + goals)  # Update goals label
        self.progress_bar_widget.update_progress(self.destination.tabungan, self.destination.budget)  # Update progress bar
        self.progress_bar_widget.update_percentage_label(self.destination.tabungan, self.destination.budget)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = BudgetingWindow()
#     window.show()
#     sys.exit(app.exec_())
