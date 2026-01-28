code = """import json, re

# Load data
with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# normalize title
def norm_title(t):
    if t is None:
        return ''
    s = str(t).strip()
    if len(s) > 0 and s[0] in ("'", '"'):
        s = s[1:]
    if len(s) > 0 and s[-1] in ("'", '"'):
        s = s[:-1]
    return s.strip().lower()

# build citation map
cit_map = {}
for c in citations:
    t = c.get('title', '')
    tot = c.get('total_citations', 0)
    try:
        tot_i = int(tot)
    except Exception:
        try:
            tot_i = int(str(tot).strip())
        except Exception:
            tot_i = 0
    cit_map[norm_title(t)] = tot_i

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
    results.append({'title': title, 'total_citations': cit_map.get(norm_title(title), 0)})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json', 'var_call_mAbq0VBhcWHcGWwAPGfTBtxu': {'docs_count': 35, 'citations_count': 252}}

exec(code, env_args)
