code = """import re, json
import pandas as pd

# Load full Mongo results
path_docs = var_call_eIw1jqzGFxqT7hfnqkYZxgcz
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract year from text and filter empirical & year>2016
records = []
for d in docs:
    text = d.get('text', '')
    # crude year extraction: look for CHI 2018, 2019, etc. or standalone years 2017-2025
    m = re.search(r'(19|20)\d{2}', text)
    year = int(m.group(0)) if m else None
    if year is None or year <= 2016:
        continue
    # contribution contains 'empirical' by assumption from regex; still keep
    title = d.get('filename','').replace('.txt','')
    records.append({'title': title, 'year': year})

emp_df = pd.DataFrame(records).drop_duplicates('title')

# Load citations aggregate
path_cit = var_call_FP1xl2G9m3ejNmssItrkPQd8
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = emp_df.merge(cit_df, on='title', how='left')
result = merged[['title','total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_eIw1jqzGFxqT7hfnqkYZxgcz': 'file_storage/call_eIw1jqzGFxqT7hfnqkYZxgcz.json', 'var_call_FP1xl2G9m3ejNmssItrkPQd8': 'file_storage/call_FP1xl2G9m3ejNmssItrkPQd8.json'}

exec(code, env_args)
