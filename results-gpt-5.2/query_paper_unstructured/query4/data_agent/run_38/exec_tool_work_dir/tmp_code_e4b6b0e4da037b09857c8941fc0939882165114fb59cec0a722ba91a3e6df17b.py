code = """import json

path_docs = var_call_HMibItbSybVlZOrOudCMaRUr
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

pa_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = (d.get('text') or '').lower()
    if '2016' not in text:
        continue
    if 'physical activity' not in (title.lower() + ' ' + text):
        continue
    pa_titles.add(title)

path_cit = var_call_pDRTPsGZdBN8y5Mri3wCsXzf
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

cit_map = {r['title']: int(r['total_citations']) for r in cits}

out = [{'title': t, 'total_citations': cit_map.get(t)} for t in sorted(pa_titles)]
out = [r for r in out if r['total_citations'] is not None]

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_HMibItbSybVlZOrOudCMaRUr': 'file_storage/call_HMibItbSybVlZOrOudCMaRUr.json', 'var_call_pDRTPsGZdBN8y5Mri3wCsXzf': 'file_storage/call_pDRTPsGZdBN8y5Mri3wCsXzf.json'}

exec(code, env_args)
