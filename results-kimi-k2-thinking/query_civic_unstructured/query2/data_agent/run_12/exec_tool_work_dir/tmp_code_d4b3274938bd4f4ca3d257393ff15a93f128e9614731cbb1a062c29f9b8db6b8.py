code = """import json
import re

# Access data from storage
funding_data = var_functions.query_db_5
civic_docs_data = var_functions.query_db_2

# Find park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    # Look for park projects completed in 2022 using text patterns
    if 'park' in text.lower():
        # Find specific mentions of completion dates in 2022
        if '2022' in text and 'completed' in text.lower() and 'park' in text.lower():
            # Look for specific park project names
            lines = text.split('\n')
            for line in lines:
                line_clean = line.strip()
                if 'park' in line_clean.lower() and len(line_clean) < 150:
                    park_projects_2022.append(line_clean)

# Function to clean project names for matching
def clean_name(name):
    if not name:
        return ''
    name = re.sub(r'\s+Project\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Design\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*-\s*Construction\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Match park projects with funding records
total_funding = 0
matched_projects = []

for park_project in park_projects_2022:
    if not park_project:
        continue
    
    park_clean = clean_name(park_project)
    if not park_clean:
        continue
    
    # Check each funding record
    for fund_record in funding_data:
        fund_project = fund_record.get('Project_Name', '')
        if not fund_project:
            continue
            
        fund_clean = clean_name(fund_project)
        if not fund_clean:
            continue
            
        # Check for name similarity
        if (park_clean in fund_clean or fund_clean in park_clean or 
            abs(len(park_clean) - len(fund_clean)) < 5 and park_clean.replace(' ', '') == fund_clean.replace(' ', '')):
            
            fund_amount = int(fund_record.get('Amount', 0))
            total_funding += fund_amount
            matched_projects.append({
                'park_project': park_project,
                'funding_project': fund_project,
                'amount': fund_amount
            })

# Sum unique funding amounts (avoid duplicates)
unique_funding = {}
for match in matched_projects:
    funding_name = match['funding_project']
    if funding_name not in unique_funding:
        unique_funding[funding_name] = match['amount']

final_total = sum(unique_funding.values())

print('__RESULT__:')
print(json.dumps({
    'total_funding': final_total,
    'unique_matched_projects': len(unique_funding),
    'all_matches': len(matched_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:36': {'total_funding': 0, 'park_records_found': 0}}

exec(code, env_args)
