
# **Python Challenge: PyBank & PyPoll**

<p align="center">
  <img src="https://img.shields.io/badge/Python-v3.8%2B-blue" alt="Python version"/>
  <img src="https://img.shields.io/badge/CSV-File%20Analysis-orange" alt="CSV Analysis"/>
  <img src="https://img.shields.io/github/languages/top/Python" alt="Python"/>
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status"/>
</p>

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Directory Structure](#directory-structure)
4. [Installation & Usage](#installation--usage)
5. [PyBank Details](#pybank-details)
6. [PyPoll Details](#pypoll-details)
7. [Results Preview](#results-preview)
8. [Resources](#resources)
9. [Contributors](#contributors)

---

## **Project Overview**
The **Python Challenge** consists of two real-world data analysis tasks:
1. **PyBank**: Analyze a company's financial data to determine key performance metrics like net profit, monthly changes, and maximum/minimum profits.
2. **PyPoll**: Automate the election voting analysis process, counting votes and determining the winner with percentages.

This project demonstrates Python's ability to process large datasets efficiently and generate actionable insights.

---

## **Features**
- Dynamic file paths for universal compatibility.
- Read and process CSV files with Python's `csv` module.
- Robust error handling for missing or incorrect data.
- Clear and concise results exported to text files.
- Beginner-friendly, well-commented code for learning and reusability.

---

## **Directory Structure**
```
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
```

---

## **Installation & Usage**
### **Prerequisites**
- Python 3.8 or higher
- Text editor (e.g., VS Code, PyCharm)
- Terminal or Command Prompt

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/python-challenge.git
   cd python-challenge
   ```

2. Navigate to either `PyBank` or `PyPoll` folders for analysis.

### **Run Scripts**
- Run PyBank:
  ```bash
  cd PyBank
  python main.py
  ```
- Run PyPoll:
  ```bash
  cd PyPoll
  python main.py
  ```

### **View Results**
- **PyBank**: Check the `analysis/budget_analysis.txt` file.
- **PyPoll**: Check the `analysis/election_results.txt` file.

---

## **PyBank Details**
The **PyBank** script processes financial data from the `budget_data.csv` file to calculate:
- Total months recorded.
- Total profit/loss over the dataset.
- Average monthly change in profits/losses.
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).

**Example Output:**
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

---

## **PyPoll Details**
The **PyPoll** script processes voting data from the `election_data.csv` file to calculate:
- Total votes cast.
- Percentage and total votes for each candidate.
- The election winner based on popular vote.

**Example Output:**
```
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
```

---

## **Results Preview**

### **PyBank Result:**
![PyBank Results](https://via.placeholder.com/800x200.png?text=PyBank+Results)

### **PyPoll Result:**
![PyPoll Results](https://via.placeholder.com/800x200.png?text=PyPoll+Results)

---

## **Resources**
The following resources were instrumental in completing this project:
- [W3Schools Python Tutorials](https://www.w3schools.com/python/) - Clear explanations and Python basics.
- [YouTube](https://www.youtube.com/) - Tutorials for CSV handling and Python concepts.
- [ChatGPT](https://chat.openai.com/) - Assistance with coding logic, troubleshooting, and clarification.
- Official Python Documentation - Comprehensive references for Python libraries.

---

## **Contributors**
- **Your Name**  
  _Data Enthusiast | Python Developer_  
  GitHub: [your-username](https://github.com/your-username)  

**Acknowledgments**:
- **Northwestern Data Bootcamp** for providing the project framework.
- **Instructor/TA/Peers** for feedback and guidance.

---

### **Notes**
Feel free to contact me via GitHub for any issues, suggestions, or discussions about this project. Contributions are welcome!

---

### Fixes Made:
1. Proper section separation with blank lines and heading formatting.
2. Added bullet points, code blocks, and horizontal rules for better readability.
3. Fixed placeholders for images to display as visually distinct results sections.

Let me know if you need additional tweaks or enhancements!
