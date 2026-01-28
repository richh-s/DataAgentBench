code = """import json, re

civic_file = locals()['var_functions.query_db:12']
funding_file = locals()['var_functions.query_db:2']

with open(civic_file) as f:
    civic_docs = json.load(f)
with open(funding_file) as f:
    funding_data = json.load(f)

funding_map = {}
for r in funding_data:
    if int(r['Amount']) > 50000:
        funding_map[r['Project_Name']] = int(r['Amount'])

projects = []
s = None

for doc in civic_docs:
    for line in doc['text'].split('\n'):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            s = 'd'
        elif 'Capital Improvement Projects (Construction)' in line:
            s = 'c'
        elif 'Capital Improvement Projects (Not Started)' in line:
            s = 'n'
        elif s == 'd' and len(line) > 15:
            if not line.startswith('(') and 'Page' not in line and 'cid:' not in line:
                l = line.lower()
                if 'updates' not in l and 'schedule' not in l and 'description' not in l:
                    name = re.sub(r'\(cid:\d+\)', '', line).strip()
                    if len(name) > 5:
                        projects.append(name)

matched = set()
for p in projects:
    for f in funding_map:
        if p == f or p in f or f in p:
            matched.add(f)
            break

print('__RESULT__:')
print(json.dumps({'count': len(matched)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 276, 'funding_sample': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
