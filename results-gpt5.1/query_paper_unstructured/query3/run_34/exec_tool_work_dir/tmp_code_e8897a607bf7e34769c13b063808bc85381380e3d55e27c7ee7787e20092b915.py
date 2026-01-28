code = """import re, json
import pandas as pd

# Load full Mongo and SQLite results
mongo_path = var_call_9c8KG0T3EbdOXzTs9FF7LNJP
sql_path = var_call_d2ZdtbKgYAqkTDQT3dG7Moav

with open(mongo_path, 'r') as f:
    mongo_records = json.load(f)
with open(sql_path, 'r') as f:
    sql_records = json.load(f)

# Extract year from text (look for patterns like CHI 2018, 2019, etc.)
records = []
for doc in mongo_records:
    text = doc.get('text', '')
    # Search for a 4-digit year between 2017 and 2025 near venue indicators or copyright lines
    years = re.findall(r'(20[1-2][0-9])', text)
    year_val = None
    for y in years:
        yi = int(y)
        if 2010 <= yi <= 2025:
            year_val = yi
            break
    # Determine contribution using simple heuristic: look in abstract/intro for the word 'empirical'
    # We'll assume any paper containing 'empirical' in text is an empirical contribution
    contrib = 'empirical' if re.search(r'empirical', text, re.IGNORECASE) else None
    if contrib == 'empirical' and year_val is not None and year_val > 2016:
        filename = doc.get('filename', '')
        title = re.sub(r'\.txt$', '', filename)
        records.append({'title': title, 'year': year_val})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(sql_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

# Some titles in SQL may be quoted; strip leading/trailing quotes
cit_df['title_clean'] = cit_df['title'].str.strip('"')
papers_df['title_clean'] = papers_df['title']

merged = pd.merge(papers_df, cit_df, on='title_clean', how='left')

result = merged[['title', 'total_citations']].dropna(subset=['total_citations']).sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9c8KG0T3EbdOXzTs9FF7LNJP': 'file_storage/call_9c8KG0T3EbdOXzTs9FF7LNJP.json', 'var_call_d2ZdtbKgYAqkTDQT3dG7Moav': 'file_storage/call_d2ZdtbKgYAqkTDQT3dG7Moav.json'}

exec(code, env_args)
