code = """import json, re, pandas as pd

# Load mongo results (physical activity mentions)
path_docs = var_call_BVWwiCap7tKObk8kHQfSOpQu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations totals
path_cit = var_call_h6OXGvmtr975xm0e2xhoRUPs
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_cit = pd.DataFrame(cits)
# coerce totals to int
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# regex to detect publication year 2016 in text
pat_2016 = re.compile(r'\b2016\b')
pat_pa = re.compile(r'(?i)physical activity')

records = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','') or ''
    # domain filter: mention physical activity
    if not pat_pa.search(text):
        continue
    # publication year detection: look for 2016 in header/copyright lines; approximate by presence of 2016 near ACM/IEEE/CHI/UbiComp etc.
    if not pat_2016.search(text[:5000]):
        continue
    records.append({'title': title})

df = pd.DataFrame(records).drop_duplicates()
if df.empty:
    out = []
else:
    df = df.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BVWwiCap7tKObk8kHQfSOpQu': 'file_storage/call_BVWwiCap7tKObk8kHQfSOpQu.json', 'var_call_h6OXGvmtr975xm0e2xhoRUPs': 'file_storage/call_h6OXGvmtr975xm0e2xhoRUPs.json'}

exec(code, env_args)
