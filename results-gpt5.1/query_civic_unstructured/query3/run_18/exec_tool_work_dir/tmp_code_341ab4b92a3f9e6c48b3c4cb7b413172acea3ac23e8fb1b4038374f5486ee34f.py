code = """import json
from pathlib import Path

funding_path = var_call_n6ommqSKhmdsHQosAoMxF6QZ
with open(funding_path, 'r') as f:
    funding = json.load(f)

civic_path = var_call_ueaVZBkIvXcJ4dG80zWUsMVM
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

text_combined = "\n".join(doc['text'] for doc in civic_docs)
lines = [l.strip() for l in text_combined.split('\n') if l.strip()]
project_names = set()
for line in lines:
    low = line.lower()
    if ('emergency' in low) or ('fema' in low):
        project_names.add(line)

for row in funding:
    name = row['Project_Name']
    low = name.lower()
    if ('fema' in low) or ('emergency' in low):
        project_names.add(name)

results = []
for row in funding:
    name = row['Project_Name']
    low = name.lower()
    if (name in project_names) or ('fema' in low) or ('emergency' in low):
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': None
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_n6ommqSKhmdsHQosAoMxF6QZ': 'file_storage/call_n6ommqSKhmdsHQosAoMxF6QZ.json', 'var_call_ueaVZBkIvXcJ4dG80zWUsMVM': 'file_storage/call_ueaVZBkIvXcJ4dG80zWUsMVM.json'}

exec(code, env_args)
