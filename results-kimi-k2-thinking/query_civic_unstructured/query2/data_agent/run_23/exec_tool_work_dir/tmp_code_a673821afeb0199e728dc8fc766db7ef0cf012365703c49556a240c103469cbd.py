code = """import json
import re

# Load civic documents
civic_path = locals()['var_functions.query_db:14']
if isinstance(civic_path, str):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

# Load funding data
funding_path = locals()['var_functions.query_db:38']
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path

print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Extract projects completed in 2022 from civic documents
completed_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for completion patterns like "completed November 2022" or "completed, November 2022"
    # Extract project names and completion dates
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if this line mentions completion in 2022
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line:
            # Look back to find project name (typically 1-3 lines above)
            project_name = None
            for j in range(i-1, max(-1, i-5), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) < 100:
                    # Skip formatting lines
                    if prev_line.startswith('(') or prev_line.startswith('●') or prev_line.startswith('■'):
                        continue
                    if 'Updates:' in prev_line or 'Schedule:' in prev_line or 'RECOMMENDED' in prev_line:
                        continue
                    project_name = prev_line
                    break
            
            if project_name:
                completed_2022_projects.append(project_name)

# Remove duplicates
unique_projects = list(set(completed_2022_projects))
print('Projects completed in 2022:', len(unique_projects))

# Filter for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume', 'canyon']
park_projects = []

for proj_name in unique_projects:
    proj_lower = proj_name.lower()
    if any(kw in proj_lower for kw in park_keywords):
        park_projects.append(proj_name)

print('Park-related projects completed in 2022:', len(park_projects))
for p in park_projects:
    print(' -', p)

# Now find funding for these projects
total_funding = 0
funded_projects = []

for project_name in park_projects:
    # Look for matching funding records
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        if fund_name and project_name in fund_name:
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            funded_projects.append({
                'project': project_name,
                'funded_as': fund_name,
                'amount': amount
            })
        elif project_name in fund_name:
            # Also check reverse match
            amount = int(fund.get('Amount', 0))
            total_funding += amount
            funded_projects.append({
                'project': project_name,
                'funded_as': fund_name,
                'amount': amount
            })

# Also check for partial matches with common park projects
# Common park projects from the data:
common_park_names = [
    'Bluffs Park Shade Structure',
    'Bluffs Park Workout Station',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Malibu Bluffs Park Roof Replacement Project',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Trancas Canyon Park Playground',
    'Marie Canyon Green Streets',
    'Point Dume Walkway Repairs'
]

for project_name in common_park_names:
    # Check if this project was completed in 2022 by looking at the text
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text and '2022' in text:
            # Check if it mentions completion in 2022
            if 'completed' in text.lower() and '2022' in text:
                # Look for funding
                for fund in funding_data:
                    fund_name = fund.get('Project_Name', '')
                    if project_name == fund_name:
                        amount = int(fund.get('Amount', 0))
                        total_funding += amount
                        funded_projects.append({
                            'project': project_name,
                            'funded_as': fund_name,
                            'amount': amount
                        })

# Remove duplicate funding entries
unique_funding = []
seen = set()
for item in funded_projects:
    key = (item['project'], item['funded_as'])
    if key not in seen:
        seen.add(key)
        unique_funding.append(item)

total_funding = sum(item['amount'] for item in unique_funding)

print('Unique funded projects:', len(unique_funding))
print('Total funding:', total_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(unique_funding),
    'projects': unique_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
