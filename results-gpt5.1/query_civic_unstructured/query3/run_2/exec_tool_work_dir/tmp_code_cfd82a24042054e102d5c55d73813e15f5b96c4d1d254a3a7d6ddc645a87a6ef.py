code = """import json, re
from pathlib import Path

# Load full funding data
path_funding = Path(var_call_GI0M1Y9BNBzrfTCt4buuDPeU)
with path_funding.open() as f:
    funding = json.load(f)

# Filter projects whose names contain 'emergency' or 'FEMA' (case-insensitive)
results = []
for row in funding:
    name = row.get('Project_Name', '') or ''
    if re.search(r'(emergency|FEMA)', name, re.IGNORECASE):
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount')) if row.get('Amount') not in (None, '') else None
        })

out = json.dumps(results, ensure_ascii=False)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_GI0M1Y9BNBzrfTCt4buuDPeU': 'file_storage/call_GI0M1Y9BNBzrfTCt4buuDPeU.json', 'var_call_eBbhtWLFSYZo73clpDFXdgGY': 'file_storage/call_eBbhtWLFSYZo73clpDFXdgGY.json'}

exec(code, env_args)
