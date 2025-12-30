code = """import re, json
import pandas as pd

path = var_call_RCZ2qPq0QkuLeMvMxRPFVUP9
with open(path, 'r') as f:
    mongo_records = json.load(f)

rows = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = re.sub(r'\.txt$', '', filename)
    m = re.search(r'20(1[7-9]|2[0-5])', text)
    year = int(m.group(0)) if m else None
    contrib = 'empirical' if re.search(r'empirical', text, re.IGNORECASE) else None
    rows.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(rows)
papers_filt = papers_df[(papers_df['contribution'] == 'empirical') & (papers_df['year'].notna()) & (papers_df['year'] > 2016)]

path2 = var_call_O3OkNIbJMojxiNrVjYbZsFMe
with open(path2, 'r') as f:
    cit_records = json.load(f)

cits_df = pd.DataFrame(cit_records)
if 'total_citations' in cits_df.columns:
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'])

cits_df['title_clean'] = cits_df['title'].str.strip('"')

merged = papers_filt.merge(cits_df, left_on='title', right_on='title_clean', how='inner')

result = merged[['title_clean', 'total_citations']].rename(columns={'title_clean': 'title'}).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RCZ2qPq0QkuLeMvMxRPFVUP9': 'file_storage/call_RCZ2qPq0QkuLeMvMxRPFVUP9.json', 'var_call_O3OkNIbJMojxiNrVjYbZsFMe': 'file_storage/call_O3OkNIbJMojxiNrVjYbZsFMe.json'}

exec(code, env_args)
