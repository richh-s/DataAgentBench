code = """import re, json, pandas as pd, os, textwrap

# Load full Mongo results
path = var_call_RWSKAOwNzkXv2yHPE7E2yeiy
with open(path, 'r') as f:
    papers = json.load(f)

# Extract metadata: title (from filename), year (from text), contribution (contains 'empirical')
records = []
for doc in papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = re.sub(r'\.txt$', '', filename)
    m = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(m.group(0)) if m else None
    contribution = 'empirical' if re.search(r'empirical', text, re.I) else None
    records.append({'title': title, 'year': year, 'contribution': contribution})

paper_df = pd.DataFrame(records)

# Filter empirical and year>2016
paper_df = paper_df[(paper_df['contribution'] == 'empirical') & (paper_df['year'] > 2016)]

# Load citations aggregate
citations = var_call_VUUhoIJ5Bd2vYHSlOsOvjLQj
if isinstance(citations, str) and os.path.isfile(citations):
    with open(citations, 'r') as f:
        citations = json.load(f)

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(paper_df, cit_df, on='title', how='left')

result = merged[['title', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RWSKAOwNzkXv2yHPE7E2yeiy': 'file_storage/call_RWSKAOwNzkXv2yHPE7E2yeiy.json', 'var_call_VUUhoIJ5Bd2vYHSlOsOvjLQj': 'file_storage/call_VUUhoIJ5Bd2vYHSlOsOvjLQj.json'}

exec(code, env_args)
