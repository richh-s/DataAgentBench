code = """import json, re
import pandas as pd

# Load mongo docs
mongo_path = var_call_lgXOXmayMqah0UoPDQC9X5L1
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_year(text):
    if not text:
        return None
    # Look for copyright year
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(\d{4})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Look for common venue header like CHI '18 or UBICOMP '15
    m = re.search(r"\b(?:CHI|UbiComp|UBICOMP|CSCW|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy < 70 else 1900+yy
    # Fallback: any year 2010-2026 near start
    head = text[:2000]
    years = [int(y) for y in re.findall(r'\b(20\d{2})\b', head)]
    if years:
        # pick most frequent, else first
        from collections import Counter
        c = Counter(years)
        return c.most_common(1)[0][0]
    return None

def extract_contribution(text):
    if not text:
        return ''
    # heuristic: if contains 'empirical' treat as empirical contribution
    return 'empirical' if re.search(r'\bempirical\b', text, flags=re.IGNORECASE) else ''

paper_rows = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','',fn)
    text = d.get('text','')
    year = extract_year(text)
    contrib = extract_contribution(text)
    paper_rows.append({'title': title, 'year': year, 'contribution': contrib})

papers = pd.DataFrame(paper_rows)
# filter contribution empirical and year>2016
papers_f = papers[(papers['contribution'].str.contains('empirical', na=False)) & (papers['year'].fillna(0).astype(int) > 2016)]

# citations totals
cit_path = var_call_eavYV7hZUhN7NTcYKJwkBCti
with open(cit_path, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df_c = pd.DataFrame(cits)
df_c['total_citations'] = pd.to_numeric(df_c['total_citations'], errors='coerce').fillna(0).astype(int)

res = papers_f.merge(df_c, on='title', how='inner')[['title','total_citations','year']]
res = res.sort_values(['total_citations','title'], ascending=[False, True])
out = res[['title','total_citations']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lgXOXmayMqah0UoPDQC9X5L1': 'file_storage/call_lgXOXmayMqah0UoPDQC9X5L1.json', 'var_call_eavYV7hZUhN7NTcYKJwkBCti': 'file_storage/call_eavYV7hZUhN7NTcYKJwkBCti.json'}

exec(code, env_args)
