code = """import re, json
import pandas as pd

# Load full mongo result
path = var_call_u7Fy43KQBrPmKDDN4J1Tz0j7
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract title and year and check contribution
papers = []
for doc in mongo_records:
    text = doc.get('text','')
    # year: look for CHI-style years like 2017, 2018 etc near 'CHI' or general
    years = re.findall(r'(20[0-2][0-9])', text)
    year = None
    if years:
        year = int(min(years))
    # contribution: look for 'contribution' section
    contrib_match = re.search(r'contribution[s]?\s*:?\s*(.+)', text, re.IGNORECASE)
    contrib = contrib_match.group(1).lower() if contrib_match else text.lower()
    if 'empirical' in contrib and year and year > 2016:
        title = doc.get('filename','').replace('.txt','')
        papers.append({'title': title, 'year': year})

# Load citations aggregation
path2 = var_call_KCeMQP6VmRKuk41BWBtJovNh
with open(path2, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

papers_df = pd.DataFrame(papers)

if not papers_df.empty:
    merged = papers_df.merge(cit_df, how='left', left_on='title', right_on='title')
    result = merged[['title','total_citations']].to_dict(orient='records')
else:
    result = []

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_u7Fy43KQBrPmKDDN4J1Tz0j7': 'file_storage/call_u7Fy43KQBrPmKDDN4J1Tz0j7.json', 'var_call_KCeMQP6VmRKuk41BWBtJovNh': 'file_storage/call_KCeMQP6VmRKuk41BWBtJovNh.json'}

exec(code, env_args)
