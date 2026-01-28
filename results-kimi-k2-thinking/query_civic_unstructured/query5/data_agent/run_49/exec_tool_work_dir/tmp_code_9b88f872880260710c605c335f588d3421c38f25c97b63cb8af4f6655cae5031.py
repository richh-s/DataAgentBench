code = """import json
import re

# Load funding data
funding_key = 'var_functions.query_db:6'
funding_data = locals()[funding_key]
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Load civic docs data
civic_key = 'var_functions.query_db:8'
civic_docs = locals()[civic_key]
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_map[name] = amount

# Extract disaster projects with 2022 start dates
disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if not line:
            continue
            
        # Check for disaster project indicators
        if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
            project_name = line
            has_2022 = False
            
            # Check next 15 lines for date information
            for j in range(i, min(i+15, len(lines))):
                next_line = lines[j]
                if '2022' in next_line:
                    has_2022 = True
                    break
            
            if has_2022:
                disaster_projects.append(project_name)

# Calculate total funding
total_funding = 0
matched = []

for project_name in disaster_projects:
    # Direct match
    if project_name in funding_map:
        amount = funding_map[project_name]
        total_funding += amount
        matched.append([project_name, amount])
    else:
        # Try base name match
        base_match = re.search(r'^(.+?)\s*\([^)]*\)$', project_name)
        if base_match:
            base_name = base_match.group(1)
            for fund_name in funding_map:
                if base_name == fund_name or fund_name.startswith(base_name):
                    amount = funding_map[fund_name]
                    total_funding += amount
                    matched.append([project_name, amount, fund_name])
                    break

# Create result
result = {
    "total_funding": total_funding,
    "project_count": len(matched),
    "details": matched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
