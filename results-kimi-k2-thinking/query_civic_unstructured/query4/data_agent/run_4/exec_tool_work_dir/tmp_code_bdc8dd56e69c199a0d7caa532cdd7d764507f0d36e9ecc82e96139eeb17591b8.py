code = """import json
import re

# Get the stored data
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:4

# Load civic documents from file
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for fund in funding_records:
    proj_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[proj_name] = amount

print(f'Loaded {len(civic_docs)} civic documents and {len(funding_records)} funding records')

# Extract Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections that mention Spring 2022
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Try to identify project names (capitalize, contains keywords)
        if (len(line) > 10 and len(line) < 150 and 
            not line.startswith('(') and 
            not any(line.startswith(x) for x in ['To:', 'From:', 'Subject:', 'Date:', 'Meeting', 'Public Works', 'Commission', 'Agenda']) and
            any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Replacement', 'Facility', 'System', 'Road', 'Park', 'Drainage'])):
            current_project = line
        
        # Check if this line mentions Spring 2022
        if ('Spring 2022' in line or '2022-Spring' in line) and current_project:
            spring_2022_projects.append(current_project)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match with funding data using various matching strategies
total_funding = 0
matched_projects = []

# First, create a list of all funding project names for comparison
all_funding_names = list(funding_lookup.keys())

for proj in spring_2022_projects:
    # Direct match
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        matched_projects.append({'project': proj, 'funding': amount})
        total_funding += amount
        continue
    
    # Partial match - check if one string is contained in the other
    for fund_proj in all_funding_names:
        proj_clean = proj.lower().replace('project', '').strip()
        fund_clean = fund_proj.lower().replace('project', '').strip()
        
        # Check for substantial overlap
        if (proj_clean in fund_clean or fund_clean in proj_clean) and abs(len(proj) - len(fund_proj)) < 30:
            if fund_proj not in [p.get('matched_name', p['project']) for p in matched_projects]:
                amount = funding_lookup[fund_proj]
                matched_projects.append({'project': proj, 'matched_name': fund_proj, 'funding': amount})
                total_funding += amount
                break

# Remove duplicates from matched projects
unique_matches = {}
for proj in matched_projects:
    key = proj.get('matched_name', proj['project'])
    if key not in unique_matches:
        unique_matches[key] = proj['funding']

final_projects = [{'project': k, 'funding': v} for k, v in unique_matches.items()]
total_funding = sum(v for v in unique_matches.values())

result = {
    'spring_2022_projects_count': len(final_projects),
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
