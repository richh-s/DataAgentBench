code = """import json, re

# Load funding records
funding = var_call_gXvh1LCEiC0knRxFJcXOdf3B

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

result_json = json.dumps(results)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_gXvh1LCEiC0knRxFJcXOdf3B': 'file_storage/call_gXvh1LCEiC0knRxFJcXOdf3B.json', 'var_call_ofn4Zqv5AjlDqCqFA64hFi50': 'file_storage/call_ofn4Zqv5AjlDqCqFA64hFi50.json'}

exec(code, env_args)
