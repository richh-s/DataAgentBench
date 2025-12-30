code = """import json
import pandas as pd

# Load Funding
f_key = 'var_function-call-9396770381544518491'
with open(locals()[f_key], 'r') as f:
    funding_data = json.load(f)

# Load Extracted
e_key = 'var_function-call-3853755936868958583'
with open(locals()[e_key], 'r') as f:
    extracted_data = json.load(f)

# Create lookup for Funding
# Map Project_Name -> Amount
# Handle potential duplicates in funding? 
# Funding table usually has unique ID.
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    amount = float(item['Amount'])
    funding_map[name] = amount

# Identify disaster projects that started in 2022
# Deduplicate names
unique_projects = set()
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']

for p in extracted_data:
    name = p['n'].strip()
    is_disaster = False
    
    # Check name for keywords
    for kw in disaster_keywords:
        if kw in name:
            is_disaster = True
            break
    
    # Check start date flag
    started_2022 = p['s']
    
    if is_disaster and started_2022:
        unique_projects.add(name)

# Calculate total
total_funding = 0
found_projects = []

for name in unique_projects:
    # Try exact match first
    if name in funding_map:
        total_funding += funding_map[name]
        found_projects.append((name, funding_map[name]))
    else:
        # Try finding closest match?
        # Maybe text extracted "Project Name " with space?
        # I stripped.
        # Maybe punctuation?
        pass

print(f"Found {len(found_projects)} matching projects.")
print(found_projects)
print("__RESULT__:")
print(total_funding)"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json', 'var_function-call-3853755936868958583': 'file_storage/function-call-3853755936868958583.json'}

exec(code, env_args)
