code = """import re, json, pandas as pd

# Load full Mongo result
import os, json as jsonmod
path = var_call_DqnV6D8jaIVAEQBRco2lnQlW
with open(path, 'r') as f:
    mongo_records = jsonmod.load(f)

# Extract year from text (look for 2016) and filter domain by 'physical activity'
physical_papers = []
for doc in mongo_records:
    text = doc.get('text', '')
    # crude year check
    if '2016' not in text:
        continue
    if re.search(r'physical activity', text, re.I):
        title = doc.get('filename', '').replace('.txt','')
        physical_papers.append(title)

# Load citations aggregation
path2 = var_call_ZdgdTjZEw7leSZSa9pY9Zfkw
with open(path2, 'r') as f:
    citation_records = jsonmod.load(f)

cit_df = pd.DataFrame(citation_records)

# Titles in cit_df may be quoted, normalize
cit_df['norm_title'] = cit_df['title'].str.strip('"')

res = cit_df[cit_df['norm_title'].isin(physical_papers)][['norm_title','total_citations']]

result = res.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DqnV6D8jaIVAEQBRco2lnQlW': 'file_storage/call_DqnV6D8jaIVAEQBRco2lnQlW.json', 'var_call_ZdgdTjZEw7leSZSa9pY9Zfkw': 'file_storage/call_ZdgdTjZEw7leSZSa9pY9Zfkw.json'}

exec(code, env_args)
