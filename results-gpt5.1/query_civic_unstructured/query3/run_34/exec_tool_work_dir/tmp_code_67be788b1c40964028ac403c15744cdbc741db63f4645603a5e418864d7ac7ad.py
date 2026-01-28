code = """import json, re

funding = var_call_2XlhwZg7vSd4LXq5RrSMOauD

# Filter funding projects whose names suggest FEMA/emergency relevance
keywords = ['FEMA', 'emergency', 'Warning Sirens', 'Warning Signs', 'Backup Power']
results = []
for row in funding:
    name = row['Project_Name']
    if any(k.lower() in name.lower() for k in keywords):
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount']
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_2XlhwZg7vSd4LXq5RrSMOauD': 'file_storage/call_2XlhwZg7vSd4LXq5RrSMOauD.json', 'var_call_osJUcjpCkrboRnOQc4FTywKx': 'file_storage/call_osJUcjpCkrboRnOQc4FTywKx.json'}

exec(code, env_args)
