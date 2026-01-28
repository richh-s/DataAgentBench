code = """import re, json, pandas as pd, os, json

# Load full mongo results
path_papers = var_call_79bxzr1heficdIt2rZLr441o
with open(path_papers, 'r') as f:
    papers = json.load(f)

# Extract metadata: title from filename, year from text (first 50 lines search for 19xx/20xx), and check contribution contains 'empirical'
records = []
for doc in papers:
    filename = doc.get('filename','')
    text = doc.get('text','') or ''
    title = re.sub(r'\.txt$','', filename)
    # crude year extraction
    m = re.search(r'(19|20)\d{2}', text[:5000])
    year = int(m.group(0)) if m else None
    # contribution heuristic: look for 'empirical' near 'contribution' or in abstract
    contrib = 'empirical' if re.search(r'empirical', text, re.I) else None
    records.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(records)
# Filter empirical and year > 2016
empirical_recent = papers_df[(papers_df['contribution'] == 'empirical') & (papers_df['year'] > 2016)].dropna(subset=['title'])

# Load citations
path_cit = var_call_Mdc1h6O2jwNyZjsJ8k0KI1iD
with open(path_cit, 'r') as f:
    cits = json.load(f)

cits_df = pd.DataFrame(cits)
# clean citations types
cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'])

# Join on title
merged = pd.merge(empirical_recent, cits_df, on='title', how='inner')

result = merged[['title','total_citations']].drop_duplicates().to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_79bxzr1heficdIt2rZLr441o': 'file_storage/call_79bxzr1heficdIt2rZLr441o.json', 'var_call_Mdc1h6O2jwNyZjsJ8k0KI1iD': 'file_storage/call_Mdc1h6O2jwNyZjsJ8k0KI1iD.json'}

exec(code, env_args)
