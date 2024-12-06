# Python Challenge: PyBank & PyPoll
<p align="center"> <img src="https://img.shields.io/badge/Python-v3.8%2B-blue" alt="Python version"/> <img src="https://img.shields.io/badge/CSV-File%20Analysis-orange" alt="CSV Analysis"/> <img src="https://img.shields.io/github/languages/top/Python" alt="Python"/> <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status"/> </p>
Table of Contents
Project Overview
Features
Directory Structure
Installation & Usage
PyBank Details
PyPoll Details
Results Preview
Resources
Contributors
Project Overview
The Python Challenge consists of two real-world data analysis tasks:

PyBank: Analyze a company's financial data to determine key performance metrics like net profit, monthly changes, and maximum/minimum profits.
PyPoll: Automate the election voting analysis process, counting votes and determining the winner with percentages.
This project demonstrates Python's ability to process large datasets efficiently and generate actionable insights.

Features
Dynamic file paths for universal compatibility.
Read and process CSV files with Python's csv module.
Robust error handling for missing or incorrect data.
Clear and concise results exported to text files.
Beginner-friendly, well-commented code for learning and reusability.
Directory Structure
css
Copy code
python-challenge/
│
├── PyBank/
│   ├── Resources/
│   │   └── budget_data.csv
│   ├── analysis/
│   │   └── budget_analysis.txt
│   └── main.py
│
├── PyPoll/
│   ├── Resources/
│   │   └── election_data.csv
│   ├── analysis/
│   │   └── election_results.txt
│   └── main.py
│
└── README.md
Installation & Usage
Prerequisites
Python 3.8 or higher
Text editor (e.g., VS Code, PyCharm)
Terminal or Command Prompt
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/python-challenge.git
cd python-challenge
Navigate to either PyBank or PyPoll folders for analysis.

Run Scripts
Run PyBank:
bash
Copy code
cd PyBank
python main.py
Run PyPoll:
bash
Copy code
cd PyPoll
python main.py
View Results
PyBank: Check the analysis/budget_analysis.txt file.
PyPoll: Check the analysis/election_results.txt file.
PyBank Details
The PyBank script processes financial data from the budget_data.csv file to calculate:

Total months recorded.
Total profit/loss over the dataset.
Average monthly change in profits/losses.
Greatest increase in profits (date and amount).
Greatest decrease in profits (date and amount).
Example Output:

yaml
Copy code
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
PyPoll Details
The PyPoll script processes voting data from the election_data.csv file to calculate:

Total votes cast.
Percentage and total votes for each candidate.
The election winner based on popular vote.
Example Output:

markdown
Copy code
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
Results Preview
PyBank Result:
<img src="https://via.placeholder.com/800x200.png?text=PyBank+Results" alt="PyBank Results"/>
PyPoll Result:
<img src="https://via.placeholder.com/800x200.png?text=PyPoll+Results" alt="PyPoll Results"/>
Resources
The following resources were instrumental in completing this project:

W3Schools Python Tutorials - Clear explanations and Python basics.
YouTube - Tutorials for CSV handling and Python concepts.
ChatGPT - Assistance with coding logic, troubleshooting, and clarification.
Official Python Documentation - Comprehensive references for Python libraries.
Contributors
Jonas Elterich
Data Enthusiast 
GitHub: Jelterich
Acknowledgments:

Northwestern Data Bootcamp for providing the project framework.
Instructor/TA/Peers for feedback and guidance.
Notes
Feel free to contact me via GitHub for any issues, suggestions, or discussions about this project. Contributions are welcome!