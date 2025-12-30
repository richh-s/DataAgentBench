code = """import re, json
import pandas as pd

# Load full mongo results
path = var_call_cl7fNMjxRo9ERA6VUN4rRYCD
with open(path, 'r') as f:
    mongo_docs = json.load(f)

# Extract title (from filename), year, and a heuristic for contribution
records = []
for doc in mongo_docs:
    filename = doc.get('filename','')
    text = doc.get('text','')
    title = filename.replace('.txt','')
    # year: look for CHI style like 'CHI 2018' or a 4-digit year 20xx or 19xx
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group(0)) if year_match else None
    # contribution heuristic: mark empirical if word appears
    contribution = 'empirical' if re.search(r'empirical', text, re.I) else None
    records.append({'title': title, 'year': year, 'contribution': contribution})

papers_df = pd.DataFrame(records)

# Filter empirical and year>2016
filtered_papers = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)].dropna(subset=['title'])

# Load citations aggregation
path2 = var_call_mikNJEBTITE0Vt8vBedqFvcy
with open(path2, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(filtered_papers[['title']].drop_duplicates(), cit_df, on='title', how='left')

result = merged[['title','total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cl7fNMjxRo9ERA6VUN4rRYCD': 'file_storage/call_cl7fNMjxRo9ERA6VUN4rRYCD.json', 'var_call_mikNJEBTITE0Vt8vBedqFvcy': 'file_storage/call_mikNJEBTITE0Vt8vBedqFvcy.json'}

exec(code, env_args)
