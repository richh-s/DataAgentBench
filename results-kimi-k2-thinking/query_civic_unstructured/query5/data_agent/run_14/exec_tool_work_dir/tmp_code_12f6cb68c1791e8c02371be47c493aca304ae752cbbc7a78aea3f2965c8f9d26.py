code = """import json
import re

funding_path = locals()['var_functions.query_db:10']
docs_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding_records = json.load(f)

with open(docs_path) as f:
    civic_docs = json.load(f)

for record in funding_records:
    record['Amount'] = int(record['Amount'])

disaster_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        if '(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line:
            project_name = line.strip()
            
            has_2022_start = False
            start_window = max(0, i - 10)
            end_window = min(len(lines), i + 20)
            
            for j in range(start_window, end_window):
                context_line = lines[j]
                if '2022' in context_line:
                    lower_ctx = context_line.lower()
                    keywords = ['begin', 'start', 'advertise', 'complete design', 'spring', 'summer', 'fall', 'winter']
                    if any(kw in lower_ctx for kw in keywords):
                        has_2022_start = True
                        break
            
            if has_2022_start:
                disaster_projects_2022.add(project_name)

result = {
    'disaster_projects_found': len(disaster_projects_2022),
    'projects': list(disaster_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}}

exec(code, env_args)
