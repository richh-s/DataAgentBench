code = """import re, json
from pathlib import Path

# Load full funding data
funding_path = var_call_Sn3mmac4DbLskVMWgk3VDDbO
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding projects whose names suggest FEMA/emergency
pattern = re.compile(r'(FEMA|emergency|Warning Sirens|Warning Signs)', re.IGNORECASE)
relevant = []
for row in funding:
    name = row.get('Project_Name', '') or ''
    if pattern.search(name):
        relevant.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': row.get('Amount')
        })

result = json.dumps(relevant, indent=2)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_Sn3mmac4DbLskVMWgk3VDDbO': 'file_storage/call_Sn3mmac4DbLskVMWgk3VDDbO.json', 'var_call_E9jICBC66anPT0hIXjopRtIB': 'file_storage/call_E9jICBC66anPT0hIXjopRtIB.json'}

exec(code, env_args)
