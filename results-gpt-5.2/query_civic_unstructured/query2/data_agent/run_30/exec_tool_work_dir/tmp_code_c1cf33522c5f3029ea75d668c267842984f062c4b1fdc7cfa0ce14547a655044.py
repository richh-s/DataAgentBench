code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_QUyr3dcKDC0eXDjbPjHLTqsp
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding by project
path_fund = var_call_pGC3XBrgMdG1xvhNaW8ThPZd
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# Extract completed-in-2022 park-related projects from texts by scanning for project name mentions

def is_park_related(name, context):
    s = (name + ' ' + context).lower()
    return ('park' in s) or ('playground' in s) or ('skate' in s) or ('bluffs' in s)

completed_2022_projects = set()

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # only consider docs that mention 2022 and completed to reduce scan
    if ('2022' not in text) or ('completed' not in text.lower()):
        continue
    lower_text = text.lower()
    for pname in fund_map.keys():
        if pname.lower() in lower_text:
            # take a local window around first occurrence
            idx = lower_text.find(pname.lower())
            start = max(0, idx-250)
            end = min(len(text), idx+250)
            window = text[start:end]
            wlow = window.lower()
            if 'completed' in wlow and '2022' in wlow and is_park_related(pname, window):
                completed_2022_projects.add(pname)

# Sum funding
total = int(sum(fund_map.get(p,0) for p in completed_2022_projects))

# Prepare for output
out = {
    'total_funding': total,
    'projects': sorted(list(completed_2022_projects))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_rA9OVMksUxsTybelcDMILcJ6': ['Funding'], 'var_call_QUyr3dcKDC0eXDjbPjHLTqsp': 'file_storage/call_QUyr3dcKDC0eXDjbPjHLTqsp.json', 'var_call_pGC3XBrgMdG1xvhNaW8ThPZd': 'file_storage/call_pGC3XBrgMdG1xvhNaW8ThPZd.json'}

exec(code, env_args)
