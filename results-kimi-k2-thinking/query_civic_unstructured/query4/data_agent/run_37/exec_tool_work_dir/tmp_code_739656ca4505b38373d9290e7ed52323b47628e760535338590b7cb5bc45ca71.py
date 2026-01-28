code = """import json, os

# Load funding data
funding_file = "/tmp/tmp4n6h1h4h.json"
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = []

print('Funding recs:', len(funding_data))

# Get civic docs file path
civic_file = "/tmp/tmp4p5a1c3b.json"
if os.path.exists(civic_file):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)
else:
    # Try to find from environment
    import glob
    tmp_files = glob.glob("/tmp/*.json")
    civic_docs = []
    for f in tmp_files:
        if '4p5' in f:
            with open(f, 'r') as file:
                civic_docs = json.load(file)
            break

print('Civic docs:', len(civic_docs))

# Extract projects
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if '2022' in line and len(line) > 10:
            if not line.startswith('(') and not any(x in line for x in ['Page', 'RECOMMENDED', 'DISCUSSION']):
                # Check for Spring
                if 'Spring' in line:
                    projects.append(line)

# Count unique
unique = list(set(projects))
print('Spring 2022 projects:', len(unique))

# Match funding
matched = []
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    for proj in unique:
        if fund_name in proj.lower():
            matched.append(int(fund.get('Amount', 0)))
            break

print('Funding matches:', len(matched))
print('Total funding:', sum(matched))

result = {'projects':len(unique), 'funding': sum(matched), 'matches': len(matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'status': 'checked'}, 'var_functions.execute_python:36': {'checked': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'count': '500', 'total_funding': '28094000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
