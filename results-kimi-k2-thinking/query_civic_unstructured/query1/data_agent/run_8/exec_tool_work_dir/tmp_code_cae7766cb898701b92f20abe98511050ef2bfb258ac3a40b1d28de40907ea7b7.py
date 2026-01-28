code = """import json, re

# Read civic documents
civic_file_path = locals()['var_functions.query_db:12']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Map project names to funding > 50000
funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[record['Project_Name']] = amount

# Extract projects from civic docs
projects = []
for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    section = None
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            section = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            section = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            section = 'not started'
        elif line and section == 'design':
            if len(line) > 15 and not line.startswith('(') and not line.startswith('Page'):
                skip = ['updates', 'schedule', 'project description', 'revised', 'preliminary', 'complete design', 'advertise']
                if not any(word in line.lower() for word in skip):
                    name = re.sub(r'\(cid:\d+\)', '', line).strip()
                    if len(name) > 5 and 'cid:' not in name:
                        proj_type = 'capital'
                        if 'FEMA' in name or 'CalOES' in name or 'CalJPIA' in name:
                            proj_type = 'disaster'
                        projects.append({'name': name, 'type': proj_type, 'status': section})

# Match design projects with funding
design_funded = []
for proj in projects:
    proj_name = proj['name']
    for fund_name, amount in funding_map.items():
        if proj_name == fund_name or proj_name in fund_name or fund_name in proj_name:
            design_funded.append({'name': fund_name, 'funding': amount})
            break

# Count unique
unique = []
seen = set()
for proj in design_funded:
    if proj['name'] not in seen:
        seen.add(proj['name'])
        unique.append(proj)

result = {'count': len(unique), 'projects': unique}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
