import json
import math
import csv

# --- 1. JSON Parsing ---
def load_data(filepath):
    """Reads and parses the JSON file manually using standard library."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None

# --- 2. Distance Calculation (Euclidean) ---
def calculate_distance(point1, point2):
    """Calculates Euclidean distance between two [x, y] points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# --- 3. Agent-Package Assignment (FIXED) ---
def assign_packages(data):
    """
    Assigns each package to the nearest agent based on distance 
    from agent's INITIAL location to the package's warehouse.
    
    FIX: We use agents' initial positions for ALL assignments.
    Tie-breaker: Lexicographically smallest ID (e.g., A1 before A2).
    """
    agents = data['agents']  # Initial positions
    warehouses = data['warehouses']
    packages = data['packages']
    
    assignments = {agent_id: [] for agent_id in agents}

    for pkg in packages:
        wh_loc = warehouses[pkg['warehouse']]
        min_dist = float('inf')
        best_agent = None
        
        for agent_id, agent_loc in agents.items():  # Always use initial loc
            dist = calculate_distance(agent_loc, wh_loc)
            
            # Strictly less than OR (equal distance AND smaller ID)
            if dist < min_dist or (dist == min_dist and (best_agent is None or agent_id < best_agent)):
                min_dist = dist
                best_agent = agent_id
                
        if best_agent:
            assignments[best_agent].append(pkg)
            
    return assignments

# --- 4. Simulation & Report Generation (FIXED) ---
def simulate_and_report(data, assignments):
    """
    Simulates delivery. 
    IMPORTANT: Agent starts from INITIAL position for EVERY package.
    Route: Initial Pos -> Warehouse -> Destination -> (Implicitly back to base for next pkg)
    """
    agents = data['agents']
    warehouses = data['warehouses']
    
    report = {}
    for agent_id in agents:
        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "efficiency": 0.0
        }
        
    for agent_id, pkg_list in assignments.items():
        if not pkg_list:
            continue
            
        total_dist = 0.0
        count = 0
        initial_pos = agents[agent_id]  # Constant starting point
        
        for pkg in pkg_list:
            wh_loc = warehouses[pkg['warehouse']]
            dest_loc = pkg['destination']
            
            # Leg 1: Initial Pos -> Warehouse
            d1 = calculate_distance(initial_pos, wh_loc)
            total_dist += d1
            
            # Leg 2: Warehouse -> Destination
            d2 = calculate_distance(wh_loc, dest_loc)
            total_dist += d2
            
            count += 1
            
        # Efficiency: Total Distance / Packages Delivered
        efficiency = total_dist / count if count > 0 else 0.0
        
        report[agent_id] = {
            "packages_delivered": count,
            "total_distance": round(total_dist, 2),
            "efficiency": round(efficiency, 2)
        }
        
    # Determine Best Agent (Lowest Efficiency Score)
    best_agent = None
    min_eff = float('inf')
    
    for aid in sorted(report.keys()):
        stats = report[aid]
        if stats['packages_delivered'] > 0:
            if stats['efficiency'] < min_eff:
                min_eff = stats['efficiency']
                best_agent = aid
                
    report["best_agent"] = best_agent
    return report

# --- Bonus: CSV Export ---
def export_csv(report, filename="top_performer.csv"):
    """Exports the best agent's stats to CSV."""
    best = report.get("best_agent")
    if best:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Agent_ID", "Packages_Delivered", "Total_Distance", "Efficiency"])
            writer.writerow([best, report[best]['packages_delivered'], 
                           report[best]['total_distance'], report[best]['efficiency']])
        print(f"Bonus: Top performer exported to {filename}")

# --- Main Execution ---
def main():
    data = load_data('data.json')
    if not data:
        return

    assignments = assign_packages(data)
    final_report = simulate_and_report(data, assignments)
    
    with open('report.json', 'w') as f:
        json.dump(final_report, f, indent=2)
        
    print("Simulation Complete. Report saved to report.json")
    print(json.dumps(final_report, indent=2))
    
    export_csv(final_report)

if __name__ == "__main__":
    main()