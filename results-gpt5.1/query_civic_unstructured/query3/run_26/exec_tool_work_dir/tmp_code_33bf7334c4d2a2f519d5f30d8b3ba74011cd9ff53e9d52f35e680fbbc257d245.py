code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_70FqoHdzlJCDlv4ZzgcPnCST
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter projects related to 'emergency' or 'FEMA' by name keywords
results = []
for row in funding:
    name = row.get('Project_Name', '') or ''
    if re.search(r'emergency', name, re.IGNORECASE) or re.search(r'FEMA', name, re.IGNORECASE):
        results.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount')) if isinstance(row.get('Amount'), str) and row.get('Amount').isdigit() else row.get('Amount')
        })

# We don't actually have structured status in funding DB; infer disaster-type FEMA/emergency projects as 'disaster' type without status
# Since the question asks for status, but it's only in civic docs and not structured here, we'll omit status or set to null.
for r in results:
    r['Status'] = None

out = json.dumps(results, indent=2)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_70FqoHdzlJCDlv4ZzgcPnCST': 'file_storage/call_70FqoHdzlJCDlv4ZzgcPnCST.json', 'var_call_N3eSttViyZlUKjL4q0XlwCs6': 'file_storage/call_N3eSttViyZlUKjL4q0XlwCs6.json'}

exec(code, env_args)
