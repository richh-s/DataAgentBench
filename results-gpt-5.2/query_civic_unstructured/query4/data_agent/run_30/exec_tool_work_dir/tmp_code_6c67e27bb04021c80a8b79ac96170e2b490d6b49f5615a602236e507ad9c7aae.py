code = """import json, re
import pandas as pd

# Load civic docs matched by regex
path = var_call_QN3GYKOI9zQrosTKXFFksrwn
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals by project
fund_path = var_call_weaVUCZ15mff52GSzJzCAyUp
with open(fund_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

spring_projects = set()

# Helper to extract project blocks and their schedules
for d in docs:
    text = d.get('text','')
    # normalize
    t = text.replace('\u2019',"'")
    # find each project section by blank lines; project name often alone in a line
    lines = [ln.strip() for ln in t.splitlines()]
    # Build indices where line looks like a project title (not bullet and not empty) and next non-empty contains 'Updates' or 'Project Description'
    for i, ln in enumerate(lines[:-1]):
        if not ln or ln.startswith('(cid') or ln.endswith(':'):
            continue
        if re.search(r'\bUpdates\b', lines[i+1], re.I) or re.search(r'\bProject Description\b', lines[i+1], re.I):
            # candidate project name
            pname = ln
            # scan following ~40 lines for schedule lines containing 'Begin' and 'Spring 2022'
            window = '\n'.join(lines[i:i+60])
            if re.search(r'Begin\s+(Construction|Design)[^\n]*:\s*Spring\s*2022', window, re.I):
                spring_projects.add(pname)

# Join with funding
spring_list = sorted(spring_projects)
sp_df = pd.DataFrame({'Project_Name': spring_list})
if not sp_df.empty and not fund_df.empty:
    merged = sp_df.merge(fund_df, on='Project_Name', how='left')
    merged['total_amount'] = merged['total_amount'].fillna(0).astype(int)
    total_funding = int(merged['total_amount'].sum())
else:
    total_funding = 0

result = {
    'spring_2022_started_project_count': int(len(spring_projects)),
    'total_funding_amount_usd': total_funding,
    'projects': spring_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Hr8WwXxtzydFUkrEapVt4Ojs': ['Funding'], 'var_call_weaVUCZ15mff52GSzJzCAyUp': 'file_storage/call_weaVUCZ15mff52GSzJzCAyUp.json', 'var_call_kOk8MQDIDghfY8ob9WPtT6vY': [], 'var_call_QN3GYKOI9zQrosTKXFFksrwn': 'file_storage/call_QN3GYKOI9zQrosTKXFFksrwn.json'}

exec(code, env_args)
