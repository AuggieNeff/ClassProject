import csv

class VotingSystem:
    def __init__(self, filename: str):
        """
        Initialize the VotingSystem with a given filename.
        """
        self.filename = filename
        self.votes = {}  # Dictionary to store voter_id and candidate pairs
        self.load_votes()  # Load existing votes from the file

    def load_votes(self) -> None:
        """
        Load votes from the CSV file.
        """
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        voter_id = row[0]  # Voter's unique ID
                        candidate = row[1]  # Candidate's name
                        self.votes[voter_id] = candidate  # Store the vote in the dictionary
        except FileNotFoundError:
            # If the file doesn't exist, no votes have been cast yet
            pass

    def save_vote(self, voter_id: str, candidate: str) -> None:
        """
        Save a new vote to the CSV file.
        """
        self.votes[voter_id] = candidate  # Add/Update the vote in the dictionary
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate])  # Write the vote to the file

    def has_voted(self, voter_id: str) -> bool:
        """
        Check if the given voter ID has already voted.
        True if the voter has already voted, False otherwise.
        """
        return voter_id in self.votes

    def get_votes(self) -> dict:
        """
        Get the current vote counts for all candidates.
        """
        return self.votes

    def clear_votes(self) -> None:
        """
        Clear all votes and reset the CSV file.
        """
        self.votes.clear()  # Clear the votes in memory
        with open(self.filename, mode='w', newline='') as file:
            file.truncate()  # Clear the contents of the file
