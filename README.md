# FastBox Mystery Delivery System

## Overview
This Python script simulates a day of logistics operations for FastBox. It assigns packages to agents based on proximity, simulates delivery routes, and generates an efficiency report.

## Assumptions & Engineering Decisions
1. **Distance Metric**: Euclidean distance is used for all calculations.
2. **Assignment Logic**: Packages are assigned to the agent closest to the *warehouse* at the time of assignment. 
3. **Tie-Breaking**: If two agents are equidistant from a warehouse, the agent with the lexicographically smaller ID (e.g., A1 vs A2) is chosen.
4. **Routing Simulation**: Agents perform deliveries sequentially. After delivering a package, the agent remains at the destination location. This "chained" approach is more realistic and efficient than returning to base after every package.
5. **Efficiency**: Defined as `Total Distance / Packages Delivered`. A lower score indicates higher efficiency.

## How to Run
1. Ensure `data.json` is in the same directory.
2. Run the script:
   ```bash
   python main.py