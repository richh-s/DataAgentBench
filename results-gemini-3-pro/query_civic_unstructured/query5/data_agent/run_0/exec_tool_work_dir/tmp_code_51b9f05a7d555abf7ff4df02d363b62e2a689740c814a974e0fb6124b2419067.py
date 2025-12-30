code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-1023604252681241279'], 'r') as f:
    funding_list = json.load(f)

with open(locals()['var_function-call-1023604252681243206'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of Project Name to Funding Info
funding_df = pd.DataFrame(funding_list)
project_funding = {row['Project_Name']: row['Amount'] for _, row in funding_df.iterrows()}
known_projects = set(project_funding.keys())

# Parse logic
project_details = {} # Name -> {'st': year, 'type': 'capital' or 'disaster'}

# Combined text for easier searching? No, structure matters.
# Let's process line by line.

current_project = None
current_type_context = 'capital' # Default

# Regex for start date
# Look for "Begin Construction: <Date>" or "Start: <Date>"
# We want the year.
date_pattern = re.compile(r'(?:Begin Construction|Start Date|Construction Start|Advertise).*?(\d{4})', re.IGNORECASE)

for doc in civic_docs:
    lines = doc['text'].split('\n')
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        # Check for section headers to help with type context
        if "Disaster Recovery Projects" in clean_line:
            current_type_context = 'disaster'
        elif "Capital Improvement Projects" in clean_line:
            current_type_context = 'capital'
        
        # Check if line is a project name
        # Using exact match from known projects
        if clean_line in known_projects:
            current_project = clean_line
            # Determine type
            # 1. By Context
            p_type = current_type_context
            # 2. By Name Suffix (override or confirm)
            lower_name = clean_line.lower()
            if any(x in lower_name for x in ['fema', 'caloes', 'caljpia', 'woolsey']):
                p_type = 'disaster'
            
            if current_project not in project_details:
                project_details[current_project] = {'type': p_type, 'st': None}
            else:
                # Update type if we found a disaster indicator
                if p_type == 'disaster':
                    project_details[current_project]['type'] = 'disaster'
            continue
            
        # If inside a project, look for start date
        if current_project:
            # We look for date pattern
            match = date_pattern.search(clean_line)
            if match:
                year = match.group(1)
                # Store the year
                # Prefer "Begin Construction" year if multiple dates appear?
                # The regex matches "Begin Construction" first.
                # If we already have a date, maybe we keep it or overwrite?
                # Usually "Begin Construction" is the definitive start.
                # Let's overwrite if we match "Begin Construction" specifically.
                
                existing_st = project_details[current_project]['st']
                
                # If we extracted a year, set it.
                # If we already extracted a year, only overwrite if this line is explicitly "Begin Construction" and the previous wasn't?
                # For simplicity, let's just take the first valid date year we find in the block, 
                # or specifically look for "Begin Construction" if possible.
                
                # Refined check:
                if "begin construction" in clean_line.lower():
                     project_details[current_project]['st'] = year
                elif existing_st is None:
                     project_details[current_project]['st'] = year

# Calculate Total Funding
total_funding = 0
matches = []

for p_name, details in project_details.items():
    p_type = details['type']
    st = details['st']
    
    # Filter: Disaster related AND started in 2022
    if p_type == 'disaster' and st == '2022':
        amount = int(project_funding.get(p_name, 0))
        total_funding += amount
        matches.append({'name': p_name, 'amount': amount, 'st': st})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matches': matches}))"""

env_args = {'var_function-call-1023604252681241279': 'file_storage/function-call-1023604252681241279.json', 'var_function-call-1023604252681243206': 'file_storage/function-call-1023604252681243206.json'}

exec(code, env_args)
