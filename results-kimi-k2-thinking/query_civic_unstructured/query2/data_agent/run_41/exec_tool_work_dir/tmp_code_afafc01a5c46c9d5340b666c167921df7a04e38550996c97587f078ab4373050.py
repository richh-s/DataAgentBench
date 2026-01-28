code = """import json

# Load the data files
civic_docs_path = var_functions.query_db:2
funding_path = var_functions.query_db:5

# Load civic documents
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

# Load funding data
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding = json.load(f)
else:
    funding = funding_path

# Simple search for park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'complete' in text.lower():
        # Look for park-related terms near completion mentions
        if ('park' in text.lower() or 'walkway' in text.lower() or 'shade' in text.lower()):
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) > 10 and not line.startswith('Public Works'):
                    if any(word in line.lower() for word in ['project', 'improvements', 'repairs']):
                        # Try to find completion info
                        line_idx = lines.index(line)
                        for j in range(line_idx+1, min(line_idx+8, len(lines))):
                            if '2022' in lines[j] and 'complete' in lines[j].lower():
                                if line not in park_projects:
                                    park_projects.append(line)
                                break

# Remove duplicates
unique_projects = list(dict.fromkeys(park_projects))

# Match with funding
total_fund = 0
matches = []

for proj in unique_projects:
    for fund in funding:
        fname = fund['Project_Name']
        amount = int(fund['Amount'])
        if proj == fname or proj in fname or fname in proj:
            total_fund += amount
            matches.append({'project': proj, 'funding': fname, 'amount': amount})
            break

result = {'total_funding': total_fund, 'project_matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
