code = """import json, re, pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_maybe(var_call_cGNpJrb5mlG7PhBiApeTNq8p)
citations = load_maybe(var_call_7HNGUbHkem8Ywi94tXTm0DLD)

# Extract year and contribution from text using simple heuristics
# - year: first occurrence of 4-digit year between 1990-2026 near header/copyright
# - contribution: substring match for 'contribution' line OR keywords indicating empirical study

year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    head = text[:5000]
    years = [int(y) for y in year_pat.findall(head)]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    # choose most frequent; tie -> max (often publication year)
    from collections import Counter
    c = Counter(years)
    top = max(c.values())
    cand = [y for y,v in c.items() if v==top]
    return max(cand)

empirical_indicators = [
    r'\bmethod\b', r'\bmethods\b', r'\bparticipants\b', r'\bstudy\b', r'\bwe conducted\b',
    r'\binterview\b', r'\bsurvey\b', r'\bexperiment\b', r'\bfield study\b', r'\buser study\b'
]
empirical_pat = re.compile('|'.join(empirical_indicators), re.IGNORECASE)

def is_empirical(text):
    # explicit contribution tags if present
    m = re.search(r'contribution\s*[:\-]\s*([^\n]+)', text[:8000], flags=re.IGNORECASE)
    if m and 'empirical' in m.group(1).lower():
        return True
    return bool(empirical_pat.search(text[:12000]))

rows = []
for d in paper_docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    yr = extract_year(text)
    emp = is_empirical(text)
    rows.append({'title': title, 'pub_year': yr, 'empirical': emp})

papers_df = pd.DataFrame(rows)
# filter empirical and pub_year > 2016
papers_f = papers_df[(papers_df['empirical'] == True) & (papers_df['pub_year'].notna()) & (papers_df['pub_year'] > 2016)].copy()

cit_df = pd.DataFrame(citations)
# cast counts
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations per title
cit_total = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = papers_f.merge(cit_total, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True]).reset_index(drop=True)

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cGNpJrb5mlG7PhBiApeTNq8p': 'file_storage/call_cGNpJrb5mlG7PhBiApeTNq8p.json', 'var_call_7HNGUbHkem8Ywi94tXTm0DLD': 'file_storage/call_7HNGUbHkem8Ywi94tXTm0DLD.json'}

exec(code, env_args)
