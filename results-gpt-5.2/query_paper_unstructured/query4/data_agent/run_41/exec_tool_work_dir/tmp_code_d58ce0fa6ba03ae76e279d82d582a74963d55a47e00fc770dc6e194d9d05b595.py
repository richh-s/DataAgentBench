code = """import json, re, pandas as pd

# Load mongo docs result
mongo_res = var_call_eimvXVZwfmwHpS6PgcTtDHnV
if isinstance(mongo_res, str) and mongo_res.endswith('.json'):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_res = json.load(f)

cit_res = var_call_OrW97RBJAFfF1XDwIX6GCqqV
if isinstance(cit_res, str) and cit_res.endswith('.json'):
    with open(cit_res, 'r', encoding='utf-8') as f:
        cit_res = json.load(f)

# Helper to extract year near venue strings
venue_markers = ['CHI', 'CSCW', 'UbiComp', 'Ubicomp', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
pattern_year = re.compile(r'\b(19|20)\d{2}\b')

def extract_pub_year(text):
    # prioritize explicit conference line like "CHI 2016" etc
    for v in venue_markers:
        m = re.search(r'\b' + re.escape(v) + r'\s*(19|20)\d{2}\b', text)
        if m:
            return int(re.search(r'(19|20)\d{2}', m.group(0)).group(0))
    # DOI/ISBN lines may include year; also copyright line
    m = re.search(r'©\s*(19|20)\d{2}', text)
    if m:
        return int(m.group(0).replace('©','').strip())
    m = re.search(r'Copyright\s*(19|20)\d{2}', text, flags=re.IGNORECASE)
    if m:
        y = re.search(r'(19|20)\d{2}', m.group(0)).group(0)
        return int(y)
    # fallback: earliest year in first 2000 chars
    years = [int(y.group(0)) for y in pattern_year.finditer(text[:2000])]
    if years:
        # likely publication year is max within reasonable range 1990-2026 in header; choose most frequent if any
        return max(years)
    return None

rows=[]
for d in mongo_res:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if re.search(r'physical activity', text, flags=re.IGNORECASE) is None:
        continue
    y = extract_pub_year(text)
    rows.append({'title': title, 'pub_year': y})

papers = pd.DataFrame(rows).drop_duplicates(subset=['title'])
# filter to 2016
papers_2016 = papers[papers['pub_year']==2016].copy()

cit_df = pd.DataFrame(cit_res)
if not cit_df.empty:
    # total_citations might be string
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = papers_2016.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_eimvXVZwfmwHpS6PgcTtDHnV': 'file_storage/call_eimvXVZwfmwHpS6PgcTtDHnV.json', 'var_call_OrW97RBJAFfF1XDwIX6GCqqV': 'file_storage/call_OrW97RBJAFfF1XDwIX6GCqqV.json'}

exec(code, env_args)
