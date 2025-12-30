code = """import re, json
import pandas as pd

# Load full Mongo results
path = var_call_MbH4fHDXb3sQUWnmrYZzdtFm
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract year, contribution, title
papers = []
for doc in mongo_records:
    text = doc.get('text','')
    # year: look for CHI 2018 style or (C) 2019 etc.
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    # contribution: check if 'empirical' appears near 'contribution' or 'contributions' or in a contributions section
    contrib = None
    lower = text.lower()
    if 'empirical' in lower:
        contrib = 'empirical'
    title = doc.get('filename','').replace('.txt','')
    papers.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(papers)

# filter empirical and year>2016
empirical_recent = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)].dropna(subset=['title'])

# Load citations
path2 = var_call_b8jOwUtRcyaNmBJMeFsNaZ6z
with open(path2, 'r') as f:
    cites = json.load(f)

cites_df = pd.DataFrame(cites)
# clean title quotes and types
cites_df['title'] = cites_df['title'].astype(str).str.replace('"','').str.strip()
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = empirical_recent.merge(cites_df, on='title', how='inner')
result = merged[['title','total_citations']].drop_duplicates().to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MbH4fHDXb3sQUWnmrYZzdtFm': 'file_storage/call_MbH4fHDXb3sQUWnmrYZzdtFm.json', 'var_call_b8jOwUtRcyaNmBJMeFsNaZ6z': 'file_storage/call_b8jOwUtRcyaNmBJMeFsNaZ6z.json'}

exec(code, env_args)
