code = """import json

# funding query result is stored in a JSON file path string
path = var_call_2XlhwZg7vSd4LXq5RrSMOauD
with open(path, 'r') as f:
    funding = json.load(f)

keywords = ['FEMA', 'emergency', 'Warning Sirens', 'Warning Signs', 'Backup Power']
results = []
for row in funding:
    name = row['Project_Name']
    if any(k.lower() in name.lower() for k in keywords):
        amt = row['Amount']
        try:
            amt_int = int(amt)
        except Exception:
            amt_int = amt
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': amt_int
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_2XlhwZg7vSd4LXq5RrSMOauD': 'file_storage/call_2XlhwZg7vSd4LXq5RrSMOauD.json', 'var_call_osJUcjpCkrboRnOQc4FTywKx': 'file_storage/call_osJUcjpCkrboRnOQc4FTywKx.json'}

exec(code, env_args)
