code = """import re, json, pandas as pd

# Load full Mongo result
import os, json as jsonlib
path = var_call_j5eDEAGE3lGywLaWlrT2IrCy
with open(path, 'r') as f:
    mongo_records = jsonlib.load(f)

# Extract metadata (title, year, contribution) heuristically
papers = []
for doc in mongo_records:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = re.sub(r'\.txt$', '', filename)
    # year: look for 20xx or 19xx, pick earliest >=2000
    years = re.findall(r'(19|20)\d{2}', text)
    year = None
    for y in years:
        y_full = int(''.join(y)) if isinstance(y, tuple) else int(y)
        if y_full >= 2000:
            year = y_full
            break
    # contribution: check for word 'empirical'
    contrib = 'empirical' if re.search(r'empirical', text, re.I) else None
    papers.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(papers)
empirical_df = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)]

# Load citations aggregated
path2 = var_call_HuRvCzqgX6fwkSqmbd4rgjD0
with open(path2, 'r') as f:
    cit_records = jsonlib.load(f)

cits_df = pd.DataFrame(cit_records)
# convert total_citations to int
cits_df['total_citations'] = cits_df['total_citations'].astype(int)

# Join on title
merged = empirical_df.merge(cits_df, on='title', how='left')
result = merged[['title','total_citations']].dropna(subset=['total_citations'])

out = result.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_j5eDEAGE3lGywLaWlrT2IrCy': 'file_storage/call_j5eDEAGE3lGywLaWlrT2IrCy.json', 'var_call_HuRvCzqgX6fwkSqmbd4rgjD0': 'file_storage/call_HuRvCzqgX6fwkSqmbd4rgjD0.json'}

exec(code, env_args)
