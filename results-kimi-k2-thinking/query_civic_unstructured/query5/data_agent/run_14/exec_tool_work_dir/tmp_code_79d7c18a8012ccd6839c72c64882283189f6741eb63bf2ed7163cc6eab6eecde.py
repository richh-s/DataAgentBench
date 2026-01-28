code = """import json
import re

# Load data
funding_path = locals()['var_functions.query_db:10']
docs_path = locals()['var_functions.query_db:2']

with open(funding_path) as f:
    funding_records = json.load(f)

with open(docs_path) as f:
    civic_docs = json.load(f)

# Convert amounts to integers
for record in funding_records:
    record['Amount'] = int(record['Amount'])

# Function to extract disaster projects with 2022 start dates
def extract_disaster_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for disaster project indicators in project names
        if '(FEMA Project)' in line or '(CalOES Project)' in line or '(CalJPIA Project)' in line:
            project_name = line
            
            # Look for 2022 in surrounding context (start dates)
            has_2022_start = False
            context_window = lines[max(0, i-10):min(len(lines), i+20)]
            
            for context_line in context_window:
                if '2022' in context_line:
                    # Check if this is a start/advertise line
                    if any(word in context_line.lower() for word in ['begin', 'start', 'advertise', 'complete design', 'spring', 'summer', 'fall', 'winter']):
                        has_2022_start = True
                        break
            
            if has_2022_start:
                projects.append({
                    'name': project_name,
                    'type': 'disaster',
                    'year': '2022'
                })
    
    return projects

# Extract disaster projects from all documents
disaster_projects_2022 = []
for doc in civic_docs:
    projects = extract_disaster_projects(doc['text'])
    disaster_projects_2022.extend(projects)

# Get unique disaster project names
disaster_project_names = list(set(p['name'] for p in disaster_projects_2022))

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_found': len(disaster_project_names),
    'project_names': disaster_project_names
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:24': {'fund_count': 500, 'doc_count': 5}}

exec(code, env_args)
