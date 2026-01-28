code = """import json
import pandas as pd
import re

# Load data
f = open(locals()['var_functions.query_db:5'], 'r')
funding_data = json.load(f)
f.close()

f = open(locals()['var_functions.query_db:0'], 'r')
civic_data = json.load(f)
f.close()

# Create DataFrames
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Get disaster projects
pattern = r'FEMA|Cal.?OES|CalJPIA|disaster|recovery'
disaster_df = funding_df[funding_df['Project_Name'].str.contains(pattern, case=False, na=False)].copy()

# Extract projects with 2022 dates from civic documents
projects_2022 = []

for doc in civic_data:
    text = doc.get('text', '')
    
    # Look for project sections
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (clean up common prefixes)
        if len(line) < 150 and not any(line.startswith(x) for x in ['(', '•', '-', '●', '■', '_', '\x95']):
            if any(keyword in line.lower() for keyword in ['project', 'repair', 'improvement', 'replacement', 'resurfacing']):
                current_project = line
        
        # Check for 2022 mention
        if current_project and '2022' in line:
            # Clean the project name for matching
            cleaned_name = current_project.split('(')[0].strip()
            if cleaned_name not in [p['clean_name'] for p in projects_2022]:
                projects_2022.append({
                    'clean_name': cleaned_name,
                    'original': current_project,
                    'line_with_2022': line
                })

# Match with funding data
total_2022_funding = 0
matched_funding_projects = []

for project in projects_2022:
    clean_name = project['clean_name']
    
    # Find matching funding records
    for _, row in disaster_df.iterrows():
        fund_name = row['Project_Name']
        fund_amount = row['Amount']
        
        # Check for direct match or partial match
        fund_clean = fund_name.split('(')[0].strip()
        
        if (clean_name in fund_clean or fund_clean in clean_name or
            any(word in fund_clean for word in clean_name.split() if len(word) > 4) or
            any(word in clean_name for word in fund_clean.split() if len(word) > 4)):
            
            if fund_name not in matched_funding_projects:
                total_2022_funding += fund_amount
                matched_funding_projects.append(fund_name)

result = {
    'projects_with_2022_mentions': len(projects_2022),
    'matched_funding_projects': len(matched_funding_projects),
    'total_2022_funding': int(total_2022_funding),
    'sample_projects_2022': [p['clean_name'] for p in projects_2022[:5]]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:16': {'total_funding_2022': 0, 'total_disaster_funding': 1410000, 'disaster_2022_projects_count': 0}}

exec(code, env_args)
