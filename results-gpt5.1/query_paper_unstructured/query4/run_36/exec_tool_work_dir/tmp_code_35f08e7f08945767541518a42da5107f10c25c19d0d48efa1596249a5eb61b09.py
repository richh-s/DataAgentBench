code = """import re, json
import pandas as pd

# Load full paper docs result
path_docs = var_call_oFANxMhtPP2clZNHkW5Astek
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract candidate papers: year 2016 and domain contains 'physical activity'
records = []
for d in docs:
    text = d.get('text', '')
    # year heuristic
    if '2016' not in text:
        continue
    # domain heuristic: look for phrase 'physical activity'
    if re.search(r'physical activity', text, re.IGNORECASE):
        title = d.get('filename', '').replace('.txt','').strip()
        records.append({'title': title})

# Unique titles
titles = sorted({r['title'] for r in records})

# Load citations aggregated
path_cit = var_call_hj9ESzxRlEGR8G2cQwFIpbkX
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

results = []
for t in titles:
    row = cit_df[cit_df['title'] == t]
    if not row.empty:
        total = int(row.iloc[0]['total_citations'])
    else:
        total = None
    results.append({'title': t, 'total_citations': total})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oFANxMhtPP2clZNHkW5Astek': 'file_storage/call_oFANxMhtPP2clZNHkW5Astek.json', 'var_call_hj9ESzxRlEGR8G2cQwFIpbkX': 'file_storage/call_hj9ESzxRlEGR8G2cQwFIpbkX.json'}

exec(code, env_args)
