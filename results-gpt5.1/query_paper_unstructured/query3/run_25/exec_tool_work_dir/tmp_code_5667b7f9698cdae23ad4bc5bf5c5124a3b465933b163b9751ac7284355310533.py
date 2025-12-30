code = """import re, json, pandas as pd
from datetime import datetime

# Load full Mongo results if needed
path_docs = var_call_pGCtZaOuedlq3zPF1BBnJw8C
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Heuristic year extraction from text
year_pattern = re.compile(r'\b(20[0-2][0-9]|19[9][0-9])\b')

records = []
for d in docs:
    text = d.get('text','')
    years = [int(y) for y in year_pattern.findall(text)]
    pub_year = None
    for y in sorted(set(years)):
        if 1990 <= y <= 2025:
            pub_year = y
            break
    if pub_year is None:
        continue
    if pub_year <= 2016:
        continue
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    # crude contribution detection: look for 'empirical' near 'contribution' or 'we present an empirical' etc.
    if re.search(r'empirical', text, re.IGNORECASE):
        records.append({'title': title, 'year': pub_year})

# Deduplicate by title keeping earliest year
df_emp = pd.DataFrame(records)
if not df_emp.empty:
    df_emp = df_emp.sort_values(['title','year']).drop_duplicates('title', keep='first')

# Load citations aggregation
path_cit = var_call_7INh4qXvTuHsPXGrhA8jx6Ll
with open(path_cit, 'r') as f:
    cit = json.load(f)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'])

# Join on exact title match
if not df_emp.empty and not df_cit.empty:
    result = pd.merge(df_emp, df_cit, how='left', left_on='title', right_on='title')
    result = result[['title','total_citations']].fillna(0)
    result = result.sort_values('title')
    out = result.to_dict(orient='records')
else:
    out = []

res_json = json.dumps(out)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_pGCtZaOuedlq3zPF1BBnJw8C': 'file_storage/call_pGCtZaOuedlq3zPF1BBnJw8C.json', 'var_call_7INh4qXvTuHsPXGrhA8jx6Ll': 'file_storage/call_7INh4qXvTuHsPXGrhA8jx6Ll.json'}

exec(code, env_args)
