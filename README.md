# FastBox Mystery Delivery System

## Overview
This Python script simulates a day of logistics operations for FastBox, a fictional delivery company. It parses input data, assigns packages to the nearest delivery agents based on Euclidean distance, simulates the delivery routes, and generates an efficiency report to identify the best-performing agent.

## Project Structure
``text
fastbox_delivery/ 
├── main.py              # Main Python script containing all logic
├── data.json            # Input data (warehouses, agents, packages)
├── report.json          # Generated JSON output report
── top_performer.csv    # CSV export of the best agent (Bonus Feature)
└── README.md            # Project documentation

##Assumptions & Engineering Decisions

As per the assignment guidelines, the following assumptions were made for ambiguous scenarios:
Distance Metric: Standard Euclidean distance is used for all calculations: √((x₂ - x₁)² + (y₂ - y₁)²).
Agent Assignment: Packages are assigned to the agent closest to the package's warehouse. The distance is calculated using the agent's initial starting position.
Tie-Breaking: If multiple agents are equidistant from a warehouse, the agent with the lexicographically smallest ID (e.g., A1 over A2) is selected to ensure deterministic results.
Routing Simulation: For each assigned package, the agent travels from their initial starting position to the warehouse (pickup), and then from the warehouse to the destination (delivery).
Efficiency Calculation: Efficiency is defined as Total Distance Traveled / Packages Delivered. A lower efficiency score indicates a more efficient agent (less distance traveled per package).
Best Agent Selection: The agent with the lowest efficiency score is declared the "best agent". Agents with 0 deliveries are excluded from this calculation to prevent division-by-zero errors.


### Execution Steps
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd fastbox_delivery
3. Run the main script:
    ```bash
     python3 main.py
 4. The script will print the final report to the console and automatically generate report.json and top_performer.csv in the same directory.
  
##Output Format

report.json

The script generates a JSON file containing the performance metrics for each agent and identifies the best agent.
Example output:

{
  "A1": {
    "packages_delivered": 2,
    "total_distance": 121.21,
    "efficiency": 60.61
  },
  "A2": {
    "packages_delivered": 2,
    "total_distance": 79.21,
    "efficiency": 39.61
  },
  "A3": {
    "packages_delivered": 1,
    "total_distance": 14.14,
    "efficiency": 14.14
  },
  "best_agent": "A3"
}

## top_performer.csv

A CSV file containing a summary of the best agent's performance with the following columns:
Agent_ID
Packages_Delivered
Total_Distance
Efficiency

##Bonus Features Implemented

CSV Export: Automatically exports the top performer's statistics to a CSV file for external analysis.
Robust Error Handling: Includes try-except blocks to gracefully handle missing files or malformed JSON inputs.
Zero-Delivery Handling: Safely handles edge cases where an agent might not be assigned any packages, preventing ZeroDivisionError.

##Testing

The code has been tested with the provided data.json and custom test cases to ensure:
Total packages delivered always matches the total packages in the input.
No division-by-zero errors occur.
Tie-breaking logic works correctly.
Different JSON inputs produce valid outputs.

##Code Quality

Modular Design: Functions are separated by responsibility (parsing, distance calculation, assignment, simulation)
Documentation: All functions include docstrings explaining their purpose
Comments: Key logic sections are commented for clarity
No External Dependencies: Uses only Python standard library modules

##Author

Developed as part of the Python Developer hiring assessment for Nexgensis Technologies Pvt. Ltd.

##License

This project is created for assessment purposes.
