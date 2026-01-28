code = """import json, pandas as pd, re

# Load full Mongo result
path = var_call_SsZCeNF82c6ql85sKJbtvAAq
with open(path, 'r') as f:
    papers = json.load(f)

# Extract empirical papers after 2016
records = []
for doc in papers:
    if not isinstance(doc, dict):
        continue
    filename = doc.get('filename','')
    if not filename:
        continue
    title = re.sub(r"\.txt$","", filename)
    text = doc.get('text','') or ''
    years = re.findall(r"20[0-3][0-9]", text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2030:
            year = yi
            break
    if year is None or year <= 2016:
        continue
    if 'empirical' not in text.lower():
        continue
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

# Load citations aggregation result (already JSON-serializable list)
cites = var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf
cites_df = pd.DataFrame(list(cites))

cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = pd.merge(papers_df, cites_df, on='title', how='left')

result = merged[['title','total_citations']].sort_values('title').to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_SsZCeNF82c6ql85sKJbtvAAq': 'file_storage/call_SsZCeNF82c6ql85sKJbtvAAq.json', 'var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf': 'file_storage/call_3RdIKm8ph6IZ0OYZ2XeC4Znf.json'}

exec(code, env_args)
