code = """import json, re
import pandas as pd

# Load mongo docs from file path
path_docs = var_call_cDCcyZ5sgM0csdzHENl8Id3w
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations totals
path_cit = var_call_MAt8tKz0uDoPcWK1SvuqiFs1
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
# ensure numeric
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# helper extraction
year_re = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    # prioritize copyright year
    m = re.search(r'Copyright\s+(?:\D*?)((?:19|20)\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    # then venue year patterns like CHI '18
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy < 50 else 1900+yy
    # fallback first plausible year in text
    years = [int(y) for y in year_re.findall(text)]
    # year_re with groups returns tuples; fix
    

def extract_year2(text):
    m = re.search(r'Copyright\s+(?:\D*?)((?:19|20)\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|CSCW|UBICOMP|UbiComp|DIS|IUI|WWW|TEI|OzCHI|AH)\s*'\s*(\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000+yy if yy < 50 else 1900+yy
    all_years = re.findall(r'\b((?:19|20)\d{2})\b', text)
    if all_years:
        # take earliest occurrence near start? choose first
        return int(all_years[0])
    return None

def has_empirical(text):
    t = text.lower()
    # match 'empirical' as contribution indicator
    return 'empirical' in t or 'we conducted' in t or 'we ran' in t or 'we present a study' in t

rows=[]
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    yr = extract_year2(text)
    if yr is None or yr <= 2016:
        continue
    if not has_empirical(text):
        continue
    rows.append({'title': title, 'year': yr})

df_docs = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# join with citations
if df_docs.empty:
    out = []
else:
    df = df_docs.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cDCcyZ5sgM0csdzHENl8Id3w': 'file_storage/call_cDCcyZ5sgM0csdzHENl8Id3w.json', 'var_call_MAt8tKz0uDoPcWK1SvuqiFs1': 'file_storage/call_MAt8tKz0uDoPcWK1SvuqiFs1.json'}

exec(code, env_args)
