code = """import json, re
import pandas as pd

# Load mongo docs
mongo_src = var_call_E4yrsfAZPPlm4k5jXwq6abl5
if isinstance(mongo_src, str) and mongo_src.endswith('.json'):
    with open(mongo_src, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = mongo_src

# Load citations
cit_src = var_call_YxzUA8LhXuhEO8M7pe577sOu
if isinstance(cit_src, str) and cit_src.endswith('.json'):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit_rows = json.load(f)
else:
    cit_rows = cit_src

# Helper: parse year from text
year_patterns = [
    re.compile(r"\b(?:19|20)\d{2}\b"),
]
venue_markers = ["CHI", "CSCW", "UBICOMP", "UbiComp", "DIS", "IUI", "WWW", "OzCHI", "TEI", "AH", "PervasiveHealth"]

def extract_year(text):
    # Prefer near top
    head = text[:2500]
    candidates = []
    for m in year_patterns[0].finditer(head):
        y = int(m.group(0))
        if 1990 <= y <= 2026:
            candidates.append(y)
    if candidates:
        # often copyright year; take max in head
        return max(candidates)
    # fallback anywhere
    candidates = []
    for m in year_patterns[0].finditer(text):
        y = int(m.group(0))
        if 1990 <= y <= 2026:
            candidates.append(y)
    return max(candidates) if candidates else None

def is_empirical(text):
    t = text.lower()
    # heuristic: presence of study / participants / experiment / survey / interviewed
    empirical_terms = ["participants", "we conducted", "we surveyed", "we interviewed", "user study", "field study", "experiment", "evaluation", "qualitative", "quantitative", "methods", "methodology"]
    return any(term in t for term in empirical_terms)

papers = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    emp = is_empirical(text)
    papers.append({'title': title, 'year': year, 'empirical': emp})

papers_df = pd.DataFrame(papers)
# Filter empirical and after 2016
papers_df = papers_df[(papers_df['empirical']==True) & (papers_df['year'].fillna(0).astype(int) > 2016)]

cit_df = pd.DataFrame(cit_rows)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)
    cit_sum = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citation_count'})
else:
    cit_sum = pd.DataFrame(columns=['title','total_citation_count'])

out = papers_df.merge(cit_sum, on='title', how='left')
out['total_citation_count'] = out['total_citation_count'].fillna(0).astype(int)
out = out[['title','total_citation_count']].sort_values(['total_citation_count','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_E4yrsfAZPPlm4k5jXwq6abl5': 'file_storage/call_E4yrsfAZPPlm4k5jXwq6abl5.json', 'var_call_YxzUA8LhXuhEO8M7pe577sOu': 'file_storage/call_YxzUA8LhXuhEO8M7pe577sOu.json'}

exec(code, env_args)
