code = """import json, re

# Load civic docs result from file
path = var_call_Pq8anEwyVn3RgRhcobvIh6nq
with open(path,'r',encoding='utf-8') as f:
    docs = json.load(f)

text = "\n".join(d['text'] for d in docs)

# Parse project sections by blank lines and look for schedule lines containing Spring 2022 as start
projects = []
current = None
for line in text.splitlines():
    l = line.strip()
    if not l:
        continue
    # heuristic: project name lines have no ':' and not bullet and not headings
    if re.match(r'^[A-Za-z0-9].{2,}$', l) and ':' not in l and not l.lower().startswith(('page','agenda item','public works','commission','to','prepared','approved','date prepared','meeting date','subject','recommended action','discussion','capital improvement projects','disaster projects','project schedule','estimated schedule','updates','project description','complete design','begin construction','advertise','award contract','begin design')) and not l.startswith(('(cid', '•','-')):
        current = l
    if current and re.search(r'Begin (Construction|Design):\s*Spring\s+2022', l, re.I):
        projects.append(current)
        current = None

projects = list(dict.fromkeys(projects))

# Load funding totals per project
fund_path = var_call_lwbNDmgVITWaBOs1FyL7L21S
with open(fund_path,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: float(r['Total_Amount']) for r in fund}

matched = [p for p in projects if p in fund_map]
missing = [p for p in projects if p not in fund_map]

total = sum(fund_map[p] for p in matched)

result = {
    'projects_started_spring_2022': projects,
    'count_projects': len(projects),
    'count_with_funding_match': len(matched),
    'total_funding_matched': total,
    'projects_without_funding_match': missing
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uj65NF4w9CdaUo3G2lJknYD5': [], 'var_call_lwbNDmgVITWaBOs1FyL7L21S': 'file_storage/call_lwbNDmgVITWaBOs1FyL7L21S.json', 'var_call_FIcFshle7x0Wv4IUBDg7ns0I': [], 'var_call_Pq8anEwyVn3RgRhcobvIh6nq': 'file_storage/call_Pq8anEwyVn3RgRhcobvIh6nq.json'}

exec(code, env_args)
