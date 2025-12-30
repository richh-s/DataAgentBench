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
all_projects = []

for doc in docs:
    txt = doc['text']
    # Split by lines
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    
    # Iterate and find "Updates:"
    for i, line in enumerate(lines):
        if 'Updates:' in line:
            # Title is likely at i-1
            if i > 0:
                title = lines[i-1]
                # Extract description/status from this line onwards
                # until next title (next Updates: - 1)
                
                # Simple extraction: take next 10 lines as context
                context = " ".join(lines[i:i+15]).lower()
                
                all_projects.append({
                    'name': title,
                    'context': context
                })

# Filter
matched_names = set()
for p in all_projects:
    name = p['name']
    ctx = p['context']
    
    # 1. Park
    if 'park' in name.lower() or 'park' in ctx:
        # 2. Completed in 2022
        # Check patterns
        if 'completed' in ctx and '2022' in ctx:
            # Refine
            # "completed november 2022"
            # "completed, november 2022"
             if re.search(r'completed.{0,20}2022', ctx):
                 matched_names.add(name)

# Resolve with Funding
# Clean names from 'matched_names' and find in 'df_fund'
final_list = []

fund_names = df_fund['Project_Name'].unique()

for m_name in matched_names:
    # Try exact or substring match
    # m_name might have special chars
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
        final_list.append(match)

# Unique
final_list = list(set(final_list))
total = df_fund[df_fund['Project_Name'].isin(final_list)]['Amount'].sum()

print("__RESULT__:")
print(json.dumps({"total": total, "projects": final_list}))"""

env_args = {'var_function-call-17862480380810104238': 'file_storage/function-call-17862480380810104238.json', 'var_function-call-18328159169731343039': 'file_storage/function-call-18328159169731343039.json', 'var_function-call-18248731954071622536': 'file_storage/function-call-18248731954071622536.json'}

exec(code, env_args)
