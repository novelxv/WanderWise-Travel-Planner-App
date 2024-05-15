import sys
import signal
from PyQt5.QtWidgets import QApplication
from src.ui.components.popup.pop_up_confirm import ConfirmationDialog

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ConfirmationDialog("Delete this itinerary?")
    res = dialog.run()
    if res == ConfirmationDialog.Accepted:
        print("Yes clicked")
    else:
        print("No clicked")
    sys.exit(app.exec_())
