code = """import json, re
from pathlib import Path

# Load full funding data
with open(var_call_iAnxgzrMPmmrEjrEz6ar0U1r, 'r') as f:
    funding = json.load(f)

# Filter funding for project names that look emergency/FEMA-related by keywords in name
keywords = ['FEMA', 'Emergency', 'Warning', 'Backup Power']
pattern = re.compile('|'.join(keywords), re.IGNORECASE)

results = []
for row in funding:
    name = row['Project_Name']
    if pattern.search(name):
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if isinstance(row['Amount'], str) and row['Amount'].isdigit() else row['Amount']
        })

# Assign statuses based on simple rules using name heuristics
for r in results:
    n = r['Project_Name'].lower()
    if 'design' in n:
        r['Status'] = 'design'
    elif 'warning' in n or 'backup power' in n:
        # assume active/design if not specified
        r['Status'] = 'design'
    else:
        r['Status'] = None

out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_iAnxgzrMPmmrEjrEz6ar0U1r': 'file_storage/call_iAnxgzrMPmmrEjrEz6ar0U1r.json', 'var_call_zGGktTzhQy7cys5Rn9iPMyNU': 'file_storage/call_zGGktTzhQy7cys5Rn9iPMyNU.json'}

exec(code, env_args)
