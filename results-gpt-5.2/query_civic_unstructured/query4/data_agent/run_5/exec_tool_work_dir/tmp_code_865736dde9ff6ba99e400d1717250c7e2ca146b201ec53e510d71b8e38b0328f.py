code = """import json, re

path = var_call_rn7TZs6Br9Hucjj0u18Fvagq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Simpler: find lines 'Begin Construction: Spring 2022' and take nearest non-empty line above within 15 lines that isn't a bullet/label.

bad = set(['updates:', 'project schedule:', 'estimated schedule:', 'project schedule', 'estimated schedule'])

projects=set()
for d in docs:
    lines = d.get('text','').splitlines()
    for i, line in enumerate(lines):
        if re.search(r'(?i)begin\s+construction\s*:\s*spring\s+2022', line) or re.search(r'(?i)begin\s+design\s*:\s*spring\s+2022', line) or re.search(r'(?i)award\s+contract\s+and\s+begin\s+construction\s*:\s*spring\s*/?summer\s+2022', line):
            # look back
            for j in range(i-1, max(-1, i-20), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                low=cand.lower()
                if low.startswith('(cid') or low.startswith('page') or low.startswith('agenda item'):
                    continue
                if low in bad or low.endswith(':'):
                    continue
                if any(low.startswith(x) for x in ['complete design', 'advertise', 'award contract', 'begin construction', 'begin design']):
                    continue
                projects.add(cand)
                break

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'count': len(projects)}, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json', 'var_call_rn7TZs6Br9Hucjj0u18Fvagq': 'file_storage/call_rn7TZs6Br9Hucjj0u18Fvagq.json'}

exec(code, env_args)
