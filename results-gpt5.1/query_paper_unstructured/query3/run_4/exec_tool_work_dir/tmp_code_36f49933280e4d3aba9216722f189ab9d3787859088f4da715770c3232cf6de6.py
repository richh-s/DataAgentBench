code = """import re, json
import pandas as pd

# Load full Mongo result
path = var_call_RCZ2qPq0QkuLeMvMxRPFVUP9
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract title, year, contribution flag (empirical?) from text heuristically
rows = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = re.sub(r'\.txt$', '', filename)
    # Year: look for CHI-style lines with years 2017-2025
    m = re.search(r'CHI\s+20(1[7-9]|2[0-5])', text)
    year = None
    if m:
        year = int('20' + m.group(1)[-2:])
    else:
        # fallback: any year 2017-2025 in text
        m2 = re.search(r'20(1[7-9]|2[0-5])', text)
        if m2:
            year = int('20' + m2.group(1)[-2:])
    # contribution: check if word empirical appears near words like study, evaluation, experiment
    contrib = None
    if re.search(r'empirical', text, re.IGNORECASE):
        contrib = 'empirical'
    rows.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(rows)

# Filter empirical and year > 2016
papers_filt = papers_df[(papers_df['contribution'] == 'empirical') & (papers_df['year'].notna()) & (papers_df['year'] > 2016)]

# Load citations
path2 = var_call_O3OkNIbJMojxiNrVjYbZsFMe
with open(path2, 'r') as f:
    cit_records = json.load(f)

cits_df = pd.DataFrame(cit_records)

# Clean titles (some have extra quotes)
cits_df['title_clean'] = cits_df['title'].str.strip('"')

# Join on title
merged = papers_filt.merge(cits_df, left_on='title', right_on='title_clean', how='inner')

result = merged[['title', 'total_citations']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RCZ2qPq0QkuLeMvMxRPFVUP9': 'file_storage/call_RCZ2qPq0QkuLeMvMxRPFVUP9.json', 'var_call_O3OkNIbJMojxiNrVjYbZsFMe': 'file_storage/call_O3OkNIbJMojxiNrVjYbZsFMe.json'}

exec(code, env_args)
