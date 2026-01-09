code = """import json, re

path = var_call_rn7TZs6Br9Hucjj0u18Fvagq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

pattern = re.compile(r'(?im)^\s*([^\n]{4,120}?)\s*\n\s*\(cid:190\)\s*project schedule.*?\n(?:.*\n){0,20}?\s*(?:award contract and )?begin (?:construction|design)\s*:\s*spring(?:/summer)?\s+2022', re.MULTILINE)
pattern2 = re.compile(r'(?im)^\s*([^\n]{4,120}?)\s*\n\s*\(cid:190\)\s*estimated schedule.*?\n(?:.*\n){0,20}?\s*begin construction\s*:\s*spring\s+2022', re.MULTILINE)

projects=set()
for d in docs:
    t=d.get('text','')
    for m in pattern.finditer(t):
        projects.add(m.group(1).strip())
    for m in pattern2.finditer(t):
        projects.add(m.group(1).strip())

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'count': len(projects)}, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json', 'var_call_rn7TZs6Br9Hucjj0u18Fvagq': 'file_storage/call_rn7TZs6Br9Hucjj0u18Fvagq.json'}

exec(code, env_args)
