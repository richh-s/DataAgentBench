code = """import json, re, pandas as pd

def load_tool_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

paper_docs = load_tool_result(var_call_5TgTA5iWZrAxlibQPy6ZRjpO)
citations = load_tool_result(var_call_2D4Q7Qs9rASceSYk4X6EUZcF)

# Extract title/year/contribution from each paper document
# Title from filename

def extract_year(text):
    # Try common patterns: 4-digit years 1990-2026; prefer earliest plausible publication year in header/copyright line
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    years = [y for y in years if 1990 <= y <= 2026]
    if not years:
        return None
    # heuristics: often publication year appears as Copyright 20xx or 'CHI 'xx' etc.
    m = re.search(r'Copyright\s+(?:\([cC]\)\s*)?(19\d{2}|20\d{2})', text)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*'?(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy < 50 else 1900+yy
    return min(years)

def has_empirical(text):
    t = text.lower()
    # contains matching for contribution list or descriptor
    return ('empirical' in t) or ('we conducted' in t and ('study' in t or 'studies' in t or 'experiment' in t or 'interview' in t or 'survey' in t))

rows=[]
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    emp = has_empirical(text)
    if emp and year is not None and year > 2016:
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

cit_df = pd.DataFrame(citations)
if not cit_df.empty:
    cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# total citation count across years
if papers_df.empty or cit_df.empty:
    out=[]
else:
    tot = cit_df.groupby('title', as_index=False)['citation_count'].sum().rename(columns={'citation_count':'total_citations'})
    merged = papers_df.merge(tot, on='title', how='left').fillna({'total_citations':0})
    merged['total_citations'] = merged['total_citations'].astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5TgTA5iWZrAxlibQPy6ZRjpO': 'file_storage/call_5TgTA5iWZrAxlibQPy6ZRjpO.json', 'var_call_2D4Q7Qs9rASceSYk4X6EUZcF': 'file_storage/call_2D4Q7Qs9rASceSYk4X6EUZcF.json'}

exec(code, env_args)
