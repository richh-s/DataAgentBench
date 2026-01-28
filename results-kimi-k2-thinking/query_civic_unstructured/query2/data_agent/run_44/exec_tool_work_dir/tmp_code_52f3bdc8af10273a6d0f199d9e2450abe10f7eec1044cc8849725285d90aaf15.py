code = """import json
import re

civic_docs = json.load(open(locals()['var_functions.query_db:0'], 'r'))
funding_data = json.load(open(locals()['var_functions.query_db:1'], 'r'))

for f in funding_data:
    f['Amount'] = int(f['Amount'])

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10 or len(line) > 150:
            continue
        
        skip_prefixes = ['(', 'Page', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']
        if any(line.startswith(prefix) for prefix in skip_prefixes):
            continue
        
        skip_phrases = ['Status Report', 'City Council', 'Public Works Commission', 'Capital Improvement Projects', 'Disaster Recovery Projects']
        if any(phrase in line for phrase in skip_phrases):
            continue
        
        if not (line[0].isupper() or line[0].isdigit()):
            continue
        
        project_name = line
        is_park = 'park' in project_name.lower()
        completed_2022 = False
        
        for j in range(i+1, min(i+15, len(lines))):
            next_line = lines[j]
            if 'completed' in next_line.lower() and '2022' in next_line:
                completed_2022 = True
            if 'park' in next_line.lower():
                is_park = True
        
        if completed_2022 and is_park and project_name not in park_projects_2022:
            park_projects_2022.append(project_name)

print('__RESULT__:')
print(json.dumps({'count': len(park_projects_2022), 'projects': park_projects_2022}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:6': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding_keys': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
