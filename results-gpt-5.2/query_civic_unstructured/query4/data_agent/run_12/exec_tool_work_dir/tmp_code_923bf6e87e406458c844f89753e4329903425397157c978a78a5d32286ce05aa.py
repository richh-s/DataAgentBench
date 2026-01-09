code = """import json, re

raw = var_call_hfv6gVDdrgKpYyCiZVl8LQPr
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

spring2022_projects = set()

# find occurrences of 'Begin Construction: Spring 2022' and take nearest preceding non-empty line as project name
for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    for i,line in enumerate(lines):
        if re.search(r'Begin Construction\s*:\s*Spring\s+2022', line, re.IGNORECASE):
            # search backwards for a plausible project name: non-empty and not bullet markers
            j = i-1
            while j>=0:
                cand = lines[j].strip()
                if cand and not cand.startswith('(cid:') and 'project schedule' not in cand.lower() and 'estimated schedule' not in cand.lower() and 'updates' not in cand.lower():
                    # stop at section headers
                    if 'capital improvement projects' in cand.lower() or 'disaster projects' in cand.lower():
                        break
                    spring2022_projects.add(cand)
                    break
                j -= 1

proj_list = sorted(spring2022_projects)
print('__RESULT__:')
print(json.dumps({"spring_2022_projects": proj_list, "count": len(proj_list)}))"""

env_args = {'var_call_WF7nOmUatVD8vw8PJCkI3sVH': ['Funding'], 'var_call_wRmXiS5fuWvTjHJBViejlb7C': ['civic_docs'], 'var_call_RU0Eeenz3jeZ4nl37lbeV0m4': 'file_storage/call_RU0Eeenz3jeZ4nl37lbeV0m4.json', 'var_call_hfv6gVDdrgKpYyCiZVl8LQPr': 'file_storage/call_hfv6gVDdrgKpYyCiZVl8LQPr.json'}

exec(code, env_args)
