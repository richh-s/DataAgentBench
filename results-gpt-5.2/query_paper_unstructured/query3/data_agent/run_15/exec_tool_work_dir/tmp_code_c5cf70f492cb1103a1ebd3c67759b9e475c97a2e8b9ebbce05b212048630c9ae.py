code = """import json, re
import pandas as pd

# Load mongo docs
mongo_src = var_call_UIRwr2U4MyuSEl9NJjOigeCX
if isinstance(mongo_src, str):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_src

# Load citations
cit_src = var_call_6Fy3O0K8mqwRY9gAdhjmuS8i
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_src


def extract_year(text):
    # common patterns like "CHI '19" or "UBICOMP '15" handled; but need >=2017
    m = re.search(r"\b(20\d{2})\b", text)
    if m:
        return int(m.group(1))
    # fallback: apostrophe year e.g., '17
    m = re.search(r"\b['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    return None


def has_empirical(text):
    t = text.lower()
    # heuristic: presence of user study / experiment / survey / interview; but require explicit empirical keyword per question
    return 'empirical' in t

rows = []
for d in mongo_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical(text):
        continue
    rows.append({'title': title, 'pub_year': year})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Total citations across all years
if papers_df.empty:
    out = []
else:
    totals = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    merged = papers_df.merge(totals, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_UIRwr2U4MyuSEl9NJjOigeCX': 'file_storage/call_UIRwr2U4MyuSEl9NJjOigeCX.json', 'var_call_6Fy3O0K8mqwRY9gAdhjmuS8i': 'file_storage/call_6Fy3O0K8mqwRY9gAdhjmuS8i.json'}

exec(code, env_args)
