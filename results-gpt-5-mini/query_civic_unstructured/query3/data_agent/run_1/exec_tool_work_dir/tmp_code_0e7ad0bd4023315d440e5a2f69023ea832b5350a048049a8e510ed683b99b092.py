code = """import json

# Load the processed results from previous execute_python (file path provided in storage)
with open(var_call_9fIxkW02rL6UZmM0930dYUCZ, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter for projects related to 'fema' or 'emergency'
filtered = []
for r in data:
    pname = r.get('Project_Name','') or ''
    fsource = r.get('Funding_Source','') or ''
    if ('fema' in pname.lower()) or ('fema' in fsource.lower()) or ('emergency' in pname.lower()) or ('emergency' in fsource.lower()):
        # Ensure Amount is int or convert
        amount = r.get('Amount')
        try:
            amount = int(amount)
        except Exception:
            try:
                amount = int(float(amount))
            except Exception:
                amount = None
        filtered.append({
            'Project_Name': pname,
            'Funding_Source': fsource,
            'Amount': amount,
            'Status': r.get('Status')
        })

# Deduplicate by Project_Name
seen = set()
unique = []
for item in filtered:
    if item['Project_Name'] not in seen:
        seen.add(item['Project_Name'])
        unique.append(item)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_F5LZc7pWGPHZcH3cfkJsTRH0': 'file_storage/call_F5LZc7pWGPHZcH3cfkJsTRH0.json', 'var_call_IBkE6sETgIJUK7RBuQYNU2IP': 'file_storage/call_IBkE6sETgIJUK7RBuQYNU2IP.json', 'var_call_9fIxkW02rL6UZmM0930dYUCZ': 'file_storage/call_9fIxkW02rL6UZmM0930dYUCZ.json'}

exec(code, env_args)
