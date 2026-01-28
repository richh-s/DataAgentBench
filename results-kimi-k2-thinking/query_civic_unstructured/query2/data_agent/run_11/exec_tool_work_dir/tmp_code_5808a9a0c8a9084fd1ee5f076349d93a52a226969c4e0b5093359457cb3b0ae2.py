code = """import json, re

# Get the data from storage variables
civic_docs_data = var_functions.query_db:5
funding_data = var_functions.query_db:6

# Load civic documents (handle file path)
if isinstance(civic_docs_data, str):
    with open(civic_docs_data) as f:
        civic_docs_data = json.load(f)

# Load funding data  
if isinstance(funding_data, str):
    with open(funding_data) as f:
        funding_data = json.load(f)

park_projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text','')
    # Check if this document mentions parks, completion, and 2022
    if 'Park' in text and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for project names containing Park
            if 'Park' in line and len(line) > 5 and not line.startswith('('):
                # Skip header lines
                if any(word in line for word in ['Subject', 'Page', 'Item', 'To:', 'From:', 'Date:']):
                    continue
                # Check following lines for completion date
                next_text = ' '.join(lines[i:i+15])
                if 'completed' in next_text.lower() and '2022' in next_text:
                    park_projects_2022.append(line)

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))

# Find funding for these projects
funding_matches = []
total_funding = 0

for project_name in unique_park_projects:
    for fund_rec in funding_data:
        fund_name = fund_rec.get('Project_Name','')
        # Fuzzy matching for project names
        if project_name.lower() == fund_name.lower():
            amount = int(fund_rec.get('Amount',0))
            total_funding += amount
            funding_matches.append({'project': project_name, 'funding_record': fund_name, 'amount': amount})

result = {
    'park_projects_2022': unique_park_projects,
    'project_count': len(unique_park_projects),
    'total_funding': total_funding,
    'funding_details': funding_matches
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
