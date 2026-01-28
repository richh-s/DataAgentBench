code = """import re, json, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_IyDkDb7QZpHWf75TYouqsjR2, 'r') as f:
    papers = json.load(f)
with open(var_call_AxQbFSvOCcPA3FNUBE4at7jH, 'r') as f:
    citations = json.load(f)

# Extract title (from filename) and publication year from text
records = []
for doc in papers:
    text = doc.get('text', '')
    # Heuristic: look for 2016 in a year-like context
    if not re.search(r'2016', text):
        continue
    # Skip if domain not physical activity
    if not re.search(r'physical activity', text, re.IGNORECASE):
        continue
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    # Try to confirm pub year = 2016 by looking for "2016" near venue header
    if not re.search(r"'16| 2016", text):
        # if explicit 2015 etc, skip
        if re.search(r" 2014| 2015| 2013| 2012", text):
            continue
    pub_year = 2016
    records.append({'title': title, 'pub_year': pub_year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(cit_df, papers_df, left_on='title', right_on='title', how='inner')

result = merged[['title', 'total_citations']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IyDkDb7QZpHWf75TYouqsjR2': 'file_storage/call_IyDkDb7QZpHWf75TYouqsjR2.json', 'var_call_AxQbFSvOCcPA3FNUBE4at7jH': 'file_storage/call_AxQbFSvOCcPA3FNUBE4at7jH.json'}

exec(code, env_args)
