code = """import re, json, os, pandas as pd

# Load full mongo results
path_docs = var_call_rSyzrSXpBa7z2r2wtF8JEQdF
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (filename without .txt) and approximate year from text
records = []
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r'\.txt$', '', filename)
    text = d.get('text','')
    m = re.search(r'CHI\s+(20\d{2})', text)
    if not m:
        m = re.search(r'(20\d{2})', text)
    year = int(m.group(1)) if m else None
    if year and year > 2016:
        records.append({'title': title, 'year': year})

# Load citations aggregation
path_cits = var_call_SMMD2sXu6oUwSFGhB9wuYt9u
with open(path_cits, 'r') as f:
    cits = json.load(f)

cit_df = pd.DataFrame(cits)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

paper_df = pd.DataFrame(records)

merged = pd.merge(paper_df, cit_df, how='inner', left_on='title', right_on='title')

result = merged[['title','total_citations']].drop_duplicates().to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_rSyzrSXpBa7z2r2wtF8JEQdF': 'file_storage/call_rSyzrSXpBa7z2r2wtF8JEQdF.json', 'var_call_SMMD2sXu6oUwSFGhB9wuYt9u': 'file_storage/call_SMMD2sXu6oUwSFGhB9wuYt9u.json'}

exec(code, env_args)
