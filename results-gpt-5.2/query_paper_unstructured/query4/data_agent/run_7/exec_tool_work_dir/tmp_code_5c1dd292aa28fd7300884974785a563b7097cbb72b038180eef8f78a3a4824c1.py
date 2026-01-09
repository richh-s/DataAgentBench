code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_json_maybe(var_call_pC8eOP03LXAsJB9K8VKEdsHh)
cit_totals = load_json_maybe(var_call_9jRo7OvxTAhw1OL1wsDaJxGX)

def extract_year(text):
    m = re.search(r'\b(CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*20(\d{2})\b', text, flags=re.I)
    if m:
        return int('20'+m.group(2))
    m = re.search(r'\b(?:Copyright|\u00a9)\s*20(\d{2})\b', text, flags=re.I)
    if m:
        return int('20'+m.group(1))
    head = text[:2000]
    m = re.search(r'\b20(\d{2})\b', head)
    if m:
        return int('20'+m.group(1))
    return None

rows=[]
for d in paper_docs:
    fn = d.get('filename','') or ''
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bphysical activity\b', text, flags=re.I):
        year = extract_year(text)
        if year == 2016:
            rows.append({'title': title})

papers2016 = pd.DataFrame(rows).drop_duplicates()

citdf = pd.DataFrame(cit_totals)
if not citdf.empty:
    # normalize column names just in case
    cols = {c.lower(): c for c in citdf.columns}
    tcol = cols.get('title')
    ccol = cols.get('total_citations')
    if tcol != 'title' and tcol is not None:
        citdf = citdf.rename(columns={tcol:'title'})
    if ccol != 'total_citations' and ccol is not None:
        citdf = citdf.rename(columns={ccol:'total_citations'})

if 'title' not in citdf.columns:
    citdf['title'] = []
if 'total_citations' not in citdf.columns:
    citdf['total_citations'] = []

citdf['total_citations'] = pd.to_numeric(citdf['total_citations'], errors='coerce').fillna(0).astype(int)

if papers2016.empty:
    result = []
else:
    out = papers2016.merge(citdf[['title','total_citations']], on='title', how='left')
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out.sort_values(['total_citations','title'], ascending=[False, True])
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_pC8eOP03LXAsJB9K8VKEdsHh': 'file_storage/call_pC8eOP03LXAsJB9K8VKEdsHh.json', 'var_call_9jRo7OvxTAhw1OL1wsDaJxGX': 'file_storage/call_9jRo7OvxTAhw1OL1wsDaJxGX.json'}

exec(code, env_args)
