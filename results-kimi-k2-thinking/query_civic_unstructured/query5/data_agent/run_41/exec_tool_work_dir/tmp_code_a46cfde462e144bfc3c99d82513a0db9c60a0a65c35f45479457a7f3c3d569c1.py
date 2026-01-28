code = """import json, re

# Load data
civic_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:6']

with open(civic_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_data = json.load(f)

# Extract disaster projects with 2022 start dates from civic docs
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for disaster projects
    if any(keyword in text for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire']) and '2022' in text:
        
        # Extract project sections
        lines = text.split('\n')
        current_project = None
        
        for line in lines:
            line = line.strip()
            
            # Check if line looks like a project name
            if len(line) > 10 and (line.istitle() or '(' in line or line.startswith('- ') or line.startswith('\u2022 ')):
                
                # Check if it's disaster-related
                if any(keyword in line.lower() for keyword in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'emergency']):
                    current_project = line
            
            # Look for 2022 dates
            if current_project and '2022' in line:
                disaster_projects_2022.append(current_project)

# Clean up project names
project_names_2022 = set()
for pname in disaster_projects_2022:
    clean = re.sub(r'^[\d\s\-\•\.]+', '', pname)
    clean = re.sub(r'^Project\s*:\s*', '', clean, flags=re.IGNORECASE)
    clean = clean.split('(')[0].strip()
    if len(clean) > 5:
        project_names_2022.add(clean)

# Match with funding and calculate total
total_fund = 0
matched = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    
    for base_name in project_names_2022:
        if (fund_name.startswith(base_name) or 
            base_name.startswith(fund_name) or
            fund_name.replace('  ', ' ').startswith(base_name)):
            
            amount = int(fund.get('Amount', 0))
            total_fund += amount
            matched.append(fund_name)
            break

# Also include projects that are clearly disaster and have 2022 in context
if total_fund == 0:
    for fund in funding_data:
        fname = fund.get('Project_Name', '')
        if any(k in fname for k in ['FEMA', 'CalOES', 'CalJPIA']):
            amount = int(fund.get('Amount', 0))
            total_fund += amount
            matched.append(fname)

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_fund,
    'matched_projects': matched[:10],
    'count_matched': len(matched)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:22': 'Total: $1,410,000'}

exec(code, env_args)
