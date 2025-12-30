code = """import re, json
import pandas as pd

# load full mongo result
path_docs = var_call_u2QVtN4oBBBO9afCZm2DI2JH
with open(path_docs, 'r') as f:
    docs = json.load(f)

# extract title (from filename), year (from text), and filter: year==2016 & domain contains 'physical activity'
records = []
for d in docs:
    title = d.get('filename','').replace('.txt','')
    text = d.get('text','')
    # year: look for 2016 explicitly
    year_match = re.search(r'2016', text)
    year = 2016 if year_match else None
    # domain physical activity: simple heuristic - phrase appears
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)
    if year == 2016 and domain_match:
        records.append({'title': title})

# unique titles
pa2016_titles = sorted({r['title'] for r in records})

# load citations aggregation
path_cit = var_call_Wln3baMAaWaRwYzuJNWR1PJW
with open(path_cit, 'r') as f:
    cits = json.load(f)

df_cits = pd.DataFrame(cits)

# keep only those titles
df_pa = df_cits[df_cits['title'].isin(pa2016_titles)].copy()

result = df_pa.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_u2QVtN4oBBBO9afCZm2DI2JH': 'file_storage/call_u2QVtN4oBBBO9afCZm2DI2JH.json', 'var_call_Wln3baMAaWaRwYzuJNWR1PJW': 'file_storage/call_Wln3baMAaWaRwYzuJNWR1PJW.json'}

exec(code, env_args)
