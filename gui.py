from PyQt6 import QtCore, QtWidgets
from logic import VotingSystem

class Ui_VoteApp(object):
    def setupUi(self, VoteApp):
        """
        Set up the user interface of the voting application.
        """
        VoteApp.setObjectName("VoteApp")
        VoteApp.resize(300, 500)

        self.centralwidget = QtWidgets.QWidget(VoteApp)
        self.centralwidget.setObjectName("centralwidget")

        # Title label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 121, 41))
        self.label_title.setObjectName("label_title")

        # ID input label
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(30, 60, 60, 31))
        self.label_id.setObjectName("label_id")

        # ID input field
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(100, 60, 150, 31))
        self.lineEdit_id.setObjectName("lineEdit_id")

        # Radio buttons for candidates
        self.radioButton_john = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_john.setGeometry(QtCore.QRect(50, 100, 200, 31))
        self.radioButton_john.setObjectName("radioButton_john")

        self.radioButton_jane = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_jane.setGeometry(QtCore.QRect(50, 150, 200, 31))
        self.radioButton_jane.setObjectName("radioButton_jane")

        # Submit vote button
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(50, 200, 200, 31))
        self.pushButton_submit.setObjectName("pushButton_submit")

        # Display results button
        self.pushButton_results = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_results.setGeometry(QtCore.QRect(50, 250, 200, 31))
        self.pushButton_results.setObjectName("pushButton_results")

        # Clear data button
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(50, 300, 200, 31))
        self.pushButton_clear.setObjectName("pushButton_clear")

        # Message label
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(30, 350, 240, 100))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")

        VoteApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(VoteApp)
        QtCore.QMetaObject.connectSlotsByName(VoteApp)

        # Initialize the voting system
        self.voting_system = VotingSystem('votes.csv')

        # Connect buttons to functions
        self.pushButton_submit.clicked.connect(self.submit_vote)
        self.pushButton_results.clicked.connect(self.display_results)
        self.pushButton_clear.clicked.connect(self.clear_votes)

    def retranslateUi(self, VoteApp):
        _translate = QtCore.QCoreApplication.translate
        VoteApp.setWindowTitle(_translate("VoteApp", "Vote App"))
        self.label_title.setText(_translate("VoteApp", "Voting Application"))
        self.label_id.setText(_translate("VoteApp", "ID:"))
        self.radioButton_john.setText(_translate("VoteApp", "John"))
        self.radioButton_jane.setText(_translate("VoteApp", "Jane"))
        self.pushButton_submit.setText(_translate("VoteApp", "Submit Vote"))
        self.pushButton_results.setText(_translate("VoteApp", "Display Results"))
        self.pushButton_clear.setText(_translate("VoteApp", "Clear Data"))

    def submit_vote(self):
        """
        Validate the vote and submit it if valid.
        """
        voter_id = self.lineEdit_id.text()
        if len(voter_id) != 4 or not voter_id.isdigit():
            self.show_message("ID must be a 4-digit number", "red")
            return

        selected_candidate = None
        if self.radioButton_john.isChecked():
            selected_candidate = "John"
        elif self.radioButton_jane.isChecked():
            selected_candidate = "Jane"

        if not selected_candidate:
            self.show_message("No candidate selected", "red")
            return

        if self.voting_system.has_voted(voter_id):
            self.show_message("ID already voted", "red")
            return

        self.voting_system.save_vote(voter_id, selected_candidate)
        self.show_message("Vote submitted successfully", "green")

    def display_results(self):
        """
        Display the current vote count for each candidate.
        """
        votes = self.voting_system.get_votes()
        john_votes = sum(1 for vote in votes.values() if vote == "John")
        jane_votes = sum(1 for vote in votes.values() if vote == "Jane")
        result_message = f"John: {john_votes} votes\nJane: {jane_votes} votes"
        self.show_message(result_message, "blue")

    def clear_votes(self):
        """
        Clear all the votes in the system.
        """
        self.voting_system.clear_votes()
        self.show_message("All votes cleared", "green")

    def show_message(self, message, color):
        """
        Display a message in the specified color.
        """
        self.label_result.setText(message)
        self.label_result.setStyleSheet(f"color: {color}")
