code = """import json
import re
import pandas as pd

civic_path = locals()['var_function-call-18248731954071622536']
funding_path = locals()['var_function-call-18328159169731343039']

with open(civic_path, 'r') as f:
    docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

df_fund = pd.DataFrame(funding)
df_fund['Amount'] = pd.to_numeric(df_fund['Amount'], errors='coerce')

projects = []

for doc in docs:
    txt = doc['text']
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    
    update_indices = [i for i, line in enumerate(lines) if 'Updates:' in line]
    project_starts = sorted(list(set([i-1 for i in update_indices if i > 0])))
    
    for k in range(len(project_starts)):
        start_idx = project_starts[k]
        end_idx = project_starts[k+1] if k+1 < len(project_starts) else len(lines)
        
        name = lines[start_idx]
        # Text from start+1 to end_idx. 
        # Note: end_idx is the start of next project (line before Updates).
        chunk = lines[start_idx+1 : end_idx]
        full_text = " ".join(chunk).lower()
        projects.append({'name': name, 'text': full_text})

final_projects = set()

for p in projects:
    name = p['name']
    text = p['text']
    
    # Topic: Park
    if 'park' in name.lower() or 'park' in text:
        # Status: Completed in 2022
        # Check specific completion patterns
        is_completed = False
        if re.search(r'construction.*?completed.*?2022', text) or \
           re.search(r'completed.*?construction.*?2022', text) or \
           re.search(r'complete construction.*?2022', text):
            is_completed = True
        elif re.search(r'completed\s+[a-zA-Z]+\s+2022', text): 
             # e.g. "completed November 2022" without "construction" word nearby
             is_completed = True
        
        if is_completed:
            final_projects.add(name)

# Resolve funding
funding_match_list = []
fund_names = df_fund['Project_Name'].unique()

for m_name in final_projects:
    clean_m = m_name.strip()
    match = None
    if clean_m in fund_names:
        match = clean_m
    else:
        for fn in fund_names:
            if fn in clean_m or clean_m in fn:
                match = fn
                break
    if match:
        funding_match_list.append(match)

funding_match_list = list(set(funding_match_list))
total_amt = df_fund[df_fund['Project_Name'].isin(funding_match_list)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total": total_amt, "projects": funding_match_list}))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json', 'var_function-call-18090166936097834747': {'total': 210001600024000.0, 'projects': ['PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure']}}

exec(code, env_args)
