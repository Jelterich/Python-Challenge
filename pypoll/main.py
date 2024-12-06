# Import necessary libraries
import csv
import os

# Define file paths for input and output
current_dir = os.path.dirname(__file__)  # Get the directory of the current script
input_file = os.path.join(current_dir, "Resources", "election_data.csv")
output_file = os.path.join(current_dir, "analysis", "election_results.txt")

# Initialize tracking variables
total_votes = 0  # Total number of votes cast
candidate_votes = {}  # Dictionary to store each candidate's votes

# Read the election data file
try:
    with open(input_file, "r") as file:
        csvreader = csv.reader(file)

        # Skip the header row
        next(csvreader)

        # Loop through the rows in the CSV file
        for row in csvreader:
            candidate = row[2]  # Candidate name is in the third column
            total_votes += 1  # Count the vote

            # If the candidate is not yet in the dictionary, add them
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 0
            # Increment the candidate's vote count
            candidate_votes[candidate] += 1

    # Prepare results summary
    results_summary = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # Track the winner
    winning_candidate = ""
    winning_votes = 0

    # Calculate percentages and find the winner
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        results_summary += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        # Check if this candidate has the most votes so far
        if votes > winning_votes:
            winning_votes = votes
            winning_candidate = candidate

    # Append the winner to the results
    results_summary += (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    # Display the results in the terminal
    print(results_summary)

    # Save the results to a text file
    with open(output_file, "w") as txt_file:
        txt_file.write(results_summary)

except FileNotFoundError:
    print(f"Error: The input file {input_file} was not found. Please check the file path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
