code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
civic_path = locals()['var_functions.query_db:14']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Define keywords for park-related projects
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation']

# Step 1: Get all park-related projects from funding database
park_funding = []
for rec in funding_records:
    pname = rec.get('Project_Name')
    if pname and any(kw in pname.lower() for kw in park_keywords):
        park_funding.append({
            'name': pname,
            'amount': int(rec.get('Amount', 0))
        })

# Step 2: Extract projects completed in 2022 from civic documents
completed_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if line indicates completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'construction was completed' in line.lower()):
            # Look backwards to find project name (up to 15 lines)
            for j in range(max(0, i-15), i):
                prev = lines[j].strip()
                # Skip empty lines, bullets, and symbols
                if prev and len(prev) > 10 and not prev.startswith('(') and not prev.startswith('•'):
                    completed_2022.append(prev)
                    break

# Step 3: Match park funding projects with 2022 completions
total_funding = 0
matched_projects = []

for park_proj in park_funding:
    park_name = park_proj['name']
    
    for completed_proj in completed_2022:
        # Match criteria: share important words
        park_words = set(word.lower() for word in park_name.split() if len(word) > 3)
        completed_words = set(word.lower() for word in completed_proj.split() if len(word) > 3)
        
        # At least 2 matching important words
        if len(park_words.intersection(completed_words)) >= 2:
            total_funding += park_proj['amount']
            matched_projects.append(park_name)
            break
        # Or direct substring match
        elif park_name.lower() in completed_proj.lower() or completed_proj.lower() in park_name.lower():
            total_funding += park_proj['amount']
            matched_projects.append(park_name)
            break

# Step 4: Check for explicit project mentions
explicit_projects = []
for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Check specific projects known to be completed in 2022
    if 'bluffs park shade structure' in text and '2022' in text:
        explicit_projects.append('Bluffs Park Shade Structure')
    if 'broad beach road water quality repair' in text and '2022' in text:
        explicit_projects.append('Broad Beach Road Water Quality Repair')
    if 'point dume walkway repairs' in text and '2022' in text:
        explicit_projects.append('Point Dume Walkway Repairs')

# Add explicit projects if not already matched
for exp_proj in explicit_projects:
    found = False
    for matched in matched_projects:
        if exp_proj in matched or matched in exp_proj:
            found = True
            break
    
    if not found:
        # Find in funding data
        for pf in park_funding:
            if exp_proj in pf['name'] or pf['name'] in exp_proj:
                total_funding += pf['amount']
                matched_projects.append(pf['name'])
                break

# Deduplicate and calculate final total
unique_projects = list(set(matched_projects))
final_total = sum(pf['amount'] for pf in park_funding if pf['name'] in unique_projects)

print('__RESULT__:')
print(json.dumps({
    'total_funding_2022_park_projects': final_total,
    'project_count': len(unique_projects),
    'projects': sorted(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
