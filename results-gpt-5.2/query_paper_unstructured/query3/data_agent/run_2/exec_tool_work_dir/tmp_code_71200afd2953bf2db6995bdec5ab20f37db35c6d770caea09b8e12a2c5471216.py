code = """import json, re
import pandas as pd

# Load mongo docs (possibly via json file path)
docs_src = var_call_QKx5xGUKcYCoT2Ejy3NYZNtc
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cits_src = var_call_4oUO2WpjgT0D6C24HXPKnhoT
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

# Helpers to extract year and contribution
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not text:
        return None
    t = text[:5000]
    years = [int(y) for y in year_re.findall(t)]
    years = [y for y in years if 1980 <= y <= 2026]
    if not years:
        return None
    # choose most frequent; tie -> max
    from collections import Counter
    c = Counter(years)
    maxfreq = max(c.values())
    cand = [y for y,f in c.items() if f==maxfreq]
    return max(cand)

def is_empirical(text):
    if not text:
        return False
    t = text.lower()
    # heuristic: contains 'empirical' and evidence of study/evaluation
    if 'empirical' not in t:
        return False
    if any(k in t for k in ['we conducted', 'we present a study', 'user study', 'field study', 'participants', 'interview', 'survey', 'experiment', 'evaluation']):
        return True
    return True

rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    yr = extract_year(text)
    emp = is_empirical(text)
    rows.append({'title': title, 'year': yr, 'empirical': emp})

df_docs = pd.DataFrame(rows)

df_cits = pd.DataFrame(cits)
if not df_cits.empty:
    df_cits['total_citations'] = pd.to_numeric(df_cits['total_citations'], errors='coerce')

# filter criteria
f = df_docs[(df_docs['empirical']==True) & (df_docs['year'].notna()) & (df_docs['year']>2016)]

# join
out = f.merge(df_cits, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])
res = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res, ensure_ascii=False))"""

env_args = {'var_call_QKx5xGUKcYCoT2Ejy3NYZNtc': 'file_storage/call_QKx5xGUKcYCoT2Ejy3NYZNtc.json', 'var_call_4oUO2WpjgT0D6C24HXPKnhoT': 'file_storage/call_4oUO2WpjgT0D6C24HXPKnhoT.json'}

exec(code, env_args)
