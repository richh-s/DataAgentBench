code = """import re, json, pandas as pd

mongo_path = var_call_JrvCkgZlVyQIh8mF21biU9gs
sql_path = var_call_ju9InGP20lZd1uAjGF4LYxx9

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

empirical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        years = re.findall(r'(20[1-9][0-9])', text)
        year = None
        if years:
            cand = sorted({int(y) for y in years})
            for y in cand:
                if y >= 2017:
                    year = y
                    break
        if year is None or year <= 2016:
            continue
        title = (doc.get('filename') or '').replace('.txt','')
        if not title:
            continue
        empirical_papers.append({'title': title, 'year': year})

emp_df = pd.DataFrame(empirical_papers).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, how='left', on='title')
merged = merged[['title','total_citations']].sort_values(['title'])

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JrvCkgZlVyQIh8mF21biU9gs': 'file_storage/call_JrvCkgZlVyQIh8mF21biU9gs.json', 'var_call_ju9InGP20lZd1uAjGF4LYxx9': 'file_storage/call_ju9InGP20lZd1uAjGF4LYxx9.json', 'var_call_zbtNXIbDTaDGuIw5urip4aHx': ['title', 'total_citations']}

exec(code, env_args)
