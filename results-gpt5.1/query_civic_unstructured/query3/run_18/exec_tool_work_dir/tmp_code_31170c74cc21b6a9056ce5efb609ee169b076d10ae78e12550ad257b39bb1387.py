code = """import re, json
from pathlib import Path

# Load full results if needed
funding_path = var_call_n6ommqSKhmdsHQosAoMxF6QZ
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = var_call_ueaVZBkIvXcJ4dG80zWUsMVM
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Build a set of emergency/FEMA-related project names from civic docs using simple pattern matching
text_combined = "\n".join(doc['text'] for doc in civic_docs)

# Candidate project name patterns: lines that likely denote project titles
lines = [l.strip() for l in text_combined.split('\n') if l.strip()]
project_names = set()
for line in lines:
    if any(k in line.lower() for k in ['emergency', 'fema']):
        project_names.add(line)

# Also include known FEMA-style project names from funding table itself
for row in funding:
    name = row['Project_Name']
    if ('fema' in name.lower()) or ('emergency' in name.lower()):
        project_names.add(name)

# Now filter funding to only those projects whose name is in our emergency/FEMA-related set or clearly emergency
results = []
for row in funding:
    name = row['Project_Name']
    if name in project_names or 'fema' in name.lower() or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': None  # status not clearly parseable from given snippet for each project
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_n6ommqSKhmdsHQosAoMxF6QZ': 'file_storage/call_n6ommqSKhmdsHQosAoMxF6QZ.json', 'var_call_ueaVZBkIvXcJ4dG80zWUsMVM': 'file_storage/call_ueaVZBkIvXcJ4dG80zWUsMVM.json'}

exec(code, env_args)
