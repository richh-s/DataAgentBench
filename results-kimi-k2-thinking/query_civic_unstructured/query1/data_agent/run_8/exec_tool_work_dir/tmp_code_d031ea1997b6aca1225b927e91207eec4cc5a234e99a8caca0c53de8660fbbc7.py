code = """import json, re

# Read data files
civic_file_path = locals()['var_functions.query_db:12']
funding_file_path = locals()['var_functions.query_db:2']

with open(civic_file_path) as f:
    civic_docs = json.load(f)
with open(funding_file_path) as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        funding_map[record['Project_Name']] = amount

# Extract design projects
projects = []
section = None

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            section = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            section = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            section = 'not_started'
        elif 'Disaster Recovery Projects' in line:
            section = 'disaster'
        elif line and section == 'design' and len(line) > 10:
            if not line.startswith('(') and 'Page' not in line and 'cid:' not in line:
                lower_line = line.lower()
                if 'updates' not in lower_line and 'schedule' not in lower_line and 'project description' not in lower_line:
                    clean_name = re.sub(r'\(cid:\d+\)', '', line).strip()
                    clean_name = re.sub(r'^[\W_]+', '', clean_name).strip()
                    if len(clean_name) > 5:
                        projects.append(clean_name)

# Find matches
design_count = 0
matched_projects = set()

for proj in projects:
    for fund_name in funding_map:
        if proj == fund_name or proj in fund_name or fund_name in proj:
            matched_projects.add(fund_name)
            break

design_count = len(matched_projects)

result = {'count': design_count}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
