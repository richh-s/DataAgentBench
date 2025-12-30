code = """import re, json
import pandas as pd

# Load full mongo results
path_docs = var_call_rQhO3J8ababzRmEaiUYRdlip
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (from filename), year (from text), and infer domain by keyword
records = []
for d in docs:
    text = d.get('text','')
    # year: look for 2016 explicitly
    year = None
    if re.search(r"2016", text):
        year = 2016
    # domain: check phrase physical activity
    domain = 'physical activity' if re.search(r"physical activity", text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        title = d.get('filename','').rsplit('.txt',1)[0]
        records.append({'title': title, 'year': year, 'domain': domain})

# Load citations aggregation
path_cit = var_call_syR0Ndh1j0mfqkBPI1WLJhad
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
# normalize title quotes
cit_df['title_clean'] = cit_df['title'].str.replace('"','', regex=False)

paper_df = pd.DataFrame(records)
if not paper_df.empty:
    merged = paper_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')
    merged['total_citations'] = merged['total_citations'].astype(float).fillna(0).astype(int)
    out = merged[['title','total_citations']].to_dict(orient='records')
else:
    out = []

res = json.dumps(out)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_rQhO3J8ababzRmEaiUYRdlip': 'file_storage/call_rQhO3J8ababzRmEaiUYRdlip.json', 'var_call_syR0Ndh1j0mfqkBPI1WLJhad': 'file_storage/call_syR0Ndh1j0mfqkBPI1WLJhad.json'}

exec(code, env_args)
