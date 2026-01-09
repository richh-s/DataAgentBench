code = """import json, re
import pandas as pd

# load docs
p_docs = var_call_7D8EP2WAYggkcSvlh6EUsyhx
with open(p_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding aggregated
p_fund = var_call_gkn6QJLGZl3ts1HELo7BGVOs
with open(p_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

# parse project schedule lines: capture project name heading followed by 'Project Schedule' block with 'Begin Construction:'
projects_started_spring_2022 = set()

begin_re = re.compile(r"Begin Construction:\s*([^\n\r]+)", re.IGNORECASE)
# project header likely a standalone line between blank lines
# We'll split into lines and find blocks
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if ln.lower().startswith('begin construction:'):
            val = ln.split(':',1)[1].strip()
            # check spring 2022
            v = val.lower().replace(' ', '')
            if '2022' in v and ('spring' in v):
                # backtrack to find nearest previous non-empty line that looks like project name
                j = i-1
                name = None
                while j>=0:
                    cand = lines[j]
                    if cand=='' or cand.lower().startswith('project schedule') or cand.lower().startswith('complete design') or cand.lower().startswith('advertise') or cand.lower().startswith('updates') or cand.lower().startswith('estimated schedule'):
                        j-=1
                        continue
                    # stop at section headers
                    if cand.lower().startswith('capital improvement projects') or cand.lower().startswith('disaster recovery projects') or cand.lower().startswith('page '):
                        break
                    # choose first meaningful
                    name = cand
                    break
                if name:
                    projects_started_spring_2022.add(name)

# total funding for those projects
count = len(projects_started_spring_2022)
fund_total = 0
missing = []
for name in sorted(projects_started_spring_2022):
    if name in fund_map:
        fund_total += fund_map[name]
    else:
        missing.append(name)

out = {
    'projects_started_spring_2022': sorted(projects_started_spring_2022),
    'count': count,
    'total_funding': int(fund_total),
    'missing_funding_projects': missing
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1EWiZF0MWHnDBQUWPaYA512M': ['Funding'], 'var_call_7D8EP2WAYggkcSvlh6EUsyhx': 'file_storage/call_7D8EP2WAYggkcSvlh6EUsyhx.json', 'var_call_gkn6QJLGZl3ts1HELo7BGVOs': 'file_storage/call_gkn6QJLGZl3ts1HELo7BGVOs.json'}

exec(code, env_args)
