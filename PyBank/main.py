# Import required libraries
import csv  # For handling CSV files
import os   # For file path management

# File paths
# The paths are simplified for universal use
input_file = os.path.join("PyBank", "Resources", "budget_data.csv")
output_file = os.path.join("PyBank", "analysis", "budget_analysis.txt")


# Initialize variables for analysis
total_months = 0  # Counter for the total number of months
net_total = 0     # Net total of profit/losses
changes = []      # List to store changes in profit/loss
months = []       # List to store months corresponding to changes
greatest_increase = ["", float("-inf")]  # Track the month and value of the greatest increase
greatest_decrease = ["", float("inf")]   # Track the month and value of the greatest decrease
prev_profit = None  # Variable to hold the profit/loss of the previous row

# Read the CSV file
try:
    with open(input_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        
        # Read and skip the header row
        header = next(reader)
        
        # Loop through each row in the dataset
        for row in reader:
            # Parse the current month's profit/loss
            current_month = row[0]
            current_profit = int(row[1])
            
            # Add to the total months and net profit/loss
            total_months += 1
            net_total += current_profit

            # Calculate the change in profit/loss if not the first row
            if prev_profit is not None:
                change = current_profit - prev_profit
                changes.append(change)
                months.append(current_month)

                # Update greatest increase in profit
                if change > greatest_increase[1]:
                    greatest_increase = [current_month, change]

                # Update greatest decrease in profit
                if change < greatest_decrease[1]:
                    greatest_decrease = [current_month, change]

            # Update previous profit/loss for the next iteration
            prev_profit = current_profit

    # Calculate the average change in profit/loss
    average_change = sum(changes) / len(changes) if changes else 0

    # Format the analysis summary
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

    # Print the results to the terminal
    print(output)

    # Save the results to a text file
    with open(output_file, "w") as txt_file:
        txt_file.write(output)

except FileNotFoundError:
    print(f"Error: Could not find file at {input_file}. Ensure the file path is correct.")


