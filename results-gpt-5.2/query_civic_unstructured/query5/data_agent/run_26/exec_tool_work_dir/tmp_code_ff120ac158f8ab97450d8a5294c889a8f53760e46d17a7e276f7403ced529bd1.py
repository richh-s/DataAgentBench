code = """import json, re

# load funding totals per project
with open(var_call_UCppypxJ9ivCqpPzCKPpOdD5,'r') as f:
    funding = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

# load docs containing Begin Construction...2022
with open(var_call_AMbDR1W598Rz0lmwiAbvO85T,'r') as f:
    docs = json.load(f)

# identify disaster projects by presence of FEMA/CalOES/CalJPIA in name or being under disaster section
# then pick those with begin construction in 2022

def extract_projects_with_begin_2022(text):
    # Find all occurrences of a project block ending before next project name candidate
    lines=[ln.rstrip() for ln in text.splitlines()]
    res=[]
    current=None
    in_disaster=False
    for ln in lines:
        s=ln.strip()
        if re.search(r'^Disaster (Recovery )?Projects', s, re.I):
            in_disaster=True
            current=None
            continue
        if re.search(r'^Capital Improvement Projects', s, re.I):
            in_disaster=False
            current=None
            continue
        if not s:
            continue
        # detect project name line
        if in_disaster and ':' not in s and not s.startswith(('-', '•','(cid')) and re.search(r'[A-Za-z]', s):
            if s.lower() in ['updates','project schedule','estimated schedule','project description','project updates']:
                continue
            if 'Project Schedule' in s or 'Estimated Schedule' in s or 'Updates' in s:
                continue
            current=s
        if in_disaster and current and 'Begin Construction' in s and '2022' in s:
            res.append(current)
    return res

projects=set()
for d in docs:
    for p in extract_projects_with_begin_2022(d.get('text','')):
        projects.add(p)

matched=[(p, fund_map[p]) for p in sorted(projects) if p in fund_map]
total=sum(a for _,a in matched)

print('__RESULT__:')
print(json.dumps({'projects': sorted(list(projects)), 'matched': matched, 'total_funding': total}))"""

env_args = {'var_call_1RXUbsill3cgLaz2LBxIQUhK': ['Funding'], 'var_call_UCppypxJ9ivCqpPzCKPpOdD5': 'file_storage/call_UCppypxJ9ivCqpPzCKPpOdD5.json', 'var_call_KrRlBWaEoRWzCOYEfmvlQflO': 'file_storage/call_KrRlBWaEoRWzCOYEfmvlQflO.json', 'var_call_haNonDDdvRgg36tBKegFtS4y': {'total_funding': 0, 'currency': 'USD', 'matched_projects_count': 0, 'matched_projects': []}, 'var_call_AMbDR1W598Rz0lmwiAbvO85T': 'file_storage/call_AMbDR1W598Rz0lmwiAbvO85T.json'}

exec(code, env_args)
