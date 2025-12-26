import json
import os
import random
import csv
from pathlib import Path

funding_sources = [
    "Government Grant",
    "Private Sponsor",
    "International Aid",
    "Local NGO Fund",
    "Corporate Sponsorship",
    "Community Fund",
    "University Research Fund",
    "State Development Grant",
    "Environmental Grant",
    "Philanthropic Donation",
    "Crowdfunding",
    "Federal Assistance",
    "Development Bank Loan",
    "Research Institution Funding",
    "Social Impact Investment",
    "Green Energy Fund",
    "International Organization Grant",
    "Local Business Support",
    "Non-profit Organization Grant",
    "Municipal Fund",
    "Public-Private Partnership (PPP)",
    "National Foundation Fund",
    "Educational Sponsorship",
    "Technology Innovation Fund",
    "Infrastructure Bond",
    "Taxpayer Contribution",
    "Venture Capital Fund",
    "Impact Investment Fund",
    "Urban Renewal Fund",
    "Cultural Heritage Grant"
]

# Read all project names from ground truth labels
def extract_project_names():
    """Extract distinct project names from all ground truth label files."""
    project_names = set()
    ground_truth_dir = Path(__file__).parent / "ground_truth_labels"
    
    for file_path in ground_truth_dir.glob("*.txt"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    # Project names are the keys of the JSON object
                    project_names.update(data.keys())
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
            continue
    
    return sorted(list(project_names))

# Generate synthetic table
def generate_synthetic_table(k=500):
    """Generate a synthetic table with k tuples."""
    # Extract distinct project names
    distinct_project_names = extract_project_names()
    num_distinct = len(distinct_project_names)
    
    print(f"Found {num_distinct} distinct project names")
    
    # Generate table data
    table = []
    
    # First, ensure all distinct project names are covered
    for i, project_name in enumerate(distinct_project_names):
        funding_id = i + 1
        funding_source = random.choice(funding_sources)
        amount = random.randint(10, 100) * 1000
        table.append({
            "Funding ID": funding_id,
            "Project Name": project_name,
            "Funding Source": funding_source,
            "Amount": amount
        })
    
    # Fill remaining entries with random project names
    remaining = k - num_distinct
    # Generate distinct random IDs from 1-500 for project names
    project_ids = random.sample(range(1, 501), remaining)
    for i in range(remaining):
        funding_id = num_distinct + i + 1
        # Generate project name in format "project_ID" with distinct random ID
        project_name = f"project_{project_ids[i]}"
        funding_source = random.choice(funding_sources)
        amount = random.randint(10, 100) * 1000
        table.append({
            "Funding ID": funding_id,
            "Project Name": project_name,
            "Funding Source": funding_source,
            "Amount": amount
        })
    
    return table

# Generate and print the table
if __name__ == "__main__":
    table = generate_synthetic_table(k=500)
    
    # Save table to CSV file
    output_dir = Path(__file__).parent / "query_dataset_table"
    output_dir.mkdir(exist_ok=True)
    csv_file = output_dir / "funding_table.csv"
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        if table:
            writer = csv.DictWriter(f, fieldnames=table[0].keys())
            writer.writeheader()
            writer.writerows(table)
    
    print(f"\nTable saved to: {csv_file}")
    print(f"Total tuples: {len(table)}")
    
    # Print table header
    print("\n" + "=" * 100)
    print(f"{'Funding ID':<12} {'Project Name':<50} {'Funding Source':<35} {'Amount':<10}")
    print("=" * 100)
    
    # Print first 10 rows as preview
    for row in table[:10]:
        print(f"{row['Funding ID']:<12} {row['Project Name']:<50} {row['Funding Source']:<35} {row['Amount']:<10}")
    
    if len(table) > 10:
        print(f"... ({len(table) - 10} more rows)")
    
    print("=" * 100)