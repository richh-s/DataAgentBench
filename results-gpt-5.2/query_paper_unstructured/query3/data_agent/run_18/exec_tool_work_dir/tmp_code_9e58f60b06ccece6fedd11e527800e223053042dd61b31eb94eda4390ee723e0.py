code = """import json, re
import pandas as pd

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

paper_docs = load_json(var_call_I3BRW4to4fb67rM4cBqFM4wN)

# Extract title from filename, infer year from text (first occurrence 19xx/20xx within first 4000 chars)
rows = []
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    head = text[:4000]
    years = [int(m.group(1)) for m in year_re.finditer(head)]
    pub_year = None
    # heuristic: choose the smallest year >= 1990 and <= 2026 found in header (often copyright/published)
    cand = [y for y in years if 1990 <= y <= 2026]
    if cand:
        pub_year = min(cand)
    # contribution: empirical if word empirical appears
    contribution_empirical = bool(re.search(r'\bempirical\b', text, flags=re.IGNORECASE))
    rows.append({'title': title, 'year': pub_year, 'empirical': contribution_empirical})

df_papers = pd.DataFrame(rows)

cit_tot = load_json(var_call_qj7b8N68H3AGXsX5VHumii2x)
df_cit = pd.DataFrame(cit_tot)
# coerce citations to int
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# join
merged = df_papers.merge(df_cit, on='title', how='inner')
res = merged[(merged['empirical']) & (merged['year'].fillna(0) > 2016)][['title','total_citations','year']].copy()
res = res.sort_values(['total_citations','title'], ascending=[False, True])
# output list of dicts
out = res[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_AxbFsXVKgoW7w5J0ciY87FQN': 'file_storage/call_AxbFsXVKgoW7w5J0ciY87FQN.json', 'var_call_qj7b8N68H3AGXsX5VHumii2x': 'file_storage/call_qj7b8N68H3AGXsX5VHumii2x.json', 'var_call_I3BRW4to4fb67rM4cBqFM4wN': 'file_storage/call_I3BRW4to4fb67rM4cBqFM4wN.json'}

exec(code, env_args)
