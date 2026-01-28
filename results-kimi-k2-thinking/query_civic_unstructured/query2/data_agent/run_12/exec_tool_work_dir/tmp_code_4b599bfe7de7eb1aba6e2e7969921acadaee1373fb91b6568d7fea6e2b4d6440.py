code = """import json
import pandas as pd
import re

# Load data from files
print("Loading data files...")

with open('/home/user/funding_data.json', 'r') as f:
    funding_data = json.load(f)

with open('/home/user/civic_docs_data.json', 'r') as f:
    civic_docs_data = json.load(f)

# Create funding dataframe
print("Processing funding data...")
df_funding = pd.DataFrame(funding_data)
print(f"Total funding records: {len(df_funding)}")

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []
print("Searching for park projects completed in 2022...")

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) > 80:
            continue
        
        # Check if line contains park-related terms
        if 'park' in line.lower() and not line.startswith('(') and not line.startswith('•'):
            # Check if associated with 2022 completion
            next_lines = ' '.join(lines[i:i+8]).lower()
            if '2022' in next_lines and 'completed' in next_lines:
                park_projects_2022.append(line)
                print(f"Found project: {line}")

print(f"Found {len(park_projects_2022)} park projects completed in 2022")

# Clean project names function
def clean_name(name):
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Apply cleaning
df_funding['clean_name'] = df_funding['Project_Name'].apply(clean_name)
cleaned_park_projects = [clean_name(p) for p in park_projects_2022]

# Find matches and calculate funding
total_funding = 0
matched_projects = []

print("Matching park projects with funding records...")

for i, park_name in enumerate(cleaned_park_projects):
    # Find matching funding records
    matches = df_funding[df_funding['clean_name'].str.contains(park_name, na=False) | 
                        df_funding['Project_Name'].str.contains(park_name, na=False)]
    
    if not matches.empty:
        for _, match_row in matches.iterrows():
            amount = int(match_row['Amount'])
            total_funding += amount
            matched_projects.append({
                'park_project': park_projects_2022[i],
                'funding_record': match_row['Project_Name'],
                'amount': amount
            })
            print(f"Match: {park_projects_2022[i]} -> {match_row['Project_Name']} = ${amount:,}")

# Additional check: Look for funding records that might be park projects
all_funding_names = df_funding['clean_name'].tolist()
for i, park_name in enumerate(cleaned_park_projects):
    for fund_name in all_funding_names:
        if park_name in fund_name or fund_name in park_name:
            fund_row = df_funding[df_funding['clean_name'] == fund_name].iloc[0]
            amount = int(fund_row['Amount'])
            # Check if not already matched
            already_matched = any(m['park_project'] == park_projects_2022[i] and 
                                 m['funding_record'] == fund_row['Project_Name'] for m in matched_projects)
            if not already_matched:
                total_funding += amount
                matched_projects.append({
                    'park_project': park_projects_2022[i],
                    'funding_record': fund_row['Project_Name'],
                    'amount': amount
                })
                print(f"Additional match: {park_projects_2022[i]} -> {fund_row['Project_Name']} = ${amount:,}")

print(f"\nTotal matched projects: {len(matched_projects)}")
print(f"Total funding for park projects completed in 2022: ${total_funding:,}")

# Prepare result
result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects
}

# Final output in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
