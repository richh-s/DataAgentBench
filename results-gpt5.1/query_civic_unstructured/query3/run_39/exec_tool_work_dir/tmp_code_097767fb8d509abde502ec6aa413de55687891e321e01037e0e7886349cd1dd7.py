code = """import json, re
from pathlib import Path

# Load full funding records
with open(var_call_mOZbtLY0mtGAXkT5cQzqZgpW, 'r') as f:
    funding = json.load(f)

# Filter funding records for project names containing 'FEMA' or 'Emergency' (case-insensitive)
results = []
for row in funding:
    name = row.get('Project_Name', '')
    if re.search(r'(fema|emergency)', name, re.IGNORECASE):
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount')) if row.get('Amount') not in (None, '') else None
        })

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_mOZbtLY0mtGAXkT5cQzqZgpW': 'file_storage/call_mOZbtLY0mtGAXkT5cQzqZgpW.json', 'var_call_MSW1elFVUuX0O5mCliKcIjbQ': 'file_storage/call_MSW1elFVUuX0O5mCliKcIjbQ.json'}

exec(code, env_args)
