code = """import re, json
from pathlib import Path

# Load full Mongo and citation results
with open(var_call_f5dPFblpyKfqSYPrjbeHT333, 'r') as f:
    mongo_docs = json.load(f)
with open(var_call_T4EuXct3Aj2YDKox6MboE1Kq, 'r') as f:
    citation_rows = json.load(f)

# Helper to extract year (look for 2016 explicitly)
def infer_year(text):
    return 2016 if '2016' in text else None

results = []
for doc in mongo_docs:
    text = doc.get('text','')
    year = infer_year(text)
    if year != 2016:
        continue
    if 'physical activity' not in text.lower():
        continue
    title = doc.get('filename','').replace('.txt','').strip()
    results.append({'title': title})

# Deduplicate titles
titles_2016_pa = sorted({r['title'] for r in results})

# Build citation map (total over all years)
cit_map = {}
for row in citation_rows:
    t = row['title'].strip()
    if t.startswith('"') and t.endswith('"'):
        t = t[1:-1]
    cit_map[t] = int(row['total_citations'])

final = []
for t in titles_2016_pa:
    final.append({
        'title': t,
        'total_citations': cit_map.get(t, 0)
    })

out = json.dumps(final)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_f5dPFblpyKfqSYPrjbeHT333': 'file_storage/call_f5dPFblpyKfqSYPrjbeHT333.json', 'var_call_T4EuXct3Aj2YDKox6MboE1Kq': 'file_storage/call_T4EuXct3Aj2YDKox6MboE1Kq.json'}

exec(code, env_args)
