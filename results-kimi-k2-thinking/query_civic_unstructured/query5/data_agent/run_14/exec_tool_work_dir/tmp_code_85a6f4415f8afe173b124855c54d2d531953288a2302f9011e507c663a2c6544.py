code = """import json
import re

# Load funding data
f_path = locals()['var_functions.query_db:10']
with open(f_path) as f:
    funding = json.load(f)

# Convert amounts to integers
for record in funding:
    record['Amount'] = int(record['Amount'])

# Load civic documents
p_path = locals()['var_functions.query_db:36']
with open(p_path) as f:
    docs = json.load(f)

# Helper function
def has_2022_start(line):
    return '2022' in line

# Find disaster projects
projects = set()
for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    for i,line in enumerate(lines):
        line = line.strip()
        if line and ('(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line):
            # Check for 2022 in context
            context = text[max(0, text.find(line)-200):min(len(text), text.find(line)+200)]
            if '2022' in context:
                projects.add(line)

# Map to funding
total = 0
matched = []
for proj in projects:
    base_name = proj.replace(' (FEMA Project)', '').replace(' (CalOES Project)', '').replace(' (CalJPIA Project)', '')
    for fund in funding:
        if proj in fund['Project_Name'] or fund['Project_Name'].startswith(base_name):
            total += fund['Amount']
            matched.append(fund)

# Get unique funding
unique_matched = {f['Funding_ID']: f for f in matched}.values()

# Result
result = {
    'disaster_projects': list(projects),
    'matching_funding': list(unique_matched),
    'total_amount': sum(f['Amount'] for f in unique_matched)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
