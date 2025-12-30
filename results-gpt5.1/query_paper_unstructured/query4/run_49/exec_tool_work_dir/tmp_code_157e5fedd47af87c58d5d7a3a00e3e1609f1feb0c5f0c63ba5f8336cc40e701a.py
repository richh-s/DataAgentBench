code = """import re, json
import pandas as pd

# Load full citation aggregates
path_citations = var_call_UnYguBMs4FZY1Doh5PexitLF
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs preview file (assume full set there)
path_docs = var_call_sjnY0UOS5MX5YjawsW9isZTr
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text', '')
    # year: look for 2016
    if '2016' not in text:
        continue
    # domain physical activity (substring, case-insensitive)
    if re.search(r'physical activity', text, re.IGNORECASE) is None:
        continue
    title = d.get('filename','').replace('.txt','')
    records.append({'title': title})

# Deduplicate
titles = sorted({r['title'] for r in records})

# Build citation map
cmap = {c['title']: int(c['total_citations']) for c in citations}

result = []
for t in titles:
    if t in cmap:
        result.append({'title': t, 'total_citations': cmap[t]})

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_sjnY0UOS5MX5YjawsW9isZTr': 'file_storage/call_sjnY0UOS5MX5YjawsW9isZTr.json', 'var_call_UnYguBMs4FZY1Doh5PexitLF': 'file_storage/call_UnYguBMs4FZY1Doh5PexitLF.json'}

exec(code, env_args)
