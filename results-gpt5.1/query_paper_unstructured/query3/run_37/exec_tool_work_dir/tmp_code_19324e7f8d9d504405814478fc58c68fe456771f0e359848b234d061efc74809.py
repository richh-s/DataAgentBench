code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo result
file_path = var_call_84SGQ8Me2ejiogflvWvf0gHj
with open(file_path, 'r') as f:
    mongo_records = json.load(f)

# Extract title (from filename) and approximate year and contribution
rows = []
for doc in mongo_records:
    filename = doc.get('filename', '')
    text = doc.get('text', '') or ''
    title = filename.replace('.txt','')
    # heuristic year search
    years = re.findall(r'20[0-9]{2}', text)
    year = None
    if years:
        year = int(years[0])
    # contribution heuristic: look for 'contribution' section or keywords
    contrib = None
    lower = text.lower()
    if 'empirical' in lower:
        contrib = 'empirical'
    rows.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(rows)

# Filter empirical and year>2016
empirical_recent = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)]

# Load citation aggregates
file_path2 = var_call_qW3hSyDrZH5DB6sWvBRgYIGY
with open(file_path2, 'r') as f:
    citation_records = json.load(f)

cites_df = pd.DataFrame(citation_records)
# normalize types
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

# Join on title
merged = empirical_recent.merge(cites_df, on='title', how='inner')

result = merged[['title','total_citations']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_84SGQ8Me2ejiogflvWvf0gHj': 'file_storage/call_84SGQ8Me2ejiogflvWvf0gHj.json', 'var_call_qW3hSyDrZH5DB6sWvBRgYIGY': 'file_storage/call_qW3hSyDrZH5DB6sWvBRgYIGY.json'}

exec(code, env_args)
