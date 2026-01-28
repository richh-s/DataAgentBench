code = """import json, re
with open(var_call_zYwQAi7fCjETMLIuuugYdGa0, 'r') as f:
    data = json.load(f)
projects = data.get('projects', [])

with open(var_call_tFD7smh9otcdUy84B2GkmS7e, 'r') as f:
    projinfo_rows = json.load(f)

# build mapping from owner/repo to fork count
forks_map = {}
proj_pattern = re.compile(r'([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)')
# patterns to find fork counts
patterns = [re.compile(r'([0-9,]+)\s+forks'),
            re.compile(r'forks count of\s+([0-9,]+)'),
            re.compile(r'been forked\s+([0-9,]+)\s+times'),
            re.compile(r'forked\s+([0-9,]+)\s+times'),
            re.compile(r'and\s+has\s+been\s+forked\s+([0-9,]+)\s+times')]

for row in projinfo_rows:
    text = row.get('Project_Information') or row.get('Project_Information')
    if not text:
        continue
    # find project owner/repo
    m = proj_pattern.search(text)
    if not m:
        continue
    proj = m.group(1)
    # find forks
    forks = None
    for p in patterns:
        mm = p.search(text)
        if mm:
            try:
                forks = int(mm.group(1).replace(',',''))
                break
            except:
                continue
    # also handle phrases like 'has been forked 12 times' already covered
    if forks is None:
        # try to find 'forks count' numeric after 'forks count of' etc with different casing
        mm = re.search(r'forks[:]?\s*([0-9,]+)', text)
        if mm:
            forks = int(mm.group(1).replace(',',''))
    if forks is None:
        # as fallback, try to find any number followed by 'fork'
        mm = re.search(r'([0-9,]+)\s+fork', text)
        if mm:
            forks = int(mm.group(1).replace(',',''))
    if forks is None:
        # try 'and has been forked X times' covered; else default 0 if mentions '0 forks'
        if re.search(r'0\s+forks', text):
            forks = 0
    if forks is None:
        continue
    # store max if multiple entries
    if proj in forks_map:
        forks_map[proj] = max(forks_map[proj], forks)
    else:
        forks_map[proj] = forks

# For each project in our merged list, get forks if present
rows = []
for p in projects:
    if p in forks_map:
        rows.append({'project': p, 'forks': forks_map[p]})

# sort by forks desc
rows_sorted = sorted(rows, key=lambda x: x['forks'], reverse=True)
# take top 5
top5 = rows_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_MEq7coGaFeZY1uYdzEuOBVxR': 'file_storage/call_MEq7coGaFeZY1uYdzEuOBVxR.json', 'var_call_DQHCHJPoGMReDnmscL4ipZwY': 'file_storage/call_DQHCHJPoGMReDnmscL4ipZwY.json', 'var_call_2e1tl2asUOd6KA5haPS4xUwV': 'file_storage/call_2e1tl2asUOd6KA5haPS4xUwV.json', 'var_call_MykHHMcZQD5RHNY0zWZurORb': 'file_storage/call_MykHHMcZQD5RHNY0zWZurORb.json', 'var_call_zYwQAi7fCjETMLIuuugYdGa0': 'file_storage/call_zYwQAi7fCjETMLIuuugYdGa0.json', 'var_call_tFD7smh9otcdUy84B2GkmS7e': 'file_storage/call_tFD7smh9otcdUy84B2GkmS7e.json'}

exec(code, env_args)
