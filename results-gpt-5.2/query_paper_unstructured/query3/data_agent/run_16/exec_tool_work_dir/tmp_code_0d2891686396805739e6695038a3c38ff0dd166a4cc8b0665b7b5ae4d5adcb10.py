code = """import json, re, pandas as pd

# Load mongo docs (may be file path)
docs_src = var_call_vhzoJOixzxQpdd67O3hQZxiy
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cit_src = var_call_2C4nNIHvmKQbHXCkNSOUrHEq
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cit_src

# Parse year + contribution from text

def extract_year(text):
    if not text:
        return None
    # Prefer explicit copyright year
    m = re.search(r'Copyright\s*(?:\(c\)\s*)?(?:\u00a9\s*)?(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # ACM/IEEE style year near venue like CHI '18 etc.
    m = re.search(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|TEI|OzCHI|WWW|AH)\b\s*['’]?(\d{2})\b", text, flags=re.IGNORECASE)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    # Any 4-digit year, take first plausible in 2000s/late 1990s
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', text)]
    for y in years:
        if 1995 <= y <= 2026:
            return y
    return None


def has_empirical_contribution(text):
    if not text:
        return False
    # Look for metadata-like field
    if re.search(r'\bcontribution\b\s*[:\-]\s*[^\n]*\bempirical\b', text, flags=re.IGNORECASE):
        return True
    # Otherwise, accept if empirical appears in early part (likely abstract/keywords/metadata)
    head = text[:5000]
    return bool(re.search(r'\bempirical\b', head, flags=re.IGNORECASE))

rows = []
for d in docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    year = extract_year(text)
    emp = has_empirical_contribution(text)
    rows.append({'title': title, 'year': year, 'empirical': emp})

papers_df = pd.DataFrame(rows)
emp_after = papers_df[(papers_df['empirical']==True) & (papers_df['year'].notna()) & (papers_df['year']>2016)][['title','year']]

cits_df = pd.DataFrame(cits)
# total_citations might be string
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = emp_after.merge(cits_df, on='title', how='inner')
out = out[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_vhzoJOixzxQpdd67O3hQZxiy': 'file_storage/call_vhzoJOixzxQpdd67O3hQZxiy.json', 'var_call_2C4nNIHvmKQbHXCkNSOUrHEq': 'file_storage/call_2C4nNIHvmKQbHXCkNSOUrHEq.json'}

exec(code, env_args)
