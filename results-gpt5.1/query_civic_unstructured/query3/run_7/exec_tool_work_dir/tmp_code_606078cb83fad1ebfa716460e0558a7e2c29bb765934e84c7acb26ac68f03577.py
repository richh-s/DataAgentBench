code = """import json

funding_path = var_call_RfUtNdCUoBUlO1cvij5epLEH
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Filter projects whose names contain 'FEMA' or 'emergency' (case-insensitive)
results = []
for row in funding_data:
    name = row.get('Project_Name', '') or ''
    if 'fema' in name.lower() or 'emergency' in name.lower():
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount')
        })

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_RfUtNdCUoBUlO1cvij5epLEH': 'file_storage/call_RfUtNdCUoBUlO1cvij5epLEH.json', 'var_call_uHrGeibWbUtBVIMt3AUwAcYT': 'file_storage/call_uHrGeibWbUtBVIMt3AUwAcYT.json'}

exec(code, env_args)
