code = """import json, pandas as pd, re

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cit = load_json_maybe_path(var_call_8iQgmxQZH8dTEoUu9lvnEql0)
docs = load_json_maybe_path(var_call_zgx8u7CePpLHfPFcFNQvWEQv)

# Build set of ACM paper titles from docs via simple heuristic: contains '© ACM' or 'ACM' copyright line
acm_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '')
    if re.search(r'\bACM\b', text) and (('© ACM' in text) or ('Copyright' in text and 'ACM' in text) or ('Request permissions from permissions@acm.org' in text) or ('acm.org' in text)):
        acm_titles.add(title)

# filter citations for those titles
rows=[]
for r in cit:
    title=r.get('title')
    if title in acm_titles:
        try:
            cc=int(r.get('citation_count'))
        except Exception:
            continue
        rows.append(cc)

avg = sum(rows)/len(rows) if rows else None
out = {"acm_papers_with_2018_citations": len(rows), "average_citation_count_2018": avg}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8iQgmxQZH8dTEoUu9lvnEql0': 'file_storage/call_8iQgmxQZH8dTEoUu9lvnEql0.json', 'var_call_zgx8u7CePpLHfPFcFNQvWEQv': 'file_storage/call_zgx8u7CePpLHfPFcFNQvWEQv.json'}

exec(code, env_args)
