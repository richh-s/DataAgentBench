code = """import json, re
import pandas as pd

_docs_src = var_call_ZVTRTOfYo0KRwH0EOJPN5n0u
if isinstance(_docs_src, str) and _docs_src.endswith('.json'):
    with open(_docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = _docs_src

_cits_src = var_call_sTACW57HJkvhSeimKCeE2CNj
if isinstance(_cits_src, str) and _cits_src.endswith('.json'):
    with open(_cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = _cits_src

year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    m = re.search(r'\bCopyright\s+(?:19|20)\d{2}\b', text, flags=re.IGNORECASE)
    if m:
        y = year_re.search(m.group(0))
        return int(y.group(0)) if y else None
    m = re.search(r'\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|TEI|OzCHI|WWW).*?\b((?:19|20)\d{2})\b', text, flags=re.DOTALL)
    if m:
        return int(m.group(1))
    m = year_re.search(text)
    return int(m.group(0)) if m else None

def has_empirical(text):
    t = (text or '').lower()
    return ('empirical' in t)

rows=[]
for d in docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    if not has_empirical(text):
        continue
    rows.append({'title': title, 'year': year})

paper_df = pd.DataFrame(rows).drop_duplicates('title')
cit_df = pd.DataFrame(cits)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

out = paper_df.merge(cit_df, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
out = out.sort_values(['year','title']).reset_index(drop=True)
result = out[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_ZVTRTOfYo0KRwH0EOJPN5n0u': 'file_storage/call_ZVTRTOfYo0KRwH0EOJPN5n0u.json', 'var_call_sTACW57HJkvhSeimKCeE2CNj': 'file_storage/call_sTACW57HJkvhSeimKCeE2CNj.json'}

exec(code, env_args)
