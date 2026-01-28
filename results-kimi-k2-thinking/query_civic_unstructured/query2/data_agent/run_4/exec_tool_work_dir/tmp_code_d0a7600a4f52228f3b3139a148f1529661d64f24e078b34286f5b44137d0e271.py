code = """import json
import re

# Load the civic documents data
civic_docs = locals()['var_functions.query_db:2']
funding_data = locals()['var_functions.query_db:6']

# Check if data is file path or actual data
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Convert amounts to integers
for record in funding_data:
    record['Amount'] = int(record['Amount'])

# Find park-related projects completed in 2022
park_completed_2022 = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check for 2022 completion
        if ('2022' in line and 
            ('completed' in line.lower() or 'construction was completed' in line.lower())):
            
            # Look back for project name (usually up to 5 lines before)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                
                # Skip empty or obviously not project names
                if (not prev_line or 
                    prev_line.startswith('(') or 
                    len(prev_line) > 100 or
                    prev_line.startswith('Page') or
                    'cid:' in prev_line):
                    continue
                
                # Check if park-related
                park_terms = ['park', 'playground', 'walkway', 'green street', 'bluffs', 
                             'shade structure', 'arbor', 'bench', 'workout', 'skate park']
                if any(term in prev_line.lower() for term in park_terms):
                    project_name = prev_line
                    # Clean name
                    project_name = re.sub(r'\(cid:\d+\)', '', project_name).strip()
                    
                    park_completed_2022.append({
                        'name': project_name,
                        'completion_line': line,
                        'doc_id': doc['_id']
                    })
                    break

# Match with funding data
funding_matches = []

for park_project in park_completed_2022:
    park_name = park_project['name'].lower()
    
    for funding in funding_data:
        fund_name = funding['Project_Name'].lower()
        
        # Check if names match (one contains the other)
        if (park_name in fund_name or fund_name in park_name):
            funding_matches.append({
                'project': park_project['name'],
                'funding_name': funding['Project_Name'],
                'amount': funding['Amount'],
                'source': funding['Funding_Source']
            })
            break

# Calculate total
total = sum([f['amount'] for f in funding_matches])

# Format results
result = {
    'total_funding': total,
    'matching_projects': len(funding_matches),
    'details': funding_matches
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}}

exec(code, env_args)
