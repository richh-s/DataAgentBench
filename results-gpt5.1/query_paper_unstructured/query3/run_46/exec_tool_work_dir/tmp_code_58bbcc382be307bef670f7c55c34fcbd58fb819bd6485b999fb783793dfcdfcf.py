code = """import re, json, pandas as pd

# Load full Mongo result
path = var_call_CXfqzE3MalmRgfugr3bHtiuh
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract title (from filename), year, and whether contribution includes 'empirical'
empirical_titles = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = filename.replace('.txt', '')
    m = re.search(r'CHI\s+([12][0-9]{3})', text)
    if not m:
        m = re.search(r'\b(20[0-9]{2})\b', text)
    year = int(m.group(1)) if m else None
    contrib_match = re.search(r'contribution[s]?[^\n]*empirical|empirical (study|studies|work|evaluation)', text, re.IGNORECASE)
    if year and year > 2016 and contrib_match:
        empirical_titles.append({'title': title, 'year': year})

# Load citations result
path2 = var_call_LxYKyMozaw0f8JNwwt0CPbU9
with open(path2, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
# clean title quotes and ensure numeric
cit_df['title_clean'] = cit_df['title'].str.replace('^"|"$', '', regex=True)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

emp_df = pd.DataFrame(empirical_titles)

merged = emp_df.merge(cit_df, left_on='title', right_on='title_clean', how='left')
result = merged[['title','total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_CXfqzE3MalmRgfugr3bHtiuh': 'file_storage/call_CXfqzE3MalmRgfugr3bHtiuh.json', 'var_call_LxYKyMozaw0f8JNwwt0CPbU9': 'file_storage/call_LxYKyMozaw0f8JNwwt0CPbU9.json'}

exec(code, env_args)
