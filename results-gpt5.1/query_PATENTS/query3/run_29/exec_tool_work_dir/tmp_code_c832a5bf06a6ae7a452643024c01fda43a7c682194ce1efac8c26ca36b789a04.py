code = """import json, re, pandas as pd, os

path = var_call_JuX5KYqIN2KYQuSBeJTNhmMD
with open(path, 'r') as f:
    records = json.load(f)

# Extract publication numbers from Patents_info
pub_pattern = re.compile(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[AB][0-9]?)')
assignee_pattern = re.compile(r'assignee_harmonized: ([^,;]+)')

rows = []
for r in records:
    pi = r.get('Patents_info','')
    m = pub_pattern.search(pi)
    pubnum = m.group(1) if m else None
    am = assignee_pattern.search(pi)
    assignee = am.group(1).strip() if am else None
    rows.append({'publication_number': pubnum, 'assignee': assignee, 'cpc': r.get('cpc'), 'citation': r.get('citation')})

result = json.dumps(rows[:50])
print('__RESULT__:')
print(result)"""

env_args = {'var_call_z5ePch7V6HT6WQ4kNEiVOTo1': [], 'var_call_D409GimujkyCN4Z0JvjLd0PP': ['cpc_definition'], 'var_call_JuX5KYqIN2KYQuSBeJTNhmMD': 'file_storage/call_JuX5KYqIN2KYQuSBeJTNhmMD.json'}

exec(code, env_args)
