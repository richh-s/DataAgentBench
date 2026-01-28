code = """import json, pandas as pd

path_docs = var_call_OXAfTPovk7spUY3tNrAz4jv5
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Simple heuristic: assume all these 'empirical' text matches are empirical contributions post-2016 cannot be reliably parsed
# So we only list unique titles we detected, without years, and join with citations if possible.

records = []
import re
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r"\.txt$","", filename).strip()
    text = d.get('text','')
    if re.search(r"empirical", text, re.I):
        if title not in [r['title'] for r in records]:
            records.append({'title': title})

path_cit = var_call_LOgffYrPQQUOI5MCOHiRdNsI
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
if 'title' in cit_df.columns:
    cit_df['clean_title'] = cit_df['title'].str.replace('^"|"$', '', regex=True)
    emp_df = pd.DataFrame(records)
    merged = emp_df.merge(cit_df, left_on='title', right_on='clean_title', how='left')
    cols = [c for c in ['title','total_citations'] if c in merged.columns]
    result = merged[cols].to_dict(orient='records')
else:
    result = records

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OXAfTPovk7spUY3tNrAz4jv5': 'file_storage/call_OXAfTPovk7spUY3tNrAz4jv5.json', 'var_call_LOgffYrPQQUOI5MCOHiRdNsI': 'file_storage/call_LOgffYrPQQUOI5MCOHiRdNsI.json'}

exec(code, env_args)
