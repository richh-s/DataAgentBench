code = """import re, json
import pandas as pd

# Load full Mongo and citations results
with open(var_call_8vtfZdGYy91w4z7S9C8RDcHl, 'r') as f:
    mongo_records = json.load(f)
with open(var_call_8pvydBcSWBMCVjIGSvEATzTp, 'r') as f:
    cit_records = json.load(f)

# Extract year and mark empirical contribution
papers = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    # Heuristic: find 4-digit year 19xx or 20xx near venue line like 'CHI 2018'
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    if year and year > 2016:
        papers.append({'title': title, 'year': year, 'contribution_empirical': True})

papers_df = pd.DataFrame(papers).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(papers_df, cit_df, on='title', how='inner')
result = merged[['title', 'total_citations']].sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_8vtfZdGYy91w4z7S9C8RDcHl': 'file_storage/call_8vtfZdGYy91w4z7S9C8RDcHl.json', 'var_call_8pvydBcSWBMCVjIGSvEATzTp': 'file_storage/call_8pvydBcSWBMCVjIGSvEATzTp.json'}

exec(code, env_args)
