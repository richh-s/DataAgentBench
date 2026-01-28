code = """import json
import re

# Load all data
civic_path = locals()['var_functions.query_db:32']
funding_path = locals()['var_functions.query_db:33']

if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_path

# Create funding lookup - aggregate by base project name
funding_lookup = {}
for f in funding:
    name = f['Project_Name']
    amount = int(f['Amount'])
    
    # Store full name
    funding_lookup[name] = amount
    
    # Store base name without parentheses
    base = re.sub(r'\s*\([^)]*\)', '', name).strip()
    if base != name:
        funding_lookup[base] = funding_lookup.get(base, 0) + amount

# Find Spring 2022 projects by looking for date references
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Regex to find project names followed by Spring 2022 dates
    patterns = [
        r'([A-Z][a-zA-Z &\-]+?)(?:\s+\(.*?\))?\s*\n[^\n]{0,200}?(?:Spring|spring|March|April|May|Mar\.?|Apr\.?)[^\n]{0,50}?2022',
        r'(?:2022[^\n]{0,100}?(?:Spring|spring|March|April|May|Mar\.?|Apr\.?)[^\n]{0,100}?)\s*\n([A-Z][a-zA-Z &\-]+)'
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE):
            if match.group(1):
                proj_name = match.group(1).strip()
                if len(proj_name) > 5 and not proj_name.startswith('('):
                    # Skip common headers
                    if not any(skip in proj_name for skip in ['Agenda', 'Page', 'To:', 'From:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject']):
                        spring_projects.append(proj_name)

# Get unique projects
unique_projects = list(set(spring_projects))

# Match with funding
matched = []
total_funds = 0

for proj in unique_projects:
    best_match = None
    best_amount = 0
    
    # Try direct match
    if proj in funding_lookup:
        best_match = proj
        best_amount = funding_lookup[proj]
    else:
        # Try partial matching
        for fund_name, amount in funding_lookup.items():
            # Check if one name contains the other
            if (proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower()) and len(proj) > 10:
                if amount > best_amount:
                    best_match = fund_name
                    best_amount = amount
    
    if best_amount > 0:
        matched.append({'project': proj, 'funding': best_match, 'amount': best_amount})
        total_funds += best_amount

# Sort by amount and get top results
matched.sort(key=lambda x: x['amount'], reverse=True)
top_projects = matched[:20]

result = {
    'projects_found': len(unique_projects),
    'projects_with_funding': len(matched),
    'total_funding': total_funds,
    'top_projects': top_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
