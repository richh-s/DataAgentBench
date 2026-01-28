code = """import re, json
import pandas as pd

# Load full Mongo result
path = var_call_SsZCeNF82c6ql85sKJbtvAAq
with open(path, 'r') as f:
    papers = json.load(f)

# Extract title (from filename), year, and whether contribution includes 'empirical'
records = []
for doc in papers:
    filename = doc.get('filename','')
    title = re.sub(r"\.txt$","", filename)
    text = doc.get('text','')
    # crude year extraction: first 4-digit year between 2000-2030
    years = re.findall(r"20[0-3][0-9]", text)
    year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2030:
            year = yi
            break
    if year is None:
        continue
    if year <= 2016:
        continue
    # contribution heuristic: look for 'contribution' section mentioning empirical or explicit 'empirical study'
    contrib_text = text.lower()
    if 'empirical' not in contrib_text:
        continue
    # we treat as empirical contribution
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

# Load citations aggregation result
cites = var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf
cites_df = pd.DataFrame(cites)
# total_citations may be string; convert
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(papers_df, cites_df, on='title', how='left')

result = merged[['title','total_citations']].sort_values('title').to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_SsZCeNF82c6ql85sKJbtvAAq': 'file_storage/call_SsZCeNF82c6ql85sKJbtvAAq.json', 'var_call_3RdIKm8ph6IZ0OYZ2XeC4Znf': 'file_storage/call_3RdIKm8ph6IZ0OYZ2XeC4Znf.json'}

exec(code, env_args)
