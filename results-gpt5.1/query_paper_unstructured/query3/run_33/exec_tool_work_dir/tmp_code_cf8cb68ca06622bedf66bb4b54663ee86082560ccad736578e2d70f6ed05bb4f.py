code = """import re, json
import pandas as pd

# Load full Mongo results
path_docs = var_call_TpAcqHYmKjVXoFyfN5TiXZPq
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title and publication year heuristically
records = []
for d in docs:
    text = d.get('text', '')
    # Heuristic year: look for CHI/other venue year patterns like 'CHI 2018' or standalone 20xx near top
    header = text[:4000]
    m = re.search(r'(19|20)\d{2}', header)
    year = int(m.group(0)) if m else None
    title = d.get('filename','').replace('.txt','').strip()
    # contribution contains 'empirical' via regex match already, but ensure semantic: check word boundary
    if re.search(r'empirical', text, re.I):
        records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])
# Filter year > 2016
papers_df = papers_df[(papers_df['year'].notna()) & (papers_df['year'] > 2016)]

# Load citations
path_cit = var_call_ns5v1vy0pRLCEWmLdanIZxfs
with open(path_cit, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(papers_df, cit_df, on='title', how='inner')

result = merged[['title','total_citations']].sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_TpAcqHYmKjVXoFyfN5TiXZPq': 'file_storage/call_TpAcqHYmKjVXoFyfN5TiXZPq.json', 'var_call_ns5v1vy0pRLCEWmLdanIZxfs': 'file_storage/call_ns5v1vy0pRLCEWmLdanIZxfs.json'}

exec(code, env_args)
