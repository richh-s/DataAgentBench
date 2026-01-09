code = """import json, re, pandas as pd

# load funding aggregated
with open(var_call_5cXBwuKOk9HBY4nYwJzmGqBJ,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load civic docs
with open(var_call_gbRRfwNhmwPiWJx613mtvjAs,'r',encoding='utf-8') as f:
    docs = json.load(f)

spring2022_projects=set()

# find project name lines followed later by Begin Construction
name_pat = re.compile(r"\n\s*([A-Z][A-Za-z0-9&\-/ ]{2,120}?)\n\s*\(cid:190\)")
begin_pat = re.compile(r"Begin\s+Construction\s*:\s*([^\n\r]+)", re.I)

for d in docs:
    text=d.get('text','')
    lines=text.splitlines()
    current_name=None
    for i,line in enumerate(lines):
        m=name_pat.match("\n"+line+"\n")
        if m:
            current_name=m.group(1).strip()
            continue
        if current_name:
            bm=begin_pat.search(line)
            if bm:
                st=bm.group(1).strip()
                if re.search(r"\bSpring\b", st, re.I) and re.search(r"\b2022\b", st):
                    spring2022_projects.add(current_name)
                current_name=None

proj_df=pd.DataFrame({'Project_Name':sorted(spring2022_projects)})
merged=proj_df.merge(fund_df, on='Project_Name', how='left')
merged['total_amount']=merged['total_amount'].fillna(0).astype(int)
count=int(len(proj_df))
total_funding=int(merged['total_amount'].sum())

result={'projects_started_spring_2022_count':count,'total_funding_usd':total_funding,'projects':merged.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HTcacgrkFLLhMSQenI9hy0rQ': ['Funding'], 'var_call_5cXBwuKOk9HBY4nYwJzmGqBJ': 'file_storage/call_5cXBwuKOk9HBY4nYwJzmGqBJ.json', 'var_call_gbRRfwNhmwPiWJx613mtvjAs': 'file_storage/call_gbRRfwNhmwPiWJx613mtvjAs.json'}

exec(code, env_args)
