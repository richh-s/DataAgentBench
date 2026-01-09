code = """import json
from pathlib import Path

def load_json(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        return json.loads(Path(path_or_obj).read_text())
    return path_or_obj

funding = load_json(var_call_GCrz7PZzTsfBZVJ15IQgHB5f)
fund_map = {r['Project_Name']: int(float(r['total_amount'])) for r in funding}

docs = load_json(var_call_Lh0eRTIe56Ejmza0L361Q0G8)
text = docs[0]['text'] if docs else ''

# Hard parse the disaster section from this doc: between "Disaster Recovery Projects" and next "Capital Improvement Projects" header.
start = text.lower().find('disaster recovery projects')
end = text.lower().find('capital improvement projects', start+1)
sec = text[start:end] if start!=-1 and end!=-1 else ''

# find project title lines in sec: lines that match a funding project name and appear as standalone line
sec_lines = [ln.strip() for ln in sec.splitlines()]
found = []
fund_names = set(fund_map.keys())
fund_lower = {k.lower(): k for k in fund_names}
for ln in sec_lines:
    if not ln:
        continue
    key = ln.lower()
    if key in fund_lower:
        found.append(fund_lower[key])

# if none exact, try substring scan for each funding name in sec
if not found:
    sec_low = sec.lower()
    for k in fund_names:
        if ('\n'+k.lower()+'\n') in sec_low:
            found.append(k)

# started in 2022: if project title occurs and nearby has "Begin Construction" with 2022 (within next ~20 lines)
started_2022=[]
for i, ln in enumerate(sec_lines):
    kl = ln.lower()
    if kl in fund_lower:
        pname = fund_lower[kl]
        window = '\n'.join(sec_lines[i:i+25]).lower()
        if 'begin construction' in window and '2022' in window:
            started_2022.append(pname)

started_2022 = sorted(set(started_2022))
total = sum(fund_map.get(p,0) for p in started_2022)

out = {'total_funding': total, 'projects': started_2022, 'project_count': len(started_2022)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NBSUCTIM9JLMEB37N0JQuCuN': ['Funding'], 'var_call_TdUCedLY6IGaC3oOgBBiqt7o': ['civic_docs'], 'var_call_GCrz7PZzTsfBZVJ15IQgHB5f': 'file_storage/call_GCrz7PZzTsfBZVJ15IQgHB5f.json', 'var_call_rg2So0OGkK4XssNZ4JbiVkKf': 'file_storage/call_rg2So0OGkK4XssNZ4JbiVkKf.json', 'var_call_Lh0eRTIe56Ejmza0L361Q0G8': 'file_storage/call_Lh0eRTIe56Ejmza0L361Q0G8.json'}

exec(code, env_args)
