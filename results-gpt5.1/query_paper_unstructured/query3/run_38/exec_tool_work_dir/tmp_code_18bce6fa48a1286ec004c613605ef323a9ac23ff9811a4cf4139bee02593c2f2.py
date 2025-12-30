code = """import json, pandas as pd, re

# Load full Mongo result
path = var_call_SsZCeNF82c6ql85sKJbtvAAq
with open(path, 'r') as f:
    papers = json.load(f)

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

# Inspect cites structure
cites = var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf

result = json.dumps({'papers_example': papers_df.head(5).to_dict(orient='records'), 'cites_example': cites[:5]})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_SsZCeNF82c6ql85sKJbtvAAq': 'file_storage/call_SsZCeNF82c6ql85sKJbtvAAq.json', 'var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf': 'file_storage/call_3RdIKm8ph6IZ0OYZ2XeC4Znf.json'}

exec(code, env_args)
