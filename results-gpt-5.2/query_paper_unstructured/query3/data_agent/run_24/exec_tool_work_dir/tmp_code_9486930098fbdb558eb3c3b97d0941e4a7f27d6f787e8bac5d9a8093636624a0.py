code = """import json, re
import pandas as pd

# Load mongo docs (may be in file)
md = var_call_sDhaSXaw90zTvuPc9Zjaoa9O
if isinstance(md, str) and md.endswith('.json'):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_Y1a94LQ7moTHEGS3sPOg0HSH
if isinstance(cit, str) and cit.endswith('.json'):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

# helper to get title from filename

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn).strip() if isinstance(fn, str) else None

# extract year from text
YEAR_RE = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not isinstance(text, str):
        return None
    # Prefer copyright year
    m = re.search(r'Copyright\s*(?:\(c\)|\u00a9)?\s*(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Prefer venue pattern e.g., CHI '17 or UbiComp '18
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    # Fallback: most frequent year in 2000-2026 range
    years = [int(y) for y in YEAR_RE.findall(text)]
    years = [y for y in years if 2000 <= y <= 2026]
    if not years:
        return None
    from collections import Counter
    c = Counter(years)
    return c.most_common(1)[0][0]

# contribution heuristic: look for explicit 'empirical' marker

def has_empirical(text):
    if not isinstance(text, str):
        return False
    return re.search(r'\bempirical\b', text, flags=re.IGNORECASE) is not None

papers = []
for d in md:
    title = title_from_filename(d.get('filename'))
    text = d.get('text','')
    year = extract_year(text)
    empirical = has_empirical(text)
    papers.append({'title': title, 'year': year, 'empirical': empirical})

papers_df = pd.DataFrame(papers).dropna(subset=['title'])
papers_df = papers_df[(papers_df['empirical']) & (papers_df['year'].notna()) & (papers_df['year'] > 2016)]

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citations per title
cit_tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})

res = papers_df[['title']].drop_duplicates().merge(cit_tot, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)
res = res.sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_sDhaSXaw90zTvuPc9Zjaoa9O': 'file_storage/call_sDhaSXaw90zTvuPc9Zjaoa9O.json', 'var_call_Y1a94LQ7moTHEGS3sPOg0HSH': 'file_storage/call_Y1a94LQ7moTHEGS3sPOg0HSH.json'}

exec(code, env_args)
