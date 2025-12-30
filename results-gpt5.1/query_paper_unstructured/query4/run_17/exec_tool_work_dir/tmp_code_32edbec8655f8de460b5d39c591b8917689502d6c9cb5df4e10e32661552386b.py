code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
path_docs = Path(var_call_s6StjNXAPEn1HJbe1LZBPSnS)
import json as _json
with path_docs.open() as f:
    docs = _json.load(f)

# Extract year from text (first 4-digit year that looks like 20xx or 19xx in typical CHI header)
records = []
for d in docs:
    text = d.get('text','')
    # heuristic: search for 2016 explicitly first
    year = None
    m = re.search(r'2016', text)
    if m:
        year = 2016
    else:
        m2 = re.search(r'20(1[0-9]|2[0-9])', text)
        if m2:
            year = int(m2.group(0))
    title = d.get('filename','').replace('.txt','')
    # domain filter: physical activity mentions
    if re.search(r'physical activity', text, re.I):
        records.append({'title': title, 'year': year})

# Deduplicate titles, keeping year=2016 if present
by_title = {}
for r in records:
    t = r['title']
    y = r['year']
    if t not in by_title or (by_title[t] is None and y is not None) or (y == 2016 and by_title[t] != 2016):
        by_title[t] = y

phys_act_2016 = [t for t,y in by_title.items() if y == 2016]

# Load citations
path_cit = Path(var_call_OoyQnSrCWMx7L2rAw7d2CEg9)
with path_cit.open() as f:
    cits = _json.load(f)

cit_df = pd.DataFrame(cits)

# Some titles in citations may be quoted; normalize
cit_df['norm_title'] = cit_df['title'].str.replace('^"|"$','', regex=True)

result_rows = []
for t in phys_act_2016:
    matches = cit_df[cit_df['norm_title'] == t]
    if not matches.empty:
        total = int(matches['total_citations'].astype(int).sum())
        result_rows.append({'title': t, 'total_citations': total})

result = json.dumps(result_rows)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_s6StjNXAPEn1HJbe1LZBPSnS': 'file_storage/call_s6StjNXAPEn1HJbe1LZBPSnS.json', 'var_call_OoyQnSrCWMx7L2rAw7d2CEg9': 'file_storage/call_OoyQnSrCWMx7L2rAw7d2CEg9.json'}

exec(code, env_args)
