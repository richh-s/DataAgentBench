code = """import json, re
from pathlib import Path

# Load full funding data
path_funding = var_call_3ChKAzAHBDYi8UKl92fz4EDA
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter funding records where project name suggests emergency/FEMA relevance
pattern = re.compile(r'(emergency|FEMA)', re.IGNORECASE)
results = []
for row in funding:
    name = row.get('Project_Name', '')
    if pattern.search(name):
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount')) if row.get('Amount') not in (None, '') else None
        })

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_3ChKAzAHBDYi8UKl92fz4EDA': 'file_storage/call_3ChKAzAHBDYi8UKl92fz4EDA.json', 'var_call_e0JXqJeNYYPgoLyojo82MVzw': 'file_storage/call_e0JXqJeNYYPgoLyojo82MVzw.json'}

exec(code, env_args)
