code = """import re, json, pandas as pd

path_docs = var_call_OXAfTPovk7spUY3tNrAz4jv5
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r"\.txt$","", filename).strip()
    text = d.get('text','')
    year_match = re.search(r"CHI\s+20(\d{2})", text)
    if not year_match:
        year_match = re.search(r"20(1[0-9]|2[0-9])", text)
    year = int(year_match.group(0)) if year_match else None
    if re.search(r"empirical", text, re.I):
        contribution = 'empirical'
    else:
        contribution = None
    if year and year > 2016 and contribution == 'empirical':
        records.append({'title': title, 'year': year})

path_cit = var_call_LOgffYrPQQUOI5MCOHiRdNsI
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
if 'title' not in cit_df.columns:
    result = records
else:
    cit_df['clean_title'] = cit_df['title'].str.replace('^"|"$', '', regex=True)
    emp_df = pd.DataFrame(records)
    merged = emp_df.merge(cit_df, left_on='title', right_on='clean_title', how='left')
    result = merged[['title','year','total_citations']].sort_values(['year','title']).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OXAfTPovk7spUY3tNrAz4jv5': 'file_storage/call_OXAfTPovk7spUY3tNrAz4jv5.json', 'var_call_LOgffYrPQQUOI5MCOHiRdNsI': 'file_storage/call_LOgffYrPQQUOI5MCOHiRdNsI.json'}

exec(code, env_args)
