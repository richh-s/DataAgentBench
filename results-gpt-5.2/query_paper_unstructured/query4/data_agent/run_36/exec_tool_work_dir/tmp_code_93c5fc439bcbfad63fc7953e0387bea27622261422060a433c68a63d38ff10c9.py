code = """import json, re, pandas as pd

# Load mongo paper docs (may be file path)
md = var_call_YHzlVNdKHazjh6rhAoLERLs0
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_ShZfqEIaw8sCHoX6PDPRUZN4
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

# helper to extract year and domain from text
year_patterns = [
    re.compile(r'\b(19\d{2}|20\d{2})\b'),
]

def infer_year(text):
    # prefer explicit copyright year
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # then venue year like CHI '16
    m = re.search(r"\b'?(\d{2})\b", text)
    # too noisy; skip
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    if not years:
        return None
    # heuristic: publication year tends to be min year >=1990 in doc header; take most frequent among first 2000 chars
    head = text[:2000]
    hy = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', head)]
    if hy:
        # choose mode
        from collections import Counter
        c = Counter(hy)
        return int(c.most_common(1)[0][0])
    return int(min(years))

def has_domain_physical_activity(text):
    return re.search(r'physical\s+activity', text, flags=re.IGNORECASE) is not None

papers = []
for d in md:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if not has_domain_physical_activity(text):
        continue
    year = infer_year(text)
    if year == 2016:
        papers.append({'title': title})

papers_df = pd.DataFrame(papers).drop_duplicates()

cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citation count across all citation_years
if papers_df.empty:
    out = []
else:
    tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
    res = papers_df.merge(tot, on='title', how='left')
    res['total_citation_count'] = res['total_citation_count'].fillna(0).astype(int)
    res = res.sort_values(['total_citation_count','title'], ascending=[False, True])
    out = res.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YHzlVNdKHazjh6rhAoLERLs0': 'file_storage/call_YHzlVNdKHazjh6rhAoLERLs0.json', 'var_call_ShZfqEIaw8sCHoX6PDPRUZN4': 'file_storage/call_ShZfqEIaw8sCHoX6PDPRUZN4.json'}

exec(code, env_args)
