code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_e4infTYqW3v45GeqPqcO5Qht
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding records for project names containing 'FEMA' or 'emergency' (case-insensitive)
pattern = re.compile(r'(fema|emergency)', re.IGNORECASE)
relevant = [
    {
        'Project_Name': r['Project_Name'],
        'Funding_Source': r['Funding_Source'],
        'Amount': int(r['Amount']) if isinstance(r['Amount'], str) and r['Amount'].isdigit() else r['Amount']
    }
    for r in funding
    if pattern.search(r['Project_Name'])
]

result = json.dumps(relevant)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_e4infTYqW3v45GeqPqcO5Qht': 'file_storage/call_e4infTYqW3v45GeqPqcO5Qht.json', 'var_call_SkfmcdJsSSpBZsStMnVSbQcj': 'file_storage/call_SkfmcdJsSSpBZsStMnVSbQcj.json'}

exec(code, env_args)
