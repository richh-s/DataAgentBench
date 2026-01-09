code = """import json, re, pandas as pd

# Load paper docs
pdocs = var_call_EEIJ91VXZJGlOphZbVwwYg8L
if isinstance(pdocs, str) and pdocs.endswith('.json'):
    with open(pdocs, 'r', encoding='utf-8') as f:
        pdocs = json.load(f)

# Load citations
cits = var_call_EGgG74giIEL1yTjCWm6wWn3j
if isinstance(cits, str) and cits.endswith('.json'):
    with open(cits, 'r', encoding='utf-8') as f:
        cits = json.load(f)

# helper to extract year and contribution
year_re = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
    # Prefer explicit copyright year
    m = re.search(r"Copyright\s*(?:\u00a9|\(c\))?\s*(19\d{2}|20\d{2})", text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Else look for patterns like 'CHI '18' or 'UBICOMP '15'
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    # Else take earliest year in first 5000 chars
    yrs = [int(y) for y in year_re.findall(text[:5000])]
    if yrs:
        return min(yrs)
    return None


def has_empirical(text):
    t = text.lower()
    # include common empirical-study cues
    keys = ['we conducted', 'we ran', 'we interviewed', 'we surveyed', 'user study', 'field study', 'experiment', 'participants', 'method', 'methods', 'study']
    if any(k in t for k in keys):
        return True
    return False

rows = []
for d in pdocs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    yr = extract_year(text)
    empirical = has_empirical(text)
    if yr is not None and yr > 2016 and empirical:
        rows.append({'title': title, 'year': yr})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

cits_df = pd.DataFrame(cits)
if not cits_df.empty:
    cits_df['citation_count'] = pd.to_numeric(cits_df['citation_count'], errors='coerce').fillna(0).astype(int)
    cits_agg = cits_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    cits_agg = pd.DataFrame(columns=['title','total_citations'])

out = papers_df.merge(cits_agg, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EEIJ91VXZJGlOphZbVwwYg8L': 'file_storage/call_EEIJ91VXZJGlOphZbVwwYg8L.json', 'var_call_EGgG74giIEL1yTjCWm6wWn3j': 'file_storage/call_EGgG74giIEL1yTjCWm6wWn3j.json'}

exec(code, env_args)
