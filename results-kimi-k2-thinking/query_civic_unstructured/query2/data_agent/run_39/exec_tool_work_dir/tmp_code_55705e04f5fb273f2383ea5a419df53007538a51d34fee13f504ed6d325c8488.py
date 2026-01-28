code = """import json
import re

# Load the MongoDB documents
mongo_path = locals()['var_functions.query_db:2']
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Load the funding records
funding_path = locals()['var_functions.query_db:5']
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Build a list of park projects from the MongoDB text that were completed in 2022
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    
    # Look for the pattern: Project Name on one line, then later "completed" with "2022"
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this line looks like a project name (contains park, reasonable length, not a header)
        if 'park' in line.lower() and 5 < len(line) < 100:
            # Skip if it's a document header
            if line.startswith('Page') or line.startswith('Agenda Item'):
                continue
            if line.startswith('To:') or 'RECOMMENDED ACTION' in line or 'DISCUSSION:' in line:
                continue
            if '(cid:' in line:
                continue
            
            # Look ahead for completion in 2022
            found_2022_completion = False
            for j in range(i+1, min(i+20, len(lines))):
                ahead_line = lines[j]
                ahead_lower = ahead_line.lower()
                
                if 'completed' in ahead_lower and '2022' in ahead_line:
                    found_2022_completion = True
                    break
            
            if found_2022_completion:
                clean_name = re.sub(r'^[\s\-•●■]+', '', line)
                park_projects_2022.append(clean_name)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Build funding map for quick lookup
funding_map = {}
for rec in funding_recs:
    proj_name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[proj_name] = amount

# Match projects with funding and sum amounts
total_funding = 0
matched_projects = []

for proj in park_projects_2022:
    for fund_proj in funding_map:
        # Check for match (case insensitive, partial match)
        proj_lower = proj.lower()
        fund_lower = fund_proj.lower()
        
        # Match if one string is contained in the other
        if proj_lower in fund_lower or fund_lower in proj_lower:
            amount = funding_map[fund_proj]
            total_funding += amount
            matched_projects.append({
                'project_name': proj,
                'funding_record_name': fund_proj,
                'amount': amount
            })

result = {
    'total_funding_2022_park_projects': total_funding,
    'number_of_matched_projects': len(park_projects_2022),
    'projects': park_projects_2022,
    'funding_details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}, 'var_functions.execute_python:44': {'mongo_docs': 19, 'funding_records': 500}}

exec(code, env_args)
