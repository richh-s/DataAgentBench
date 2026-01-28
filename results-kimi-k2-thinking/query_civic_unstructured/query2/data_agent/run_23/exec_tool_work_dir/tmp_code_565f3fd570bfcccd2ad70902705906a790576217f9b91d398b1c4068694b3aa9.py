code = """import json, re

# Load data from files
civic_path = 'mongo_result_civic_docs.json'
funding_path = 'sqlite_result_Funding.json'

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'civic docs and', len(funding_data), 'funding records')

# Find park projects completed in 2022
park_projects_completed = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Check if document mentions 2022 completion
    if 'completed' in text.lower() and '2022' in text:
        # Extract project names that are park-related and completed in 2022
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            line_lower = line.lower()
            if 'completed' in line_lower and '2022' in line:
                # Look for project name
                project_name = None
                for j in range(i-1, max(-1, i-5), -1):
                    prev = lines[j].strip()
                    if prev and len(prev) < 80:
                        if not prev.startswith('(') and 'Updates:' not in prev and 'Schedule:' not in prev:
                            project_name = prev
                            break
                
                if project_name:
                    # Check if park-related
                    if any(kw in project_name.lower() for kw in ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']):
                        park_projects_completed.append(project_name)

# Remove duplicates
park_projects_completed = list(set(park_projects_completed))
print('Park projects completed in 2022:', len(park_projects_completed))

# Match with funding data
matched_projects = []
total_funding = 0

for park_proj in park_projects_completed:
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        # Direct match or partial match
        if park_proj in fund_name or fund_name in park_proj:
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            matched_projects.append({
                'project_name': park_proj,
                'funded_as': fund_name,
                'amount': amount
            })

# Also check known park projects that were completed in 2022
known_park_projects = [
    'Bluffs Park Shade Structure',
    'Point Dume Walkway Repairs',
    'Marie Canyon Green Streets'
]

for project in known_park_projects:
    for doc in civic_docs:
        text = doc.get('text', '')
        if project in text and 'completed' in text.lower() and '2022' in text:
            for fund in funding_data:
                if fund.get('Project_Name', '') == project:
                    amount = int(fund.get('Amount', 0))
                    already_exists = any(m['project_name'] == project for m in matched_projects)
                    if not already_exists:
                        total_funding += amount
                        matched_projects.append({
                            'project_name': project,
                            'funded_as': project,
                            'amount': amount
                        })

# Remove duplicates
unique_matches = []
seen = set()
for m in matched_projects:
    key = (m['project_name'], m['funded_as'])
    if key not in seen:
        seen.add(key)
        unique_matches.append(m)

total_funding = sum(m['amount'] for m in unique_matches)

print('Total matched projects:', len(unique_matches))
print('Total funding:', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(unique_matches),
    'details': unique_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
