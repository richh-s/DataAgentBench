code = """import re, json, pandas as pd

# Load Mongo results file
import pathlib, os, builtins
path = var_call_QRK93mPYMlkyz3zwNNkSxatS
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract title (from filename), year, and infer domain by keyword 'physical activity'
physical_papers = []
for doc in mongo_records:
    text = doc.get('text', '') or ''
    # Year extraction: look for 2016 in the header area (first 1000 chars)
    header = text[:1000]
    year = None
    if '2016' in header:
        year = 2016
    # Domain detection
    if re.search(r'physical activity', text, re.IGNORECASE):
        domain = 'physical activity'
    else:
        domain = None
    if year == 2016 and domain == 'physical activity':
        filename = doc.get('filename','')
        title = re.sub(r'\.txt$', '', filename)
        physical_papers.append({'title': title, 'year': year, 'domain': domain})

# Load citation totals
path2 = var_call_7PK0GYE3zAb5q8Yj6gyv1vw2
with open(path2, 'r') as f2:
    cit_records = json.load(f2)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

phys_df = pd.DataFrame(physical_papers)

if not phys_df.empty:
    merged = phys_df.merge(cit_df, left_on='title', right_on='title', how='left')
    result = merged[['title', 'total_citations']].fillna(0)
    result_list = result.to_dict(orient='records')
else:
    result_list = []

out = json.dumps(result_list)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_QRK93mPYMlkyz3zwNNkSxatS': 'file_storage/call_QRK93mPYMlkyz3zwNNkSxatS.json', 'var_call_7PK0GYE3zAb5q8Yj6gyv1vw2': 'file_storage/call_7PK0GYE3zAb5q8Yj6gyv1vw2.json'}

exec(code, env_args)
