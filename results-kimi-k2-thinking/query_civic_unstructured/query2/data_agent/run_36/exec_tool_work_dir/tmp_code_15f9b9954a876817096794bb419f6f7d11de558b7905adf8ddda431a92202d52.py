code = """import json
import os
import re
import pandas as pd

# Load funding data
funding_file = var_functions.query_db:39
if isinstance(funding_file, str):
    with open(funding_file, 'r') as f:
        funding_content = f.read().strip()
        funding_data = json.loads(funding_content) if funding_content.startswith('[') else []
else:
    funding_data = funding_file

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

print(f"Loaded {len(funding_df)} funding records")
print("Sample funding data:")
print(funding_df.head(3))

# Load park documents
park_file = var_functions.query_db:38
if isinstance(park_file, str):
    with open(park_file, 'r') as f:
        park_docs = json.load(f)
else:
    park_docs = park_file

print(f"\nLoaded {len(park_docs)} park-related documents")

# Extract park projects completed in 2022
park_2022_projects = []

for doc in park_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check for park/playground with completed and 2022
    if ('park' in lower_text or 'playground' in lower_text) and 'completed' in lower_text and '2022' in lower_text:
        
        # Look for specific project mentions
        # Pattern: Project name followed by completion mention
        patterns = [
            r'([A-Z][a-zA-Z\s]{5,}Park[A-Za-z\s]{0,50})[^.]*?(?:completed|completion)[^.]*?(?:2022|November\s+2022|December\s+2022)',
            r'([A-Z][a-zA-Z\s]{5,}Playground[A-Za-z\s]{0,30})[^.]*?(?:completed|completion)[^.]*?(?:2022|November\s+2022|December\s+2022)',
            r'(Bluffs\s+Park\s+Shade\s+Structure)',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                project_name = match.group(1).strip()
                # Clean up the name
                project_name = re.sub(r'\s+', ' ', project_name)
                project_name = re.sub(r'^[\-\•\■\s]+', '', project_name)
                
                if 10 < len(project_name) < 100:  # Reasonable length
                    # Verify it mentions completion in 2022
                    context_start = max(0, match.start() - 200)
                    context_end = min(len(text), match.end() + 200)
                    context = text[context_start:context_end].lower()
                    
                    if 'completed' in context and '2022' in context:
                        park_2022_projects.append(project_name)

# Remove duplicates while preserving order
seen = set()
unique_park_projects = []
for proj in park_2022_projects:
    if proj.lower() not in seen:
        seen.add(proj.lower())
        unique_park_projects.append(proj)

print(f"\nFound {len(unique_park_projects)} unique park projects completed in 2022:")
for proj in unique_park_projects:
    print(f"  - {proj}")

# Match with funding data
matched_projects = []
total_funding = 0

for park_proj in unique_park_projects:
    # Find exact or partial matches in funding database
    park_proj_lower = park_proj.lower()
    
    # Direct match attempt
    matches = funding_df[funding_df['Project_Name'].str.lower().str.contains(park_proj_lower, na=False)]
    
    if not matches.empty:
        for _, match in matches.iterrows():
            if match['Amount'] > 0:
                matched_projects.append({
                    'project_name': match['Project_Name'],
                    'amount': int(match['Amount']),
                    'funding_source': match['Funding_Source'],
                    'matched_to': park_proj
                })
                total_funding += match['Amount']
    else:
        # Try reverse matching - see if funding name is in our project name
        for _, fund_row in funding_df.iterrows():
            fund_name_lower = str(fund_row['Project_Name']).lower()
            if fund_name_lower in park_proj_lower and fund_row['Amount'] > 0:
                matched_projects.append({
                    'project_name': fund_row['Project_Name'],
                    'amount': int(fund_row['Amount']),
                    'funding_source': fund_row['Funding_Source'],
                    'matched_to': park_proj
                })
                total_funding += fund_row['Amount']

# Remove duplicate funding matches (same project might match multiple park projects)
unique_funding = {}
for proj in matched_projects:
    proj_name = proj['project_name']
    if proj_name not in unique_funding:
        unique_funding[proj_name] = proj

final_projects = list(unique_funding.values())
total_funding = sum(p['amount'] for p in final_projects)

print(f"\nMatched with funding:")
for proj in final_projects:
    print(f"  - {proj['project_name']}: ${proj['amount']:,}")

print(f"\nTotal funding for park projects completed in 2022: ${total_funding:,}")

result = {
    'total_funding': int(total_funding),
    'number_of_projects': len(final_projects),
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.execute_python:34': {'files': []}, 'var_functions.execute_python:36': {}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
