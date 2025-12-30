code = """import re, json
import pandas as pd

# Load full citations data
path = var_call_2ZxW3LCyZ3PMVOQHwdgjifY2
with open(path, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)

# Load full paper docs data
path_docs = var_call_R6WBCMetXnn5O1mOWG5pjP8i
with open(path_docs, 'r') as f:
    docs = json.load(f)

rows = []
for d in docs:
    text = d.get('text', '') or ''
    # crude year extraction: look for 2016
    year = 2016 if '2016' in text else None
    if year != 2016:
        continue
    # domain filter: contains 'physical activity' (case-insensitive)
    if re.search(r'physical activity', text, re.IGNORECASE):
        title = d.get('filename', '').replace('.txt','')
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates('title')

if papers_df.empty:
    result = []
else:
    merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title', 'total_citations']]
    result = merged.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_R6WBCMetXnn5O1mOWG5pjP8i': 'file_storage/call_R6WBCMetXnn5O1mOWG5pjP8i.json', 'var_call_2ZxW3LCyZ3PMVOQHwdgjifY2': 'file_storage/call_2ZxW3LCyZ3PMVOQHwdgjifY2.json'}

exec(code, env_args)
