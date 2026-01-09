code = """import json, re
import pandas as pd

p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

p_fund = var_call_gkn6QJLGZl3ts1HELo7BGVOs
with open(p_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

projects_started_spring_2022 = set()

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        low = ln.lower()
        if low.startswith('begin construction:'):
            val = ln.split(':',1)[1].strip()
            v = val.lower().replace(' ', '')
            if ('2022' in v) and ('spring' in v):
                j = i-1
                name = None
                while j >= 0:
                    cand = lines[j]
                    cl = cand.lower()
                    if cand == '' or cl.startswith('project schedule') or cl.startswith('complete design') or cl.startswith('advertise') or cl.startswith('updates') or cl.startswith('estimated schedule'):
                        j -= 1
                        continue
                    if cl.startswith('capital improvement projects') or cl.startswith('disaster recovery projects') or cl.startswith('page '):
                        break
                    name = cand
                    break
                if name:
                    projects_started_spring_2022.add(name)

count = len(projects_started_spring_2022)
fund_total = 0
missing = []
for name in sorted(projects_started_spring_2022):
    amt = fund_map.get(name)
    if amt is None:
        missing.append(name)
    else:
        fund_total += amt

out = {
    'count': count,
    'total_funding': int(fund_total),
    'projects_started_spring_2022': sorted(projects_started_spring_2022),
    'missing_funding_projects': missing
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json'}

exec(code, env_args)
