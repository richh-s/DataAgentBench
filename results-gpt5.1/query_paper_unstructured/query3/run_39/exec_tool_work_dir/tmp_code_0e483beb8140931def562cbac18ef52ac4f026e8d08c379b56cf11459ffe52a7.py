code = """import re, json
import pandas as pd

# Load mongo results
path_docs = var_call_wjqlgL3e0gHXq232Imp66Eqx
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (from filename) and year from text; keep those with empirical contribution and year>2016
records = []
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r'\.txt$', '', filename)
    text = d.get('text','')
    m = re.search(r'(19|20)\d{2}', text)
    year = int(m.group(0)) if m else None
    if year and year > 2016:
        if re.search(r'empirical', text, re.IGNORECASE):
            records.append({'title': title, 'year': year})

# Load citations totals
path_cits = var_call_FvoBSrj8fbX3yonWywwbGwJb
with open(path_cits, 'r') as f:
    cits = json.load(f)

df_emp = pd.DataFrame(records).drop_duplicates(subset=['title'])
df_cit = pd.DataFrame(cits)
if not df_cit.empty:
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)

# Join on title
res = pd.merge(df_emp, df_cit, on='title', how='left')[['title','total_citations']]
res = res.sort_values('title')

result = res.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wjqlgL3e0gHXq232Imp66Eqx': 'file_storage/call_wjqlgL3e0gHXq232Imp66Eqx.json', 'var_call_FvoBSrj8fbX3yonWywwbGwJb': 'file_storage/call_FvoBSrj8fbX3yonWywwbGwJb.json'}

exec(code, env_args)
