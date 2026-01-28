code = """import json

with open(var_call_bL3GaMT9aRuk5IYztuJtmf6B, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_x7aqU6vz0ZsKaLH4mtwjbPXb, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

funding = [(r.get('Project_Name') or '').strip() for r in funding_rows]
funding_map = { (r.get('Project_Name') or '').strip(): int(r.get('Total_Amount') or 0) for r in funding_rows }

projects = set()
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i,l in enumerate(lines):
        lo = l.lower()
        if 'spring' in lo and 'begin' in lo:
            # check nearby for 2022
            window = '\n'.join(lines[max(0,i-3): i+4]).lower()
            if '2022' not in window:
                continue
            # search backward for project title
            name = None
            for j in range(i-1, max(-1,i-15), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if cand.endswith(':'):
                    continue
                if len(cand) > 120:
                    continue
                # skip lines that are generic headings
                lo_c = cand.lower()
                if any(x in lo_c for x in ['updates', 'project schedule', 'project description', 'agenda', 'page']):
                    continue
                name = ' '.join(cand.split())
                break
            if name:
                projects.add(name)

proj_list = sorted(projects)
# match funding
proj_funding = []
for p in proj_list:
    amt = 0
    # exact
    if p in funding_map:
        amt = funding_map[p]
    else:
        pl = p.lower()
        for fn, val in funding_map.items():
            if pl in fn.lower() or fn.lower() in pl:
                amt += val
    proj_funding.append({'name': p, 'funding': amt})

total_projects = len(proj_funding)
total_funding = sum(x['funding'] for x in proj_funding)
res = {'project_count': total_projects, 'total_funding': total_funding, 'projects': proj_funding}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_MujWVKL2rzsnCnBkRhI5jdNc': ['civic_docs'], 'var_call_CkJufZ8OKzfyEKZaSzfjxgyj': ['Funding'], 'var_call_bL3GaMT9aRuk5IYztuJtmf6B': 'file_storage/call_bL3GaMT9aRuk5IYztuJtmf6B.json', 'var_call_x7aqU6vz0ZsKaLH4mtwjbPXb': 'file_storage/call_x7aqU6vz0ZsKaLH4mtwjbPXb.json'}

exec(code, env_args)
