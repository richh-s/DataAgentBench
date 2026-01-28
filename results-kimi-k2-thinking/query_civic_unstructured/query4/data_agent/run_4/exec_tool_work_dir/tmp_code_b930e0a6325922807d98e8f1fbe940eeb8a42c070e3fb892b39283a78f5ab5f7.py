code = """import json

# Access the stored file paths
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:4

# Load data
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_records = json.load(f)

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if name:
        funding_lookup[name] = amount

print('Loaded data:', len(civic_docs), 'docs,', len(funding_records), 'funding records')

# Process documents
total_funding = 0
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract project names from this document
        import re
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Heuristic: project names contain keywords and reasonable length
            if any(k in line for k in ['Project', 'Improvements', 'Repairs', 'Replacement']) and \
               not line.startswith('(') and 10 < len(line) < 150:
                # Check if this project has funding
                if line in funding_lookup:
                    amt = funding_lookup[line]
                    found_projects.append({'name': line, 'funding': amt})
                    total_funding += amt
                else:
                    # Try partial match
                    for fund_name in funding_lookup:
                        if line.lower() in fund_name.lower() or fund_name.lower() in line.lower():
                            amt = funding_lookup[fund_name]
                            found_projects.append({'name': line, 'funding': amt})
                            total_funding += amt
                            break

# Remove duplicates
unique_projects = {}
for proj in found_projects:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj['funding']

final_projects = [{'name': k, 'funding': v} for k, v in unique_projects.items()]

result = {
    'spring_2022_count': len(final_projects),
    'total_funding': total_funding,
    'projects': final_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
