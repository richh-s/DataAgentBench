code = """import re, json
import pandas as pd

# load full mongo results
path = var_call_u3XqMjRhfeRjwAOUapo9hu79
with open(path, 'r') as f:
    mongo_docs = json.load(f)

# extract title (filename without .txt), year, domain
records = []
for d in mongo_docs:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','')
    # year: look for 2016
    year = None
    m = re.search(r"2016", text)
    if m:
        year = 2016
    # domain: check for 'physical activity'
    domain = 'physical activity' if re.search(r'physical activity', text, re.I) else None
    if year == 2016 and domain == 'physical activity':
        records.append({'title': title, 'year': year, 'domain': domain})

# load citations aggregation
path2 = var_call_0wDfUPWsFBjQXSHCX4tuj3oM
with open(path2, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(records)
if not papers_df.empty:
    merged = papers_df.merge(cit_df, left_on='title', right_on='title', how='left')
    merged = merged[['title','total_citations']].fillna(0)
    result = merged.to_dict(orient='records')
else:
    result = []

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_u3XqMjRhfeRjwAOUapo9hu79': 'file_storage/call_u3XqMjRhfeRjwAOUapo9hu79.json', 'var_call_0wDfUPWsFBjQXSHCX4tuj3oM': 'file_storage/call_0wDfUPWsFBjQXSHCX4tuj3oM.json'}

exec(code, env_args)
