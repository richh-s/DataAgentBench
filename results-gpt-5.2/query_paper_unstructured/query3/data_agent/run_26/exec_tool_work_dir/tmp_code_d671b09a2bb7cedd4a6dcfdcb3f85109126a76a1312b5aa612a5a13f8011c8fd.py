code = """import json, re, pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_maybe(var_call_cGNpJrb5mlG7PhBiApeTNq8p)
citations = load_maybe(var_call_7HNGUbHkem8Ywi94tXTm0DLD)

year_pat = re.compile(r"\b(19\d{2}|20\d{2})\b")

def extract_year(text):
    head = (text or '')[:5000]
    years = [int(y) for y in year_pat.findall(head)]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    from collections import Counter
    c = Counter(years)
    top = max(c.values())
    cand = [y for y,v in c.items() if v==top]
    return max(cand)

empirical_indicators = [
    r"\bparticipants\b", r"\bstudy\b", r"\bwe conducted\b",
    r"\binterview\b", r"\bsurvey\b", r"\bexperiment\b", r"\bfield study\b", r"\buser study\b"
]
empirical_pat = re.compile(r"|".join(empirical_indicators), re.IGNORECASE)

def is_empirical(text):
    t = (text or '')[:12000]
    m = re.search(r"contribution\s*[:\-]\s*([^\n]+)", t[:8000], flags=re.IGNORECASE)
    if m and 'empirical' in m.group(1).lower():
        return True
    return bool(empirical_pat.search(t))

rows = []
for d in paper_docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    rows.append({'title': title, 'pub_year': extract_year(text), 'empirical': is_empirical(text)})

papers_df = pd.DataFrame(rows)
papers_f = papers_df[(papers_df['empirical'] == True) & (papers_df['pub_year'].notna()) & (papers_df['pub_year'] > 2016)].copy()

cit_df = pd.DataFrame(citations)
cit_df['citation_count'] = pd.to_numeric(cit_df.get('citation_count'), errors='coerce').fillna(0).astype(int)

cit_total = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

out = papers_f.merge(cit_total, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)

out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True]).reset_index(drop=True)

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_cGNpJrb5mlG7PhBiApeTNq8p': 'file_storage/call_cGNpJrb5mlG7PhBiApeTNq8p.json', 'var_call_7HNGUbHkem8Ywi94tXTm0DLD': 'file_storage/call_7HNGUbHkem8Ywi94tXTm0DLD.json'}

exec(code, env_args)
