code = """import re, json
import pandas as pd

# Load full results if stored as file paths
import os, json as js

def load_var(maybe_path):
    if isinstance(maybe_path, str) and os.path.isfile(maybe_path):
        with open(maybe_path, 'r') as f:
            return js.load(f)
    return maybe_path

papers = load_var(var_call_2bKqeoRvFThFA0LVCty3rEo)
citations = load_var(var_call_CUyaDzkmuLyaHJzlKyDP8D7o)

# Extract title (from filename) and year (from text) and filter empirical contributions
records = []
year_pattern = re.compile(r'\b(20[0-2][0-9]|19[9][0-9])\b')

for doc in papers:
    text = doc.get('text','')
    if 'empirical' not in text.lower():
        continue
    years = [int(y) for y in year_pattern.findall(text)]
    pub_year = None
    for y in sorted(set(years)):
        if 1990 <= y <= 2025:
            pub_year = y
            break
    if not pub_year or pub_year <= 2016:
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': pub_year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(cit_df, papers_df, on='title', how='inner')

result = merged[['title','total_citations']].sort_values('title').to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_2bKqeoRvFThFA0LVCty3rEoV': 'file_storage/call_2bKqeoRvFThFA0LVCty3rEoV.json', 'var_call_CUyaDzkmuLyaHJzlKyDP8D7o': 'file_storage/call_CUyaDzkmuLyaHJzlKyDP8D7o.json'}

exec(code, env_args)
