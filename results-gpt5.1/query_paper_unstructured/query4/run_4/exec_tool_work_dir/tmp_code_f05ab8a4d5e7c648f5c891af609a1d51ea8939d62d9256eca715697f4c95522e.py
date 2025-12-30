code = """import re, json
import pandas as pd

# Load full Mongo results
path = var_call_2af0Ig6P1JqAn6pC7A5pWUYz
with open(path, 'r') as f:
    mongo_records = json.load(f)

# Extract title (filename without .txt), year, and detect physical activity domain via heuristic
papers = []
for doc in mongo_records:
    filename = doc.get('filename','')
    text = doc.get('text','')
    title = re.sub(r'\.txt$', '', filename)
    # year: look for 2016 explicitly in text (e.g., CHI 2016, © 2016, 2016 ACM etc.)
    year_match = re.search(r'2016', text)
    year = 2016 if year_match else None
    if year != 2016:
        continue
    # domain: check if phrase physical activity appears anywhere
    if re.search(r'physical activity', text, re.IGNORECASE):
        papers.append({'title': title})

# Load citation aggregates
path2 = var_call_S7rRiRU6gGjocPSr6NjcB118
with open(path2, 'r') as f:
    cit_records = json.load(f)

cit_df = pd.DataFrame(cit_records)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

pa_titles = [p['title'] for p in papers]
res_df = cit_df[cit_df['title'].isin(pa_titles)][['title','total_citations']].sort_values('title')

result = res_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_2af0Ig6P1JqAn6pC7A5pWUYz': 'file_storage/call_2af0Ig6P1JqAn6pC7A5pWUYz.json', 'var_call_S7rRiRU6gGjocPSr6NjcB118': 'file_storage/call_S7rRiRU6gGjocPSr6NjcB118.json'}

exec(code, env_args)
