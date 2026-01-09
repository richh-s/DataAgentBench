code = """import json, re
import pandas as pd

path_docs = var_call_fctWhpzPaIUkV7suRLsL7LGk
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_cit = var_call_pJUoBOD4gzic997sxqFXbYgW
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
# Normalize citation df columns
if 'title' not in cit_df.columns:
    # attempt to find similar
    for c in cit_df.columns:
        if c.lower()=='title':
            cit_df = cit_df.rename(columns={c:'title'})
            break
if 'total_citations' not in cit_df.columns:
    for c in cit_df.columns:
        if c.lower() in ('total_citations','totalcitation','total'):
            cit_df = cit_df.rename(columns={c:'total_citations'})
            break
cit_df['title'] = cit_df['title'].astype(str)
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

contrib_pat = re.compile(r'\bempirical\b', re.IGNORECASE)
year_pat1 = re.compile(r'\b(19\d{2}|20\d{2})\b')
venue_year_pat = re.compile(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|OzCHI|TEI|WWW|PervasiveHealth)\s*'?\s*(\d{2})\b")

def extract_year(text):
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = venue_year_pat.search(text)
    if m:
        yy = int(m.group((1)))
        return 2000 + yy if yy < 50 else 1900 + yy
    years = [int(y) for y in year_pat1.findall(text)]
    years = [y for y in years if 1990 <= y <= 2026]
    if years:
        return min(years)
    return None

rows=[]
for d in docs:
    t = d.get('filename','')
    if t.lower().endswith('.txt'):
        t = t[:-4]
    text = d.get('text','') or ''
    year = extract_year(text)
    if year is None:
        continue
    if year > 2016 and contrib_pat.search(text):
        rows.append({'title': t, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

out = papers_df.merge(cit_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(json.dumps(out.to_dict(orient='records')))"""

env_args = {'var_call_F6F7FPlZguD3C8fO9BEXO9cQ': 'file_storage/call_F6F7FPlZguD3C8fO9BEXO9cQ.json', 'var_call_pJUoBOD4gzic997sxqFXbYgW': 'file_storage/call_pJUoBOD4gzic997sxqFXbYgW.json', 'var_call_fctWhpzPaIUkV7suRLsL7LGk': 'file_storage/call_fctWhpzPaIUkV7suRLsL7LGk.json'}

exec(code, env_args)
