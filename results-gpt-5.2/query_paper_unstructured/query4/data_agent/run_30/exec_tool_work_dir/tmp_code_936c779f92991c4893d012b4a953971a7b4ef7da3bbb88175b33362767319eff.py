code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
md = var_call_zYyrGcCxbdn8jeAcpsO8OfVU
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_ld2V1lYUHjPBEP7CbAaRSHh9
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

cit_df = pd.DataFrame(cit)
# coerce totals
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Helper: extract year (best-effort) from first ~2000 chars
year_pat = re.compile(r'\b(19|20)\d{2}\b')

def infer_year(text):
    if not text:
        return None
    head = text[:2500]
    # look for 'Copyright 2016' or '2016' near venue header
    m = re.search(r'Copyright\s+(\d{4})', head, flags=re.I)
    if m:
        return int(m.group(1))
    # ACM/IEEE citation line sometimes includes year after venue
    years = [int(y) for y in year_pat.findall(head)]
    # year_pat.findall returns tuples due to group; fix
    yrs = []
    for m in re.finditer(r'\b(19|20)\d{2}\b', head):
        yrs.append(int(m.group(0)))
    if not yrs:
        return None
    # choose the most frequent, tie -> max
    from collections import Counter
    c = Counter(yrs)
    topn = max(c.values())
    candidates = [y for y,v in c.items() if v==topn]
    return max(candidates)

rows = []
for d in md:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','')
    # domain physical activity heuristic: contains phrase in keywords/abstract
    if re.search(r'physical\s+activity', text, flags=re.I):
        year = infer_year(text)
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')
# filter publication year 2016
papers_2016 = papers_df[papers_df['year']==2016].copy()

# join citations totals
out = papers_2016.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYyrGcCxbdn8jeAcpsO8OfVU': 'file_storage/call_zYyrGcCxbdn8jeAcpsO8OfVU.json', 'var_call_ld2V1lYUHjPBEP7CbAaRSHh9': 'file_storage/call_ld2V1lYUHjPBEP7CbAaRSHh9.json'}

exec(code, env_args)
