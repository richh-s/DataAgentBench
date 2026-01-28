code = """import json, re
import pandas as pd

path_docs = var_call_E45dgkpCoxaWAr3U85uEBNV5
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_cit = var_call_aG6IT16wCr82mSBjjC7TnIKa
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

def extract_year(text):
    m = re.search(r'Copyright\s*(?:\(c\)|\u00a9)?\s*(19\d{2}|20\d{2})', text, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|TEI|OzCHI|WWW|PervasiveHealth)\s*['’](\d{2})\b", text)
    if m:
        yy = int(m.group(1))
        return 2000 + yy if yy <= 30 else 1900 + yy
    head = text[:2000]
    years = re.findall(r'\b(19\d{2}|20\d{2})\b', head)
    if years:
        yrs = [int(y) for y in years]
        yrs = [y for y in yrs if 1990 <= y <= 2026]
        if yrs:
            return sorted(yrs)[0]
    return None

def extract_contribution_blob(text):
    m = re.search(r'\bcontribution\s*[:\-]\s*([^\n\r]+)', text, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip().lower()
    return text.lower()

rows = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    year = extract_year(text)
    contrib_blob = extract_contribution_blob(text)
    is_empirical = 'empirical' in contrib_blob
    rows.append({'title': title, 'year': year, 'empirical': is_empirical})

df_docs = pd.DataFrame(rows)
filtered = df_docs[(df_docs['empirical'] == True) & (df_docs['year'].notna()) & (df_docs['year'] > 2016)].copy()

res = filtered.merge(df_cit, on='title', how='left')
res['total_citations'] = res['total_citations'].fillna(0).astype(int)
res = res[['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_E45dgkpCoxaWAr3U85uEBNV5': 'file_storage/call_E45dgkpCoxaWAr3U85uEBNV5.json', 'var_call_aG6IT16wCr82mSBjjC7TnIKa': 'file_storage/call_aG6IT16wCr82mSBjjC7TnIKa.json'}

exec(code, env_args)
