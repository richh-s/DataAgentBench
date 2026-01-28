code = """import json
import pandas as pd
import re

# Load funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Simple extraction approach - collect all project info first
all_project_info = []

# Process each civic document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find project names - look for lines that are likely project names
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Heuristic: project names are often title case and not too long
        if len(line) < 120 and (line.istitle() or 'Project' in line):
            # Check if line contains project-related keywords
            keywords = ['Project', 'Improvement', 'Repair', 'Replacement', 'System', 
                       'Facility', 'Structure', 'Road', 'Street', 'Park', 'Drain', 'Bridge']
            if any(kw in line for kw in keywords):
                info = {'Project_Name': line}
                
                # Look for status in surrounding text
                context = ' '.join(lines[max(0,i-5):min(len(lines),i+10)]).lower()
                
                if 'design' in context:
                    info['status'] = 'design'
                elif 'construction' in context:
                    info['status'] = 'construction'
                elif 'completed' in context:
                    info['status'] = 'completed'
                
                # Check for FEMA or emergency
                if 'fema' in context:
                    info['topic'] = 'FEMA'
                elif 'emergency' in context or 'warning' in context:
                    info['topic'] = 'emergency'
                
                if 'topic' in info:
                    all_project_info.append(info)

# Create dataframes
df_funding = pd.DataFrame(funding_data)
df_info = pd.DataFrame(all_project_info)

# Filter for emergency/FEMA projects
emergency_info = df_info[df_info['topic'].isin(['FEMA', 'emergency'])]

# Get project names from info
info_names = set(emergency_info['Project_Name'].str.lower())

results = []

# Method 1: Match funding projects that contain emergency/FEMA keywords
emergency_keywords = ['fema', 'emergency', 'warning']
for _, fund in df_funding.iterrows():
    proj_name = fund['Project_Name'].lower()
    if any(kw in proj_name for kw in emergency_keywords):
        # Find matching status
        status = 'Unknown'
        for _, info in emergency_info.iterrows():
            if info['Project_Name'].lower() in proj_name or proj_name in info['Project_Name'].lower():
                status = info.get('status', 'Unknown')
                break
        
        results.append({
            'Project_Name': fund['Project_Name'],
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Status': status
        })

# Method 2: For projects in info that didn't match above, find similar funding records
for _, info in emergency_info.iterrows():
    info_name = info['Project_Name']
    matching_funds = df_funding[df_funding['Project_Name'].str.contains(info_name[:20], case=False, na=False)]
    
    if not matching_funds.empty:
        for _, fund in matching_funds.iterrows():
            # Prevent duplicates
            already_exists = any(r['Project_Name'] == fund['Project_Name'] for r in results)
            if not already_exists:
                results.append({
                    'Project_Name': fund['Project_Name'],
                    'Funding_Source': fund['Funding_Source'],
                    'Amount': int(fund['Amount']),
                    'Status': info.get('status', 'Unknown')
                })

# Convert to DataFrame and sort
result_df = pd.DataFrame(results)
if not result_df.empty:
    result_df = result_df.sort_values('Project_Name')
    output = result_df.to_dict('records')
else:
    output = []

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
