code = """import json, re
import pandas as pd

# Load mongo docs (may be file path)
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

# Extract year and contribution from text using heuristics

year_patterns = [
    re.compile(r'\b(?:19|20)\d{2}\b'),
]

def extract_year(text):
    # Prefer explicit Copyright year
    m = re.search(r'Copyright\s*(?:\(c\))?\s*(?:19|20)\d{2}', text, flags=re.I)
    if m:
        y = re.search(r'(19|20)\d{2}', m.group(0)).group(0)
        return int(y)
    # Then ACM/IEEE style: year near venue line like CHI '17 etc
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|Ubicomp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    # Else pick earliest plausible year after 2010? Actually publication year likely earliest year in header; take min >=1990
    years = [int(x.group(0)) for x in re.finditer(r'\b(19|20)\d{2}\b', text)]
    if not years:
        return None
    # Heuristic: publication year tends to be min of years in doc
    return min(years)

def extract_contribution(text):
    # Look for 'Contribution:' line
    m = re.search(r'\bcontribution\b\s*[:\-]\s*([^\n\r]+)', text, flags=re.I)
    if m:
        return m.group(1).strip().lower()
    # Look for keywords in some metadata section (domain/source/venue/contribution)
    # fallback: simple contains
    return 'empirical' if re.search(r'\bempirical\b', text, flags=re.I) else ''

recs = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    contrib = extract_contribution(text)
    recs.append({'title': title, 'year': year, 'contribution': contrib})

papers = pd.DataFrame(recs)
# Filter empirical and after 2016
papers_f = papers[(papers['year'].fillna(0).astype(int) > 2016) & (papers['contribution'].str.contains('empirical', case=False, na=False))]

cits_df = pd.DataFrame(cits)
# total_citations may be string
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce').fillna(0).astype(int)

merged = papers_f.merge(cits_df, on='title', how='left')
merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
merged = merged[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = merged.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fWruw89VasDc1xQsR4VIVlXr': 'file_storage/call_fWruw89VasDc1xQsR4VIVlXr.json', 'var_call_B8K4UO5BTpJMWJ0R1quKYhOE': 'file_storage/call_B8K4UO5BTpJMWJ0R1quKYhOE.json'}

exec(code, env_args)
