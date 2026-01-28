code = """import json

res_path = var_call_dloGuUYONRqxgiFxJkj2ybgZ
with open(res_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter for projects with 'fema' or 'emergency' or 'outdoor warning' or 'sirens' in project name
keywords = ['fema', 'emergency', 'outdoor warning', 'sirens']
filtered = [
    {
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': r['Amount'],
        'Status': r['Status']
    }
    for r in data if any(k in r['Project_Name'].lower() for k in keywords)
]

# Prepare output lines
lines = []
lines.append('Project Name | Funding Source | Amount | Status')
for r in filtered:
    lines.append("{} | {} | ${:,} | {}".format(r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status']))

answer = '\n'.join(lines)

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json', 'var_call_LjDjToKzxMRjHcG573Em5PnB': 'file_storage/call_LjDjToKzxMRjHcG573Em5PnB.json', 'var_call_dloGuUYONRqxgiFxJkj2ybgZ': 'file_storage/call_dloGuUYONRqxgiFxJkj2ybgZ.json'}

exec(code, env_args)
