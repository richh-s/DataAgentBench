code = """import json, re

path = var_call_Pq8anEwyVn3RgRhcobvIh6nq
with open(path,'r',encoding='utf-8') as f:
    docs = json.load(f)

all_text = "\n".join(d.get('text','') for d in docs)

projects = []
current = None

stop_prefixes = (
    'page','agenda item','public works','commission','to','prepared','approved',
    'date prepared','meeting date','subject','recommended action','discussion',
    'capital improvement projects','disaster projects','project schedule','estimated schedule',
    'updates','project description','complete design','begin construction','advertise',
    'award contract','begin design'
)

name_re = re.compile(r"^[A-Za-z0-9][A-Za-z0-9\s\-\&\(\)/',\.]{2,}$")

for line in all_text.splitlines():
    l = line.strip()
    if not l:
        continue
    low = l.lower()

    if (':' not in l and not low.startswith(stop_prefixes) and not l.startswith(('(cid', '-', '*'))
        and name_re.match(l)):
        current = l

    if current and re.search(r'Begin\s+(Construction|Design):\s*Spring\s+2022', l, re.I):
        projects.append(current)
        current = None

projects = list(dict.fromkeys(projects))

fund_path = var_call_lwbNDmgVITWaBOs1FyL7L21S
with open(fund_path,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_map = {r['Project_Name']: float(r['Total_Amount']) for r in fund}

matched = [p for p in projects if p in fund_map]
missing = [p for p in projects if p not in fund_map]

total = sum(fund_map[p] for p in matched)

result = {
    'count_projects': len(projects),
    'total_funding': total,
    'projects': projects,
    'projects_without_funding_match': missing
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uj65NF4w9CdaUo3G2lJknYD5': [], 'var_call_lwbNDmgVITWaBOs1FyL7L21S': 'file_storage/call_lwbNDmgVITWaBOs1FyL7L21S.json', 'var_call_FIcFshle7x0Wv4IUBDg7ns0I': [], 'var_call_Pq8anEwyVn3RgRhcobvIh6nq': 'file_storage/call_Pq8anEwyVn3RgRhcobvIh6nq.json'}

exec(code, env_args)
