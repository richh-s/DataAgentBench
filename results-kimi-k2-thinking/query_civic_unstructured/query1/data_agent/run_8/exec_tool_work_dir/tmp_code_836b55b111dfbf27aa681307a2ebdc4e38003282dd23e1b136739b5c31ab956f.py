code = """import json, re

civic_file = locals()['var_functions.query_db:12']
funding_file = locals()['var_functions.query_db:2']

with open(civic_file) as f:
    civic_docs = json.load(f)
with open(funding_file) as f:
    funding_data = json.load(f)

# Create funding map
funding_map = {}
for r in funding_data:
    amount = int(r['Amount'])
    if amount > 50000:
        funding_map[r['Project_Name']] = amount

# Extract design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    in_design_section = False
    for line in text.split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif any(x in line for x in ['Construction)', 'Not Started)']):
            in_design_section = False
        elif in_design_section and len(line) > 10:
            if not line.startswith('(') and 'Page' not in line:
                clean = re.sub(r'\(cid:\d+\)', '', line).strip()
                if len(clean) > 5 and 'updates' not in clean.lower():
                    design_projects.append(clean)

# Match with funding
matches = set()
for proj in design_projects:
    for fund_name in funding_map:
        if proj == fund_name or proj in fund_name or fund_name in proj:
            matches.add(fund_name)

result = dict(count=len(matches))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
