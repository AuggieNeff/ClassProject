import sys
from PyQt6 import QtWidgets
from gui import Ui_VoteApp

def main():
    app = QtWidgets.QApplication(sys.argv)
    VoteApp = QtWidgets.QMainWindow()
    ui = Ui_VoteApp()
    ui.setupUi(VoteApp)
    VoteApp.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

