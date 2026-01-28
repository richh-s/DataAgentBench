code = """import json

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Filter for funding > $50,000
high_funding = []
for record in funding_data:
    try:
        amount = int(record.get('Amount', 0))
        if amount > 50000:
            high_funding.append(record)
    except:
        pass

print('Funding records over $50,000:', len(high_funding))

# Load civic docs
civic_file = var_functions.query_db:16
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract capital projects with design status
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    in_design_section = False
    for i, line in enumerate(lines):
        lower_line = line.lower().strip()
        
        if 'capital improvement projects (design)' in lower_line:
            in_design_section = True
            continue
        
        if in_design_section:
            if any(marker in lower_line for marker in ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']):
                break
            
            clean_line = line.strip()
            if not clean_line or len(clean_line) < 5:
                continue
            
            skip = ['updates:', 'project schedule', 'subject:', 'recommended action', 'date prepared', 'cid:', '•']
            if any(s in lower_line for s in skip):
                continue
            
            if i + 1 < len(lines):
                next_line = lines[i + 1].lower().strip()
                if 'updates:' in next_line or 'project schedule' in next_line or next_line.startswith('('):
                    project_name = clean_line.lstrip('0123456789.-• ')
                    if len(project_name) > 5 and 'capital improvement' not in project_name.lower():
                        capital_design_projects.append(project_name)

print('Capital design projects:', len(capital_design_projects))

# Match with funding
matches = []
matched_names = set()

for design_project in capital_design_projects:
    design_lower = design_project.lower()
    
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        
        if (design_lower in fund_name or fund_name in design_lower or design_lower == fund_name):
            if design_project not in matched_names:
                matches.append({
                    'project': design_project,
                    'funding': fund['Project_Name'],
                    'amount': int(fund['Amount'])
                })
                matched_names.add(design_project)
            break

print('Matching projects with funding > $50,000:', len(matches))

result = {'count': len(matches)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
