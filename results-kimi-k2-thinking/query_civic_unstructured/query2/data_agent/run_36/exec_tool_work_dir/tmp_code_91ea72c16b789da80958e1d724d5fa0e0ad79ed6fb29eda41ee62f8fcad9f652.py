code = """import json
import pandas as pd
import os
import re

# Load park documents data
park_file = "/tmp/tmprv7m5z8x.json"
if os.path.exists(park_file):
    with open(park_file, 'r') as f:
        park_docs = json.load(f)
else:
    park_docs = []

# Load funding data
funding_file = "/tmp/tmp4g9x7lxn.json"
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            funding_data = json.loads(content)
        else:
            funding_data = []
else:
    funding_data = []

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
if not funding_df.empty:
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Find park projects that mention completion in 2022
park_2022_names = []

for doc in park_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for park/playground with completed and 2022
    if ('park' in lower_text or 'playground' in lower_text) and 'completed' in lower_text and '2022' in lower_text:
        # Look for specific project name patterns
        patterns = [
            r'Bluffs Park Shade Structure',
            r'Trancas Canyon Park[^\n]*',
            r'[^.]*Park[^.]*2022[^.]*',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                proj_text = match.group(0).strip()
                if len(proj_text) < 150 and 'completed' in proj_text.lower():
                    # Extract project name (first line or reasonable length)
                    lines = proj_text.split('\n')
                    for line in lines:
                        line_clean = line.strip()
                        if line_clean and len(line_clean) > 10:
                            park_2022_names.append(line_clean)
                            break

# Remove very short or generic names
park_2022_names = [name for name in park_2022_names if len(name) > 15]

# Get unique names
unique_park_names = list(set(park_2022_names))

# Find matching funding records
matched_projects = []
total_funding = 0

if not funding_df.empty:
    for park_name in unique_park_names:
        # Search for funding matches
        for _, fund_row in funding_df.iterrows():
            fund_name = str(fund_row['Project_Name'])
            
            # Check for matches
            if (park_name.lower() in fund_name.lower() or 
                fund_name.lower() in park_name.lower() or
                ('park' in fund_name.lower() and any(term in fund_name.lower() for term in ['bluffs', 'trancas', 'shade', '2022']))):
                
                amount = fund_row['Amount']
                if amount > 0:
                    matched_projects.append({
                        'project_name': fund_name,
                        'amount': int(amount),
                        'funding_source': fund_row['Funding_Source']
                    })
                    total_funding += amount

# If no exact matches, get all park projects with 2022 in name
if not matched_projects and not funding_df.empty:
    park_in_2022 = funding_df[funding_df['Project_Name'].str.contains('2022|park', case=False, na=False)]
    for _, row in park_in_2022.iterrows():
        if 'park' in str(row['Project_Name']).lower():
            amount = row['Amount']
            if amount > 0:
                matched_projects.append({
                    'project_name': row['Project_Name'],
                    'amount': int(amount),
                    'funding_source': row['Funding_Source']
                })
                total_funding += amount

result_data = {
    'total_funding': int(total_funding),
    'project_count': len(matched_projects),
    'projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
