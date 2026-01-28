code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs_full = json.load(f)
else:
    civic_docs_full = locals()['var_functions.query_db:2']

funding_data = locals()['var_functions.query_db:0']
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:0']

# Find disaster-related projects from funding data
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'emergency', 'warning', 'siren']
disaster_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    if any(keyword in project_name for keyword in disaster_keywords):
        disaster_funding.append(record)

# Now check which of these projects started in 2022
# We need to extract start dates from civic documents
projects_with_dates = []

for doc in civic_docs_full:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 150:
            continue
            
        # Check if this matches any disaster project name
        for disaster_proj in disaster_funding:
            proj_name = disaster_proj['Project_Name']
            if proj_name in line or line in proj_name:
                # Look for 2022 dates in surrounding lines
                context = '\n'.join(lines[max(0, i-5):min(len(lines), i+5)])
                if '2022' in context:
                    projects_with_dates.append({
                        'project': proj_name,
                        'has_2022': True,
                        'funding': int(disaster_proj.get('Amount', 0))
                    })

print('__RESULT__')
print(json.dumps({
    'disaster_funding_total': len(disaster_funding),
    'projects_with_2022': len(projects_with_dates),
    'total_funding_2022': sum(p['funding'] for p in projects_with_dates)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}}

exec(code, env_args)
