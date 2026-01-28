code = """import json
import re

# Get civic documents data from storage
civic_docs = var_functions.query_db:5
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Get funding data from storage
funding = var_functions.query_db:6
if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    
    # Look for park projects completed in 2022
    if 'park' in text and '2022' in text and 'completed' in text:
        lines = doc.get('text', '').split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if 'park' in line.lower():
                # Check if this is likely a project name
                if len(line) > 5 and not line.startswith('(') and not any(x in line for x in ['subject', 'page', 'item', 'to:', 'from:']):
                    # Look ahead for status and date
                    next_lines = '\n'.join(lines[i+1:min(i+10, len(lines))])
                    if 'completed' in next_lines.lower() and '2022' in next_lines.lower():
                        park_projects_2022.append(line)

print('__RESULT__:')
print(json.dumps({
    'projects': list(set(park_projects_2022)),
    'count': len(set(park_projects_2022))
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
