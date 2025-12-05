code = """import json, re, pandas as pd
from pathlib import Path

# load full publication records
path = Path(var_call_Nx9DQZ8F7pzaqZrZyWTtWIXy)
rows = json.loads(path.read_text())

# find UNIV CALIFORNIA-assigned patents and map their publication numbers
univ_pubs = set()
for r in rows:
    info = r.get('Patents_info','')
    m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
    if 'UNIV CALIFORNIA' in info and m:
        univ_pubs.add(m.group(1))

# now, we really need entire table, not just CALIFORNIA subset, to find who cites these
# but we don't have it loaded; so with current subset, look for citations to these pub numbers
assignee_to_cpcs = {}
for r in rows:
    cites = json.loads(r.get('citation') or '[]')
    cited_pubs = {c.get('publication_number') for c in cites if c.get('publication_number')}
    if not (univ_pubs & cited_pubs):
        continue
    info = r.get('Patents_info','')
    m_owner = re.search(r'owned by ([^,]+)', info)
    assignee = m_owner.group(1).strip() if m_owner else None
    if not assignee or assignee == 'UNIV CALIFORNIA':
        continue
    cpc_list = json.loads(r.get('cpc') or '[]')
    primary_codes = {e['code'] for e in cpc_list if e.get('first')}
    if not primary_codes:
        primary_codes = {e['code'] for e in cpc_list}
    assignee_to_cpcs.setdefault(assignee, set()).update(primary_codes)

result = {a: sorted(list(codes)) for a, codes in assignee_to_cpcs.items()}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0ub88KCucwbY1WygdzX6TgVw': [], 'var_call_9gthWyxyYF2zG9mTIxpopX1D': [], 'var_call_Nx9DQZ8F7pzaqZrZyWTtWIXy': 'file_storage/call_Nx9DQZ8F7pzaqZrZyWTtWIXy.json'}

exec(code, env_args)
