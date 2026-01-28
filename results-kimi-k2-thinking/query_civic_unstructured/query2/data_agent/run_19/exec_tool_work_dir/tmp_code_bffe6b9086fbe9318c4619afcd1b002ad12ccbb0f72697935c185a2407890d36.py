code = """import json
import re

# Load full datasets
f_path = locals()['var_functions.query_db:0']
c_path = locals()['var_functions.query_db:14']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    docs = json.load(f)

# Comprehensive approach to find all park projects completed in 2022

# Step 1: Identify all park-related projects in funding database
park_projects = []
for rec in funding:
    name = rec.get('Project_Name', '')
    low_name = name.lower()
    # Broader park-related keywords
    if any(kw in low_name for kw in ['park', 'bluffs', 'playground', 'arbors', 'walkway', 'shade', 'recreation', 'trancas', 'legacy park']):
        park_projects.append({'name': name, 'amount': int(rec.get('Amount', 0))})

# Step 2: Extract all projects completed in 2022 from civic documents
completed_2022 = []
for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for completion indicators with 2022
        if '2022' in line and ('completed' in line.lower() or 'construction was completed' in line.lower()):
            # Look backwards for project name
            for j in range(max(0, i-20), i):
                prev = lines[j].strip()
                # Skip formatting lines
                if prev and len(prev) > 8 and not prev.startswith('(') and not prev.startswith('•') and not prev.startswith('Page'):
                    completed_2022.append(prev)
                    break
        i += 1

# Step 3: Check for specific known completed projects
for doc in docs:
    text = doc.get('text', '').lower()
    
    # Bluffs Park Shade Structure - completed November 2022
    if 'bluffs park shade structure' in text and 'november 2022' in text and 'completed' in text:
        completed_2022.append('Bluffs Park Shade Structure')
        
    # Broad Beach Road Water Quality Repair - completed November 2022  
    if 'broad beach road water quality repair' in text and 'november 2022' in text:
        completed_2022.append('Broad Beach Road Water Quality Repair')
        
    # Point Dume Walkway Repairs - completed November 2022
    if 'point dume walkway repairs' in text and 'november 2022' in text:
        completed_2022.append('Point Dume Walkway Repairs')
        
    # Marie Canyon Green Streets - mentioned but check if 2022
    if 'marie canyon green streets' in text and '2022' in text:
        completed_2022.append('Marie Canyon Green Streets')
        
    # Trancas Canyon Park projects
    if 'trancas canyon park' in text and '2022' in text and 'completed' in text:
        completed_2022.append('Trancas Canyon Park')

# Step 4: Match park funding projects with 2022 completions
total_funding = 0
matched_project_names = []

for park_proj in park_projects:
    park_name = park_proj['name']
    park_name_lower = park_name.lower()
    
    for completed_proj in completed_2022:
        comp_lower = completed_proj.lower()
        
        # Try multiple matching strategies
        match = False
        
        # 1. Direct substring match
        if park_name_lower in comp_lower or comp_lower in park_name_lower:
            match = True
        
        # 2. Word overlap (at least 2 significant words)
        if not match:
            park_words = set(w for w in park_name_lower.split() if len(w) > 3)
            comp_words = set(w for w in comp_lower.split() if len(w) > 3)
            # Exclude common words from intersection
            common_words = {'project', 'repair', 'improvements', 'improvement', 'and', 'the', 'at', 'of', 'for', 'to'}
            meaningful_intersection = park_words.intersection(comp_words) - common_words
            
            if len(meaningful_intersection) >= 2:
                match = True
                
        # 3. Keyword matching for specific known projects
        if not match:
            if 'bluffs park' in park_name_lower and 'bluffs park' in comp_lower:
                match = True
            elif 'broad beach' in park_name_lower and 'broad beach' in comp_lower:
                match = True
            elif 'point dume' in park_name_lower and 'point dume' in comp_lower:
                match = True
                
        if match:
            total_funding += park_proj['amount']
            matched_project_names.append(park_name)
            break

# Deduplicate while preserving totals
unique_projects = list(set(matched_project_names))
final_total = sum(p['amount'] for p in park_projects if p['name'] in unique_projects)

# Sort projects alphabetically
sorted_projects = sorted(unique_projects)

result = {
    'total_funding_2022_park_projects': final_total,
    'number_of_projects': len(sorted_projects),
    'project_names': sorted_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
