code = """import json
# Read the full execute_python output file
with open(var_call_dBcDFEUiEH5kcvW7dmjgYcG5, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter entries that are related to FEMA or emergency (by project name or funding source mentioning FEMA/Federal Assistance)
related = []
for r in data:
    pname = (r.get('Project_Name') or '').lower()
    fsrc = (r.get('Funding_Source') or '').lower()
    if 'fema' in pname or 'fema' in fsrc or 'federal assistance' in fsrc or 'emergency' in pname or 'warning' in pname or 'siren' in pname:
        related.append(r)

# Prepare concise result list
out = []
for r in related:
    out.append({
        'Project_Name': r.get('Project_Name'),
        'Funding_Source': r.get('Funding_Source'),
        'Amount': r.get('Amount'),
        'Status': r.get('Status')
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_CHWKaz9CJKOfQ2VL3FnKxhnX': 'file_storage/call_CHWKaz9CJKOfQ2VL3FnKxhnX.json', 'var_call_0EQqnWVhr6zNhR7UcxXNBDd9': 'file_storage/call_0EQqnWVhr6zNhR7UcxXNBDd9.json', 'var_call_dBcDFEUiEH5kcvW7dmjgYcG5': 'file_storage/call_dBcDFEUiEH5kcvW7dmjgYcG5.json'}

exec(code, env_args)
