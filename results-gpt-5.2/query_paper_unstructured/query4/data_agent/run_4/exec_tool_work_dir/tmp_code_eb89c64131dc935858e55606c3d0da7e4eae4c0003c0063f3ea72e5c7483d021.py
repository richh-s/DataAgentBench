code = """import json, re, pandas as pd

# load filenames+texts
path_docs = var_call_1rPXOD1IbeOs7rgV9oCk5Tbu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load citations
path_cit = var_call_PHs1YTCi9RyIl0q0iydGp7PZ
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

def infer_pub_year(text):
    # look for common ACM/IEEE style year lines near top
    head = text[:3000]
    m = re.search(r"\b(19|20)\d{2}\b", head)
    if not m:
        return None
    # heuristic: choose first year found
    return int(m.group(0))

def has_domain_physical_activity(doc):
    # use keywords section if present; else fallback contains
    t = doc.get('text','')
    head = t[:6000].lower()
    if 'author keywords' in head:
        # take chunk after author keywords
        idx = head.find('author keywords')
        chunk = head[idx:idx+1200]
        return 'physical activity' in chunk
    return 'physical activity' in head

rows=[]
for d in docs:
    title = d['filename'][:-4] if d.get('filename','').endswith('.txt') else d.get('filename')
    if not has_domain_physical_activity(d):
        continue
    year = infer_pub_year(d.get('text',''))
    if year != 2016:
        continue
    rows.append({'title': title, 'pub_year': year})

papers = pd.DataFrame(rows).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(cits)
if len(cit_df):
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations across all citation years
if len(papers)==0:
    out = []
else:
    merged = papers.merge(cit_df[['title','citation_count']], on='title', how='left')
    merged['citation_count'] = merged['citation_count'].fillna(0).astype(int)
    out_df = merged.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    out_df = out_df.sort_values(['total_citations','title'], ascending=[False, True])
    out = out_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ciwq0tFCWCD1wIn1KzMWRPmu': 'file_storage/call_ciwq0tFCWCD1wIn1KzMWRPmu.json', 'var_call_PHs1YTCi9RyIl0q0iydGp7PZ': 'file_storage/call_PHs1YTCi9RyIl0q0iydGp7PZ.json', 'var_call_1rPXOD1IbeOs7rgV9oCk5Tbu': 'file_storage/call_1rPXOD1IbeOs7rgV9oCk5Tbu.json'}

exec(code, env_args)
