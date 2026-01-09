code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_ColyzPVLwrm6y70pEszOjYFI)

# find first doc containing disaster section and print snippet around it
for d in docs:
    t = d.get('text','') or ''
    if re.search(r'Disaster\s+Recovery\s+Projects', t, re.IGNORECASE):
        lines = t.splitlines()
        for i,ln in enumerate(lines):
            if re.search(r'Disaster\s+Recovery\s+Projects', ln, re.IGNORECASE):
                start=max(0,i-3); end=min(len(lines), i+80)
                snippet='\n'.join(lines[start:end])
                print('__RESULT__:')
                print(json.dumps({'filename': d.get('filename'), 'snippet': snippet[:8000]}))
                raise SystemExit
print('__RESULT__:')
print(json.dumps({'error':'not found'}))"""

env_args = {'var_call_YgUR6tR7zkFTdknoL5kz9DLG': 'file_storage/call_YgUR6tR7zkFTdknoL5kz9DLG.json', 'var_call_ColyzPVLwrm6y70pEszOjYFI': 'file_storage/call_ColyzPVLwrm6y70pEszOjYFI.json', 'var_call_iMOex9cPQGXibS0Ruz0oHmZx': {'total_funding_disaster_projects_started_2022': 0, 'num_projects': 0, 'projects': []}}

exec(code, env_args)
