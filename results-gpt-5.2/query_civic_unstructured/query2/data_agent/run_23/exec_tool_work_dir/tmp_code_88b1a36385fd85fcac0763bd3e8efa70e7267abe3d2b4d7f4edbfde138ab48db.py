code = """import json, re
import pandas as pd

fp = var_call_s2zxLpt2M81xgHj3iD5tzsh9
with open(fp,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])

# load docs
path = var_call_Eai1gFyqM6dFXNoszLVPh4Kg
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

# find explicit "Park" projects and their completion in 2022 using regex across whole corpus
# We'll look for patterns like "<Project Name>\n...Updates: ...completed ... 2022" in same doc.

project_names = set(fund_df['Project_Name'].tolist())
# focus on park-related by name contains Park / Playground / Skate Park / Bluffs etc? Use keyword park in project name.
park_name_projects = {p for p in project_names if re.search(r'\bpark\b', p, re.IGNORECASE)}

completed_2022 = set()

for d in docs:
    text=d.get('text','')
    for p in park_name_projects:
        # if project name appears and within 300 chars after it contains completed and 2022
        for m in re.finditer(re.escape(p), text, flags=re.IGNORECASE):
            seg=text[m.end(): m.end()+500]
            if re.search(r'completed[^\n\.]*2022|construction was completed[^\n\.]*2022', seg, flags=re.IGNORECASE):
                completed_2022.add(p)

# compute total
sel = fund_df[fund_df['Project_Name'].isin(sorted(completed_2022))]

total=int(sel['total_amount'].sum())
out={'total_funding': total, 'projects': sel.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_s2zxLpt2M81xgHj3iD5tzsh9': 'file_storage/call_s2zxLpt2M81xgHj3iD5tzsh9.json', 'var_call_Eai1gFyqM6dFXNoszLVPh4Kg': 'file_storage/call_Eai1gFyqM6dFXNoszLVPh4Kg.json', 'var_call_trs0AmXXSajzTXjsnWZIdQib': {'total_funding': 0, 'projects': []}}

exec(code, env_args)
