code = """import sqlite3
import pandas as pd
import json
import re

# Load Funding data
funding_data = pd.read_sql_query("SELECT * FROM Funding", sqlite3.connect('funding_database.db'))

# Load Civic Docs
with open(locals()['var_function-call-1716930988388569207'], 'r') as f:
    civic_docs = json.load(f)

# Identify Disaster Projects in Funding
# Keywords from hints: FEMA, CalOES, CalJPIA
def is_disaster_project(name):
    keywords = ["FEMA", "CalOES", "CalJPIA"]
    return any(k in name for k in keywords)

disaster_funding = funding_data[funding_data['Project_Name'].apply(is_disaster_project)].copy()

# Extract base names for linking
def get_base_name(name):
    # Remove suffixes like (FEMA Project), (CalOES Project), etc.
    # Pattern: " (FEMA...)" at the end
    base = re.sub(r'\s*\(.*?(FEMA|CalOES|CalJPIA).*?\)\s*$', '', name)
    return base.strip()

disaster_funding['Base_Name'] = disaster_funding['Project_Name'].apply(get_base_name)

# Parse Civic Docs for Start Dates
project_start_years = {}

# We need to find project blocks. 
# Strategy: Look for lines that match known project names (from Funding)
# Then scan following lines for dates.

# Get all known project names (both base and full) to scan for
known_projects = set(funding_data['Project_Name'].unique())
known_base_names = set(disaster_funding['Base_Name'].unique())
all_names = known_projects.union(known_base_names)

def normalize(text):
    return text.lower().strip()

normalized_names = {normalize(name): name for name in all_names}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if line is a project name
        # We use exact match or match with slight variations against known names
        norm_line = normalize(line_clean)
        
        if norm_line in normalized_names:
            current_project = normalized_names[norm_line]
            continue
            
        # If we are inside a project block, look for start dates
        if current_project:
            # Look for "Begin Construction: <Date>" or similar
            # Patterns:
            # Begin Construction: Fall 2023
            # Begin construction: April 2023
            # Construction start: ...
            
            # Regex for 2022
            if "2022" in line_clean:
                # Check context
                # "Begin Construction: ... 2022"
                # "Start: ... 2022"
                # "Schedule: ... 2022"
                if re.search(r'(?i)(begin construction|start construction|construction start|scheduled to start|advertise).*?2022', line_clean):
                    # Found a start in 2022
                    project_start_years[current_project] = 2022
                elif re.search(r'(?i)construction was completed.*?2022', line_clean):
                    # If completed in 2022, did it start in 2022?
                    # E.g. "Construction was completed November 2022"
                    # It might have started in 2022. 
                    # Let's verify if there's a separate start date. 
                    # If not, assume it started in 2022 if the duration is typically short?
                    # Or check for "Start" lines separately.
                    # For now, let's log it as potential.
                    if current_project not in project_start_years:
                        project_start_years[current_project] = 2022 # Tentative
                
                # Check for "Spring 2022", "Summer 2022", "Fall 2022", "Winter 2022"
                # But we already checked "2022" in line.

# Calculate Total Funding
total_funding = 0
funded_projects = []

for index, row in disaster_funding.iterrows():
    p_name = row['Project_Name']
    b_name = row['Base_Name']
    amount = row['Amount']
    
    # Check if this project started in 2022
    # Check exact name or base name
    started = False
    if p_name in project_start_years and project_start_years[p_name] == 2022:
        started = True
    elif b_name in project_start_years and project_start_years[b_name] == 2022:
        started = True
        
    if started:
        total_funding += amount
        funded_projects.append((p_name, amount))

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "funded_projects": funded_projects, "debug_start_years": list(project_start_years.keys())}))"""

env_args = {'var_function-call-3449562557564616894': 'file_storage/function-call-3449562557564616894.json', 'var_function-call-3449562557564617795': 'file_storage/function-call-3449562557564617795.json', 'var_function-call-1716930988388569207': 'file_storage/function-call-1716930988388569207.json'}

exec(code, env_args)
