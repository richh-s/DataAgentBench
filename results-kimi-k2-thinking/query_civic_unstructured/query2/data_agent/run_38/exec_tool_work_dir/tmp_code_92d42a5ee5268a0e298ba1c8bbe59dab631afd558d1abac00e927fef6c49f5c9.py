code = """import json

# Load data
civic_docs_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup
funding_lookup = {}
for record in funding_data:
    name = record['Project_Name'].lower()
    amount = int(record['Amount'])
    funding_lookup[name] = amount

# Extract park projects completed 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    orig_lines = doc.get('text', '').split('\n')
    
    # Flag: contains completion in 2022 and park
    if 'completed' in text and '2022' in text and 'park' in text:
        for line in orig_lines:
            line_lower = line.lower()
            if 'park' in line_lower:
                has_keywords = any(k in line_lower for k in ['project', 'repairs', 'improvements'])
                if has_keywords and len(line) < 150:
                    park_projects.append(line.strip())

# Unique projects
unique_projects = list(set(park_projects))

# Match funding
total = 0
matches = []

for proj in unique_projects:
    proj_key = proj.lower()
    if proj_key in funding_lookup:
        total += funding_lookup[proj_key]
        matches.append(proj)

# Final result
result = {
    'total_funding': total,
    'matched_projects': matches,
    'park_candidates': unique_projects[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_count': 500, 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}}

exec(code, env_args)
