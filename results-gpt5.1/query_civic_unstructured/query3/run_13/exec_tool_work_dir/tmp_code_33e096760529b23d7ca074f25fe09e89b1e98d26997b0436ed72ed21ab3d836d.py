code = """import json, re
from pathlib import Path

# Load full funding data
funding_path = var_call_UvbB21fpFJslBIl0dNhm4T2q
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Filter funding records whose project names suggest emergency/FEMA context
emergency_keywords = ['emergency', 'fema']
re_emerg = re.compile('|'.join(emergency_keywords), re.I)

filtered = []
for row in funding:
    name = row.get('Project_Name','') or ''
    if re_emerg.search(name):
        filtered.append({
            'Project_Name': name,
            'Funding_Source': row.get('Funding_Source'),
            'Amount': int(row.get('Amount')) if isinstance(row.get('Amount'), str) and row.get('Amount').isdigit() else row.get('Amount')
        })

result = json.dumps(filtered, indent=2)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_UvbB21fpFJslBIl0dNhm4T2q': 'file_storage/call_UvbB21fpFJslBIl0dNhm4T2q.json', 'var_call_9RYShSkmz75VfKV8Xo6DRxEN': 'file_storage/call_9RYShSkmz75VfKV8Xo6DRxEN.json'}

exec(code, env_args)
