code = """import json, re, pandas as pd

with open(var_call_5cXBwuKOk9HBY4nYwJzmGqBJ,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

with open(var_call_gbRRfwNhmwPiWJx613mtvjAs,'r',encoding='utf-8') as f:
    docs = json.load(f)

spring2022_projects=set()

name_pat = re.compile(r"^\s*([A-Z][A-Za-z0-9&\-/ ]{2,120}?)\s*$")
begin_pat = re.compile(r"Begin\s+Construction\s*:\s*([^\n\r]+)")

for d in docs:
    lines=d.get('text','').splitlines()
    current_name=None
    for line in lines:
        if '(cid:190)' in line and current_name is None:
            continue
        m=name_pat.match(line)
        if m and len(m.group(1).split())>=2:
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

result={'projects_started_spring_2022_count':int(len(proj_df)),'total_funding_usd':int(merged['total_amount'].sum())}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HTcacgrkFLLhMSQenI9hy0rQ': ['Funding'], 'var_call_5cXBwuKOk9HBY4nYwJzmGqBJ': 'file_storage/call_5cXBwuKOk9HBY4nYwJzmGqBJ.json', 'var_call_gbRRfwNhmwPiWJx613mtvjAs': 'file_storage/call_gbRRfwNhmwPiWJx613mtvjAs.json'}

exec(code, env_args)
