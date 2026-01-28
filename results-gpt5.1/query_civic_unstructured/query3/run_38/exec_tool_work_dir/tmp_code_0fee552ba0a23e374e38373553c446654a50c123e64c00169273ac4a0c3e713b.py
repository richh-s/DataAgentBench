code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_SfnoTowQ7tH4pS0MRXasGWJg
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding projects related to 'emergency' or 'FEMA' in name (case-insensitive)
pattern = re.compile(r'(emergency|fema)', re.IGNORECASE)
relevant = [
    {
        'Project_Name': rec['Project_Name'],
        'Funding_Source': rec['Funding_Source'],
        'Amount': int(rec['Amount']) if isinstance(rec['Amount'], str) and rec['Amount'].isdigit() else rec['Amount']
    }
    for rec in funding
    if pattern.search(rec['Project_Name'])
]

result = json.dumps(relevant)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_SfnoTowQ7tH4pS0MRXasGWJg': 'file_storage/call_SfnoTowQ7tH4pS0MRXasGWJg.json', 'var_call_1CSmpPCsCa6CBzQg2rk8q1qX': 'file_storage/call_1CSmpPCsCa6CBzQg2rk8q1qX.json'}

exec(code, env_args)
