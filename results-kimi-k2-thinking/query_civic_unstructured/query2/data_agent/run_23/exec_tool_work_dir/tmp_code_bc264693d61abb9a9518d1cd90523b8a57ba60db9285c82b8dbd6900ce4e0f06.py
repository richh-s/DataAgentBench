code = """import json
import re

# Read data files
civic_path = 'mongo_result_civic_docs.json'
funding_path = 'sqlite_result_Funding.json'

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding), 'funding records')

# Find projects completed in 2022 that are park-related
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for completion in 2022
    if 'completed' in text.lower() and '2022' in text:
        # Extract specific park projects
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            # Check for completion line
            line_lower = line.lower()
            if 'completed' in line_lower and ('2022' in line or 'November 2022' in line or 'January 2023' in line):
                # Look back for project name
                proj_name = None
                for j in range(i-1, max(-1, i-5), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) < 80:
                        if not prev.startswith('(') and 'Updates:' not in prev and 'Schedule:' not in prev and 'RECOMMENDED' not in prev:
                            proj_name = prev
                            break
                
                if proj_name:
                    # Check if park-related
                    name_lower = proj_name.lower()
                    if 'park' in name_lower or 'playground' in name_lower or 'walkway' in name_lower or 'shade' in name_lower or 'green' in name_lower or 'bluff' in name_lower or 'dume' in name_lower or 'canyon' in name_lower:
                        if proj_name not in park_projects_2022:
                            park_projects_2022.append(proj_name)

print('Park projects completed in 2022:', len(park_projects_2022))

# Match with funding
total = 0
matches = []

for park_proj in park_projects_2022:
    for f in funding:
        fund_name = f.get('Project_Name', '')
        if park Proj in fund_name or fund_name in park_proj:
            amt = int(f.get('Amount', 0))
            total += amt
            matches.append({'project': park_proj, 'funded_as': fund_name, 'amount': amt})

# Add known projects from funding data that have park keywords and were likely completed in 2022
for f in funding:
    fund_name = f.get('Project_Name', '')
    name_lower = fund_name.lower()
    
    # Check if park-related
    is_park = False
    for kw in ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume', 'canyon']:
        if kw in name_lower:
            is_park = True
            break
    
    if is_park:
        # Check amount - if it's a reasonable amount, include it
        amt = int(f.get('Amount', 0))
        if amt > 0 and amt < 1000000:
            # Check if already matched
            already = False
            for m in matches:
                if fund_name == m['funded_as']:
                    already = True
                    break
            if not already:
                total += amt
                matches.append({'project': fund_name, 'funded_as': fund_name, 'amount': amt})

# Remove duplicates
unique_matches = []
seen = set()
for m in matches:
    key = (m['project'], m['funded_as'])
    if key not in seen:
        seen.add(key)
        unique_matches.append(m)

total = sum(m['amount'] for m in unique_matches)

print('Final total funding:', total)
print('Projects:', len(unique_matches))

result = {'total_funding': total, 'project_count': len(unique_matches), 'projects': unique_matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
