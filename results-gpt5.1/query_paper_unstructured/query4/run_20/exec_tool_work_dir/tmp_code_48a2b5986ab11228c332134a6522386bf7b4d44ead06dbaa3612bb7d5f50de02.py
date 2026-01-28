code = """import re, json
import pandas as pd

# load mongo results from file
path_docs = var_call_ADq7EW2E0Z08yYG3JlzPesmG
with open(path_docs, 'r') as f:
    docs = json.load(f)

# extract title (filename without .txt), year from text using regex for 2016, and filter domain by 'physical activity'
rows = []
for d in docs:
    text = d.get('text','')
    # require year 2016 in text
    if '2016' not in text:
        continue
    # domain physical activity heuristic: phrase present
    if 'physical activity' not in text.lower():
        continue
    filename = d.get('filename','')
    title = re.sub(r'\.txt$','', filename)
    rows.append({'title': title})

papers_df = pd.DataFrame(rows).drop_duplicates()

# load citations aggregated by title
path_cit = var_call_UD86ZCFpneRT2j9PVfrkoiCV
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# join
merged = pd.merge(papers_df, cit_df, on='title', how='left')

result = merged[['title','total_citations']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ADq7EW2E0Z08yYG3JlzPesmG': 'file_storage/call_ADq7EW2E0Z08yYG3JlzPesmG.json', 'var_call_UD86ZCFpneRT2j9PVfrkoiCV': 'file_storage/call_UD86ZCFpneRT2j9PVfrkoiCV.json'}

exec(code, env_args)
