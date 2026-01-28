code = """import json, re
import pandas as pd

# Load mongo docs (filepath)
path_docs = var_call_fctWhpzPaIUkV7suRLsL7LGk
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations totals (filepath)
path_cit = var_call_pJUoBOD4gzic997sxqFXbYgW
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
# coerce total_citations numeric
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Heuristic extract year and contribution
contrib_pat = re.compile(r'\bempirical\b', re.IGNORECASE)

year_pat1 = re.compile(r'\b(19\d{2}|20\d{2})\b')
venue_year_pat = re.compile(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|OzCHI|TEI|WWW|PervasiveHealth)\s*'?\s*(\d{2})\b")

def extract_year(text):
    # try explicit copyright year
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # try venue 'yy pattern
    m = venue_year_pat.search(text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy < 50 else 1900 + yy
    # try common header like "UBICOMP '15" already covered; fallback min year >=2000 if exists
    years = [int(y) for y in year_pat1.findall(text)]
    if years:
        # choose earliest plausible publication year >=1990 and <=2026
        years = [y for y in years if 1990 <= y <= 2026]
        if years:
            return min(years)
    return None

rows = []
for d in docs:
    title = d['filename']
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    year = extract_year(text)
    is_emp = bool(contrib_pat.search(text))
    if year is None:
        continue
    if is_emp and year > 2016:
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

out = papers_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_F6F7FPlZguD3C8fO9BEXO9cQ': 'file_storage/call_F6F7FPlZguD3C8fO9BEXO9cQ.json', 'var_call_pJUoBOD4gzic997sxqFXbYgW': 'file_storage/call_pJUoBOD4gzic997sxqFXbYgW.json', 'var_call_fctWhpzPaIUkV7suRLsL7LGk': 'file_storage/call_fctWhpzPaIUkV7suRLsL7LGk.json'}

exec(code, env_args)
