code = """import json, re
import pandas as pd

# Load paper docs (may be in a json file path)
docs_src = var_call_ZVTRTOfYo0KRwH0EOJPN5n0u
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

cits_src = var_call_sTACW57HJkvhSeimKCeE2CNj
if isinstance(cits_src, str) and cits_src.endswith('.json'):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

# helpers
year_re = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    # prioritize common copyright / proceedings patterns
    m = re.search(r'\bCopyright\s+(?:19|20)\d{2}\b', text, flags=re.IGNORECASE)
    if m:
        y = year_re.search(m.group(0))
        return int(y.group(0)) if y else None
    m = re.search(r"\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|TEI|OzCHI|WWW)[^\n]{0,40}\b((?:19|20)\d{2})\b", text)
    if m:
        return int(m.group(1))
    m = re.search(r'\b(?:19|20)\d{2}\b', text)
    return int(m.group(0)) if m else None

def has_empirical(text):
    t = text.lower()
    # simple contains matching per hint; look for explicit contribution markers too
    return ('empirical' in t) or ('we conducted' in t) or ('we present a study' in t) or ('user study' in t) or ('field study' in t)

rows=[]
for d in docs:
    fn = d.get('filename','')
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
# normalize totals to int
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
