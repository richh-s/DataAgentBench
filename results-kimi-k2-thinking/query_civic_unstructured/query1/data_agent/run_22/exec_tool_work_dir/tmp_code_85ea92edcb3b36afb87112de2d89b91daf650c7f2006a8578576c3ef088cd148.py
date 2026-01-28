code = """import json
import re

# Read the data
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_status = None
    current_type = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for section headers
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
            current_type = 'capital'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'completed'
            current_type = 'capital'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not started'
            current_type = 'capital'
        elif 'Disaster Recovery Projects' in line:
            current_type = 'disaster'
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'completed'
            elif '(Not Started)' in line:
                current_status = 'not started'
        elif current_status and current_type:
            # Skip metadata lines
            skip_words = ['Updates:', 'Project Schedule', 'Estimated Schedule', 'Project Description:', 
                         'To:', 'Prepared by:', 'Approved by:', 'RECOMMENDED ACTION', 'DISCUSSION:', 
                         'Page', 'Agenda Item', 'Subject:', 'Date prepared:', 'Meeting date:']
            should_skip = any(word in line for word in skip_words)
            
            if not should_skip and not line.startswith('(') and len(line) < 150:
                if 'Capital Improvement' not in line and 'Disaster Recovery' not in line:
                    projects.append({'Project_Name': line, 'status': current_status, 'type': current_type})

# Find capital projects with design status and funding > 50000
design_capital = [p for p in projects if p['status'] == 'design' and p['type'] == 'capital']
matches = []
seen_projects = set()

for proj in design_capital:
    for fund in funding_data:
        if int(fund['Amount']) > 50000:
            proj_lc = proj['Project_Name'].lower()
            fund_lc = fund['Project_Name'].lower()
            
            if proj_lc == fund_lc or proj_lc in fund_lc or fund_lc in proj_lc:
                if proj['Project_Name'] not in seen_projects:
                    seen_projects.add(proj['Project_Name'])
                    matches.append(proj['Project_Name'])

result = {'count': len(matches), 'projects': matches[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'total_funding_records': 276, 'total_civic_docs': 5, 'first_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount'], 'first_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
