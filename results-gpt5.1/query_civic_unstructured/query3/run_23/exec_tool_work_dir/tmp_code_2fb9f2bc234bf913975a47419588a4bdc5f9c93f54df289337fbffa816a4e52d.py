code = """import json, re, pandas as pd

# Load full funding results
path_funding = var_call_m3zT9ckTc4dnfsPhpnWOfjz7
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter projects with 'emergency' or 'FEMA' in name (case-insensitive)
pattern = re.compile(r'(emergency|FEMA)', re.IGNORECASE)
rows = []
for rec in funding:
    name = rec.get('Project_Name','')
    if pattern.search(name):
        rows.append({
            'Project_Name': name,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': rec.get('Amount')
        })

result = json.dumps(rows)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_m3zT9ckTc4dnfsPhpnWOfjz7': 'file_storage/call_m3zT9ckTc4dnfsPhpnWOfjz7.json', 'var_call_T8o8E8AyPhtLQAPKLUJUCxZd': 'file_storage/call_T8o8E8AyPhtLQAPKLUJUCxZd.json'}

exec(code, env_args)
