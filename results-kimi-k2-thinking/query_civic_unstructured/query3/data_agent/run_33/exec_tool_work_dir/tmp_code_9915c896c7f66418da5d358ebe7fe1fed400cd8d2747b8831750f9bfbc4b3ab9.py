code = """import json
import re

civic_file = str(locals()['var_functions.query_db:0'])
funding_file = str(locals()['var_functions.query_db:5'])

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

projects = []
seen_projects = set()

# First collect all FEMA projects from funding data
for fund_record in funding_data:
    proj_name = fund_record['Project_Name']
    if 'fema' in proj_name.lower():
        projects.append({
            'Project_Name': proj_name,
            'Funding_Source': fund_record['Funding_Source'],
            'Amount': int(fund_record['Amount']),
            'Status': 'Status not available in civic docs'
        })
        seen_projects.add(proj_name.lower())

# Check civic documents for emergency/FEMA mentions
for doc in civic_docs:
    text_lines = doc['text'].split('\n')
    for line in text_lines:
        line_lower = line.lower().strip()
        if 'emergency' in line_lower or 'fema' in line_lower:
            # Clean line
            clean_line = line.strip()
            if len(clean_line) < 10:
                continue
            if clean_line.startswith('('):
                continue
            
            line_lower_key = clean_line.lower()
            if line_lower_key in seen_projects:
                continue
                
            # Find matching funding
            funding_info = None
            for f in funding_data:
                f_name = f['Project_Name']
                if clean_line in f_name or f_name in clean_line:
                    funding_info = f
                    break
            
            if funding_info:
                amount_val = int(funding_info['Amount'])
                source_val = funding_info['Funding_Source']
            else:
                amount_val = 0
                source_val = 'Unknown'
            
            projects.append({
                'Project_Name': clean_line,
                'Funding_Source': source_val,
                'Amount': amount_val,
                'Status': 'Referenced in civic documents'
            })
            seen_projects.add(line_lower_key)

# Sort by amount
projects.sort(key=lambda x: x['Amount'], reverse=True)

output = {'projects': projects}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
