code = """import re, json
import pandas as pd

# load full mongo result
path = var_call_CBVCXEsOVfqxCFWYQQt7iNvM
with open(path, 'r') as f:
    papers = json.load(f)

records = []
for doc in papers:
    title = doc.get('filename', '').replace('.txt','')
    text = doc.get('text','')
    # simple year extraction: look for 2016 near 'CHI', 'Ubicomp', etc., else fallback to 2016 if appears
    year = None
    m = re.search(r'\b(20\d{2})\b', text)
    if m:
        year = int(m.group(1))
    domain = None
    if re.search(r'physical activity', text, re.I):
        domain = 'physical activity'
    records.append({'title': title, 'year': year, 'domain': domain})

# filter for 2016 & physical activity
df_papers = pd.DataFrame(records)
fa_2016 = df_papers[(df_papers['year'] == 2016) & (df_papers['domain'] == 'physical activity')]

# load citations summary
path2 = var_call_oVT6RhT9QdgKOvJriw35Hz9w
with open(path2, 'r') as f:
    cits = json.load(f)

df_cits = pd.DataFrame(cits)
# ensure numeric
df_cits['total_citations'] = pd.to_numeric(df_cits['total_citations'])

# join on title
merged = fa_2016.merge(df_cits, on='title', how='left')

result = merged[['title','total_citations']].fillna(0)

out = result.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_CBVCXEsOVfqxCFWYQQt7iNvM': 'file_storage/call_CBVCXEsOVfqxCFWYQQt7iNvM.json', 'var_call_oVT6RhT9QdgKOvJriw35Hz9w': 'file_storage/call_oVT6RhT9QdgKOvJriw35Hz9w.json'}

exec(code, env_args)
