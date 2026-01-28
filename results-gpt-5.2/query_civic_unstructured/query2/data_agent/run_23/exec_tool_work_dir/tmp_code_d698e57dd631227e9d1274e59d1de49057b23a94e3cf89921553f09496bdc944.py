code = """import json, re
import pandas as pd

fp = var_call_s2zxLpt2M81xgHj3iD5tzsh9
with open(fp,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])

path = var_call_Eai1gFyqM6dFXNoszLVPh4Kg
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

project_names = set(fund_df['Project_Name'].tolist())
park_name_projects = {p for p in project_names if re.search(r'\bpark\b', p, re.IGNORECASE)}

completed_2022=set()
for d in docs:
    text=d.get('text','')
    for p in park_name_projects:
        for m in re.finditer(re.escape(p), text, flags=re.IGNORECASE):
            seg=text[m.end(): m.end()+800]
            if re.search(r'construction\s+was\s+completed[^\n\.]*2022|completed[^\n\.]*2022', seg, flags=re.IGNORECASE):
                completed_2022.add(p)

sel=fund_df[fund_df['Project_Name'].isin(sorted(completed_2022))]
total=int(sel['total_amount'].sum())
out={'total_funding': total, 'projects': sel.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_s2zxLpt2M81xgHj3iD5tzsh9': 'file_storage/call_s2zxLpt2M81xgHj3iD5tzsh9.json', 'var_call_Eai1gFyqM6dFXNoszLVPh4Kg': 'file_storage/call_Eai1gFyqM6dFXNoszLVPh4Kg.json', 'var_call_trs0AmXXSajzTXjsnWZIdQib': {'total_funding': 0, 'projects': []}}

exec(code, env_args)
