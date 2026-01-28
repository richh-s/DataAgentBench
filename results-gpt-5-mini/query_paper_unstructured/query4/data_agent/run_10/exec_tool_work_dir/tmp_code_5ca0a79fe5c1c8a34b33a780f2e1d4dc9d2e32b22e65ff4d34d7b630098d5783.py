code = """import json

with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

cit_map = {}
for rec in citations:
    t = rec.get('title') or ''
    norm = t.strip().strip('\"\'').lower()
    try:
        tot = int(rec.get('total_citations', 0))
    except Exception:
        tot = 0
    cit_map[norm] = tot

results = []
for d in docs:
    text = d.get('text', '')
    if not isinstance(text, str):
        continue
    if 'physical activity' not in text.lower():
        continue
    if '2016' not in text[:1500]:
        continue
    filename = d.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    norm = title.strip().strip('\"\'').lower()
    total = cit_map.get(norm, 0)
    results.append({'title': title, 'total_citations': total})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json', 'var_call_mAbq0VBhcWHcGWwAPGfTBtxu': {'docs_count': 35, 'citations_count': 252}}

exec(code, env_args)
