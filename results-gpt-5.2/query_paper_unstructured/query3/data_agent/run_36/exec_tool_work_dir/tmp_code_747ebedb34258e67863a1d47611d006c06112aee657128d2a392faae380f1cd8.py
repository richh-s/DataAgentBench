code = """import json, re
import pandas as pd

docs_src = var_call_fWruw89VasDc1xQsR4VIVlXr
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cits_src = var_call_B8K4UO5BTpJMWJ0R1quKYhOE
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src


def extract_year(text):
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(?:19|20)\d{2}', text, flags=re.I)
    if m:
        y = re.search(r'(19|20)\d{2}', m.group(0)).group(0)
        return int(y)
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*\'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    years = [int(x.group(0)) for x in re.finditer(r'\b(?:19|20)\d{2}\b', text)]
    if not years:
        return None
    return min(years)

def extract_contribution(text):
    m = re.search(r'\bcontribution\b\s*[:\-]\s*([^\n\r]+)', text, flags=re.I)
    if m:
        return m.group(1).strip().lower()
    return 'empirical' if re.search(r'\bempirical\b', text, flags=re.I) else ''

recs = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    recs.append({'title': title, 'year': extract_year(text), 'contribution': extract_contribution(text)})

papers = pd.DataFrame(recs)
papers_f = papers[(papers['year'].fillna(0).astype(int) > 2016) & (papers['contribution'].str.contains('empirical', case=False, na=False))]

cits_df = pd.DataFrame(cits)
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce').fillna(0).astype(int)

merged = papers_f.merge(cits_df, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
merged = merged[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(json.dumps(merged.to_dict(orient='records')))"""

env_args = {'var_call_fWruw89VasDc1xQsR4VIVlXr': 'file_storage/call_fWruw89VasDc1xQsR4VIVlXr.json', 'var_call_B8K4UO5BTpJMWJ0R1quKYhOE': 'file_storage/call_B8K4UO5BTpJMWJ0R1quKYhOE.json'}

exec(code, env_args)
