code = """import json, re

# Load funding data
path_funding = var_call_S2FyB9Hi6mksY91hNwPjctOC
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter for project names related to 'emergency' or 'FEMA'
results = []
for row in funding:
    name = row.get('Project_Name', '') or ''
    if re.search(r'emergency', name, re.IGNORECASE) or re.search(r'FEMA', name, re.IGNORECASE):
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount')
        })

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S2FyB9Hi6mksY91hNwPjctOC': 'file_storage/call_S2FyB9Hi6mksY91hNwPjctOC.json', 'var_call_s8DvN1ucz0aKxbc7Z9HovwsE': 'file_storage/call_s8DvN1ucz0aKxbc7Z9HovwsE.json'}

exec(code, env_args)
