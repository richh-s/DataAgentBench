code = """import re, json, pandas as pd
from pathlib import Path

# Load full mongo results
path = Path(var_call_hSqNQ6fvV01Q7VPIdZBdjwN1)
import json as jsonlib
with path.open() as f:
    mongo_docs = jsonlib.load(f)

# Extract papers with year 2016 and domain containing 'physical activity'
records = []
for doc in mongo_docs:
    text = doc.get('text', '')
    # year: look for 2016
    year_match = re.search(r"2016", text)
    if not year_match:
        continue
    # domain: check phrase 'physical activity'
    if re.search(r"physical activity", text, re.IGNORECASE):
        title = doc.get('filename','').replace('.txt','')
        records.append({'title': title})

# Deduplicate titles
titles = sorted({r['title'] for r in records})

# Load citations aggregate
path2 = Path(var_call_oVSA9if4X5XojaxYslTstn6M)
with path2.open() as f:
    cits = jsonlib.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

res = cit_df[cit_df['title'].isin(titles)][['title','total_citations']]

result = res.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hSqNQ6fvV01Q7VPIdZBdjwN1': 'file_storage/call_hSqNQ6fvV01Q7VPIdZBdjwN1.json', 'var_call_oVSA9if4X5XojaxYslTstn6M': 'file_storage/call_oVSA9if4X5XojaxYslTstn6M.json'}

exec(code, env_args)
