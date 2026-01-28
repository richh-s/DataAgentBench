code = """import json, re
import pandas as pd

_docs_src = var_call_gdpScBbhv5TooWljmDT7Dc6G
if isinstance(_docs_src, str):
    with open(_docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = _docs_src

_cits_src = var_call_2F1arjDMEJ90CApnyrEodfYU
if isinstance(_cits_src, str):
    with open(_cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = _cits_src


def extract_year(text):
    if not text:
        return None
    t = text[:6000]
    m = re.search(r'Copyright\s*(?:©|\(C\)|\u00a9)?\s*(19\d{2}|20\d{2})', t, flags=re.IGNORECASE)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    m = re.search(r'\b(19\d{2}|20\d{2})\b', t)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    return None


def extract_contribution(text):
    if not text:
        return None
    tl = text.lower()
    m = re.search(r'contribution\s*[:\-]\s*([^\n\r]+)', tl)
    if m:
        return m.group(1).strip()
    return None


rows = []
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    contrib = extract_contribution(text)
    l = text.lower()
    inferred_empirical = False
    if l:
        cond1 = ('we conducted' in l) or ('we interviewed' in l) or ('we surveyed' in l) or ('field study' in l) or ('user study' in l) or ('participants' in l)
        cond2 = ('method' in l) or ('methods' in l) or ('results' in l)
        if cond1 and cond2:
            inferred_empirical = True
    rows.append({'title': title, 'year': year, 'contribution_raw': contrib, 'inferred_empirical': inferred_empirical})

papers = pd.DataFrame(rows)
papers['is_empirical'] = papers['contribution_raw'].fillna('').str.contains('empirical', case=False) | papers['inferred_empirical']

papers_f = papers[(papers['year'].notna()) & (papers['year'] > 2016) & (papers['is_empirical'])][['title','year']]

cits_df = pd.DataFrame(cits)
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce')

out = papers_f.merge(cits_df[['title','total_citations']], on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['total_citations','title'], ascending=[False, True])

result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_gdpScBbhv5TooWljmDT7Dc6G': 'file_storage/call_gdpScBbhv5TooWljmDT7Dc6G.json', 'var_call_2F1arjDMEJ90CApnyrEodfYU': 'file_storage/call_2F1arjDMEJ90CApnyrEodfYU.json'}

exec(code, env_args)
