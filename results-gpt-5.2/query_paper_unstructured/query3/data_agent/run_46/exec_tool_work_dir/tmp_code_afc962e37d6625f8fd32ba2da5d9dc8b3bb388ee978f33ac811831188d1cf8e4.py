code = """import json, re, pandas as pd

# Load filenames+texts
path = var_call_tceA0ijmJOUOkbKam3TWFmL6
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Heuristic extraction of publication year from header/copyright lines
year_patterns = [
    re.compile(r"\bCHI\s*'?\s*(\d{2})\b"),
]

def extract_year(text):
    # prefer explicit 4-digit years between 2000-2026 near top
    head = text[:2500]
    yrs = [int(y) for y in re.findall(r"\b(20\d{2})\b", head)]
    # remove likely citation_year occurrences? in head typically pub year.
    if yrs:
        # choose most frequent; tie -> max
        from collections import Counter
        c = Counter(yrs)
        m = max(c.values())
        cand = [y for y,v in c.items() if v==m]
        return max(cand)
    return None

# Determine contribution contains 'empirical'

def has_empirical(text):
    return re.search(r"\bempirical\b", text, flags=re.IGNORECASE) is not None

rows=[]
for d in docs:
    title = d['filename'].rsplit('.txt',1)[0]
    text = d.get('text','') or ''
    if not has_empirical(text):
        continue
    year = extract_year(text)
    if year is None or year<=2016:
        continue
    rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

# Load citations
cit_path = var_call_KqWpDGKnYGXGtW0dbCqmSD8r
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)
    # total citations across all years
    tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
else:
    tot = pd.DataFrame(columns=['title','total_citations'])

out = papers_df.merge(tot, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict('records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8i47lMSYBgdOkF2dYzuuZIpo': 'file_storage/call_8i47lMSYBgdOkF2dYzuuZIpo.json', 'var_call_KqWpDGKnYGXGtW0dbCqmSD8r': 'file_storage/call_KqWpDGKnYGXGtW0dbCqmSD8r.json', 'var_call_tceA0ijmJOUOkbKam3TWFmL6': 'file_storage/call_tceA0ijmJOUOkbKam3TWFmL6.json'}

exec(code, env_args)
