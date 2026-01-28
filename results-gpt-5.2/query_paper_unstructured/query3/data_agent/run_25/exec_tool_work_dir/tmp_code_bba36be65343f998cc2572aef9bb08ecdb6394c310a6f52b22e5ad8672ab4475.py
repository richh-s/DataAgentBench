code = """import json, re, pandas as pd

# Load citations
cit_path = var_call_U0lcnZKHih4sfzLUna4TquRB
with open(cit_path,'r',encoding='utf-8') as f:
    cit = json.load(f)

dfc = pd.DataFrame(cit)
if dfc.empty:
    out = []
else:
    dfc['citation_count'] = pd.to_numeric(dfc['citation_count'], errors='coerce').fillna(0).astype(int)

# Load empirical docs (text contains 'empirical')
docs_path = var_call_Je3SoVz4YZtloNvEzc1vUPot
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

def title_from_filename(fn):
    return re.sub(r'\.txt$','',fn)

def extract_year(text):
    # look for 4-digit year, prefer 2017+ and within plausible range
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    # prefer max year <=2026 (often citation year or conference year); but publication year is typically near header with CHI 2018 etc.
    # choose most frequent year among candidates 2000+
    from collections import Counter
    c = Counter(years)
    # tie-break by higher year
    yr = sorted(c.items(), key=lambda kv:(-kv[1], -kv[0]))[0][0]
    return yr

rows=[]
for d in docs:
    t = title_from_filename(d.get('filename',''))
    year = extract_year(d.get('text','') or '')
    rows.append({'title': t, 'year': year, 'contribution':'empirical'})

dfd = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Filter after 2016
post = dfd[(dfd['year'].notna()) & (dfd['year'].astype(int) > 2016)].copy()

# join citations and sum counts across years
if post.empty:
    res=[]
else:
    merged = post.merge(dfc, on='title', how='left')
    agg = merged.groupby(['title'], as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    res = agg.sort_values('total_citation_count', ascending=False).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ULK3sMfRoEwsNpJE1cmbWOF4': 'file_storage/call_ULK3sMfRoEwsNpJE1cmbWOF4.json', 'var_call_U0lcnZKHih4sfzLUna4TquRB': 'file_storage/call_U0lcnZKHih4sfzLUna4TquRB.json', 'var_call_Je3SoVz4YZtloNvEzc1vUPot': 'file_storage/call_Je3SoVz4YZtloNvEzc1vUPot.json'}

exec(code, env_args)
