code = """import re, json
import pandas as pd

# Load full mongo results
with open(var_call_IY3qQ3ZO54SiWF2aAJxUKhMc, 'r') as f:
    mongo_records = json.load(f)

# Extract title and year, and check contribution 'empirical'
rows = []
for doc in mongo_records:
    filename = doc.get('filename','')
    title = filename.replace('.txt','')
    text = doc.get('text','')
    # year: look for CHI-style patterns like 'CHI 2018' or any 4-digit between 2000-2025
    year_match = re.search(r'(20[0-2][0-9])', text)
    year = int(year_match.group(1)) if year_match else None
    # contribution: assume if the word 'empirical' appears in contribution sense; we already filtered by regex empirical, but keep flag
    contribution_empirical = bool(re.search(r'empirical', text, re.I))
    if year and year > 2016 and contribution_empirical:
        rows.append({'title': title, 'year': year})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# Load citations aggregated
with open(var_call_NuKM50qsfqSpTRXGp99o9Uf7, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Join on title
merged = pd.merge(papers_df, cit_df, on='title', how='left')
result = merged[['title','total_citations']].sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IY3qQ3ZO54SiWF2aAJxUKhMc': 'file_storage/call_IY3qQ3ZO54SiWF2aAJxUKhMc.json', 'var_call_NuKM50qsfqSpTRXGp99o9Uf7': 'file_storage/call_NuKM50qsfqSpTRXGp99o9Uf7.json'}

exec(code, env_args)
