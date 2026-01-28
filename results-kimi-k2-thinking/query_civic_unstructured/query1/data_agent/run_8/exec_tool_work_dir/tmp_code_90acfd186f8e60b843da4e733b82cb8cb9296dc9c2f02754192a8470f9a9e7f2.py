code = """import json, re

# Read data files
civic_file_path = locals()['var_functions.query_db:12']
funding_file_path = locals()['var_functions.query_db:2']

with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    if int(record['Amount']) > 50000:
        funding_map[record['Project_Name']] = int(record['Amount'])

# Extract design projects
projects = []
section = None
for doc in civic_docs:
    for line in doc.get('text', '').split('\n'):
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            section = 'design'
        elif any(header in line for header in ['Construction', 'Not Started']):
            section = None
        elif line and section == 'design' and len(line) > 10:
            if not line.startswith('(') and not line.startswith('Page'):
                skip_patterns = ['updates', 'schedule', 'project description', 'revised', 'preliminary']
                if not any(pattern in line.lower() for pattern in skip_patterns):
                    clean_name = re.sub(r'\(cid:\d+\)', '', line).strip()
                    if len(clean_name) > 5:
                        projects.append(clean_name)

# Find projects with funding
matched = []
for proj in projects:
    for fund_name in funding_map:
        if proj == fund_name or proj in fund_name or fund_name in proj:
            matched.append(fund_name)
            break

unique = list(set(matched))

result = {'count': len(unique)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
