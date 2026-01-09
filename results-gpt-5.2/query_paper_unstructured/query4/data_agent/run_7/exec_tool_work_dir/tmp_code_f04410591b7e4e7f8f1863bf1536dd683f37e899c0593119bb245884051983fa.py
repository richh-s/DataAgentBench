code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

paper_docs = load_json_maybe(var_call_pC8eOP03LXAsJB9K8VKEdsHh)
cit_totals = load_json_maybe(var_call_9jRo7OvxTAhw1OL1wsDaJxGX)

# Heuristic extraction: use filename as title; determine year and domain from text.
# Year: look for patterns like 'CHI 2016' or '2016,' in the header.
# Domain: must contain phrase 'physical activity' (case-insensitive) in text.

def extract_year(text):
    # prioritize explicit venue year like 'CHI 2016' etc.
    m = re.search(r'\b(CHI|UbiComp|Ubicomp|CSCW|DIS|IUI|WWW|TEI|AH|PervasiveHealth|OzCHI)\s*20(\d{2})\b', text, flags=re.I)
    if m:
        return int('20'+m.group(2))
    # generic year in copyright line
    m = re.search(r'\b(?:Copyright|\u00a9)\s*20(\d{2})\b', text, flags=re.I)
    if m:
        return int('20'+m.group(1))
    # fallback: first occurrence of 20xx in first 2000 chars
    head = text[:2000]
    m = re.search(r'\b20(\d{2})\b', head)
    if m:
        return int('20'+m.group(1))
    return None

rows=[]
for d in paper_docs:
    title = d.get('filename','')
    if title.lower().endswith('.txt'):
        title = title[:-4]
    text = d.get('text','') or ''
    if re.search(r'\bphysical activity\b', text, flags=re.I):
        year = extract_year(text)
        if year == 2016:
            rows.append({'title': title})

papers2016 = pd.DataFrame(rows).drop_duplicates()

citdf = pd.DataFrame(cit_totals)
# total_citations may be strings
if not citdf.empty:
    citdf['total_citations'] = pd.to_numeric(citdf['total_citations'], errors='coerce').fillna(0).astype(int)

out = papers2016.merge(citdf, on='title', how='left')
out['total_citations'] = out['total_citations'].fillna(0).astype(int)
# Sort by citations desc then title
out = out.sort_values(['total_citations','title'], ascending=[False, True])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_pC8eOP03LXAsJB9K8VKEdsHh': 'file_storage/call_pC8eOP03LXAsJB9K8VKEdsHh.json', 'var_call_9jRo7OvxTAhw1OL1wsDaJxGX': 'file_storage/call_9jRo7OvxTAhw1OL1wsDaJxGX.json'}

exec(code, env_args)
