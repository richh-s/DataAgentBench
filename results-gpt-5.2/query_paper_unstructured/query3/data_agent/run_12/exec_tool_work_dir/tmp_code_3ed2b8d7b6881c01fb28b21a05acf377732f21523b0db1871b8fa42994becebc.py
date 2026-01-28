code = """import json, re
import pandas as pd

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_maybe(var_call_vn3nTXDsXzarlWujBSwTmBHt)
cit_totals = load_maybe(var_call_6V3Z3WKiTXg2i63Ooky3DYYP)

cit_df = pd.DataFrame(cit_totals)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))

contrib_empirical_pat = re.compile(r'\bempirical\b', re.IGNORECASE)
venue_year_pat = re.compile(r'\b(?:CHI|CSCW|UbiComp|UBICOMP|DIS|IUI|WWW|TEI|OzCHI|AH|PervasiveHealth)\b[\s\S]{0,80}?(19\d{2}|20\d{2})', re.IGNORECASE)
year_pat = re.compile(r'\b(19\d{2}|20\d{2})\b')

def extract_year(text):
    if not text:
        return None
    m = venue_year_pat.search(text)
    if m:
        y = int(m.group(1))
        if 1980 <= y <= 2030:
            return y
    for m2 in year_pat.finditer(text[:2000]):
        y = int(m2.group(1))
        if 1980 <= y <= 2030:
            return y
    return None

rows = []
for d in paper_docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if not contrib_empirical_pat.search(text):
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    total_cit = int(cit_map.get(title, 0))
    rows.append({'title': title, 'total_citations': total_cit})

out_df = pd.DataFrame(rows)
if not out_df.empty:
    out_df = out_df.sort_values(['total_citations','title'], ascending=[False, True])
result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_vn3nTXDsXzarlWujBSwTmBHt': 'file_storage/call_vn3nTXDsXzarlWujBSwTmBHt.json', 'var_call_6V3Z3WKiTXg2i63Ooky3DYYP': 'file_storage/call_6V3Z3WKiTXg2i63Ooky3DYYP.json'}

exec(code, env_args)
