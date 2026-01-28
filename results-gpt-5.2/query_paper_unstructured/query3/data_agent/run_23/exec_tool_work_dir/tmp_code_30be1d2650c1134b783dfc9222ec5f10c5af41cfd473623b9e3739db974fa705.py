code = """import json, re, pandas as pd

mongo_path = var_call_8vEW7lVoN6kzXxvCW81JTN0L
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

cit_path = var_call_VcrI2tjrrfCudHexjwRqMOky
if isinstance(cit_path, str) and cit_path.endswith('.json'):
    with open(cit_path, 'r', encoding='utf-8') as f:
        cites = json.load(f)
else:
    cites = var_call_VcrI2tjrrfCudHexjwRqMOky

def extract_year(text):
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})', text or '', flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r'\b(19\d{2}|20\d{2})\b\s*ACM\b', text or '', flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*'?\s*(\d{2})\b", text or '')
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    head = (text or '')[:2000]
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', head)]
    years = [y for y in years if 1990 <= y <= 2026]
    return min(years) if years else None

def has_empirical_contribution(text):
    t = (text or '').lower()
    patterns = [
        r'\\bcontribution\\s*[:\\-]\\s*[^\\n]*empirical\\b',
        r'\\bcontributions\\s*[:\\-]\\s*[^\\n]*empirical\\b',
        r'\\btype\\s*of\\s*contribution\\s*[:\\-]\\s*[^\\n]*empirical\\b',
        r'\\bempirical\\s+study\\b',
        r'\\bwe\\s+(conduct|present|report)\\s+an\\s+empirical\\b'
    ]
    return any(re.search(p, t, flags=re.IGNORECASE) for p in patterns)

papers = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    empirical = has_empirical_contribution(text)
    papers.append({'title': title, 'year': year, 'empirical': empirical})

pdf = pd.DataFrame(papers)
pdf_f = pdf[(pdf['empirical'] == True) & (pdf['year'].notna()) & (pdf['year'] > 2016)].copy()

cdf = pd.DataFrame(cites)
cdf['citation_count'] = pd.to_numeric(cdf['citation_count'], errors='coerce').fillna(0).astype(int)

tot = cdf.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})

out = pdf_f.merge(tot, on='title', how='left')
out['total_citation_count'] = out['total_citation_count'].fillna(0).astype(int)

out = out[['title','total_citation_count']].sort_values(['total_citation_count','title'], ascending=[False, True])
result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8vEW7lVoN6kzXxvCW81JTN0L': 'file_storage/call_8vEW7lVoN6kzXxvCW81JTN0L.json', 'var_call_VcrI2tjrrfCudHexjwRqMOky': 'file_storage/call_VcrI2tjrrfCudHexjwRqMOky.json'}

exec(code, env_args)
