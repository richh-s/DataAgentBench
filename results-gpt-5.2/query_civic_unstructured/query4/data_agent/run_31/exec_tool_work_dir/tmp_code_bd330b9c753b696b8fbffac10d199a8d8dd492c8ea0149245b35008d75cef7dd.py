code = """import json, re, pandas as pd

# load funding aggregated
path_funding = var_call_5cXBwuKOk9HBY4nYwJzmGqBJ
with open(path_funding,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load civic docs
path_docs = var_call_gbRRfwNhmwPiWJx613mtvjAs
with open(path_docs,'r',encoding='utf-8') as f:
    docs = json.load(f)

spring2022_projects=set()

# regex to find project sections with schedule
pat = re.compile(r"\n\s*([A-Z0-9][^\n]{2,120}?)\n\s*\(cid:190\)\s*Updates:.*?\(cid:190\)\s*(?:Project Schedule|Estimated Schedule)\s*:.*?(?=\n\s*[A-Z0-9][^\n]{2,120}\n\s*\(cid:190\)|\Z)", re.S)
start_pat = re.compile(r"Begin\s+Construction\s*:\s*([^\n\r]+)", re.I)

for d in docs:
    text=d.get('text','')
    for m in pat.finditer(text):
        name=m.group(1).strip()
        block=m.group(0)
        sm=start_pat.search(block)
        if not sm:
            continue
        st=sm.group(1).strip()
        st_clean=re.sub(r"[\u2022\(\)\[\]\\u2013\u2014]", " ", st)
        if re.search(r"\bSpring\b", st_clean, re.I) and re.search(r"\b2022\b", st_clean):
            spring2022_projects.add(name)

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
