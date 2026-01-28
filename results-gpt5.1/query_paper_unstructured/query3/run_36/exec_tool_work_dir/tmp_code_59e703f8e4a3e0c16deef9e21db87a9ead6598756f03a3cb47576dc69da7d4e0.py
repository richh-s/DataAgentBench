code = """import re, json, pandas as pd
from datetime import datetime

# Load full results if stored in files
paper_path = var_call_S0PTExgxghOnm3uoZgX1mD5E
cites_path = var_call_W8cOEzND1SanxVZ9MIkWkbzn

with open(paper_path, 'r') as f:
    paper_docs = json.load(f)
with open(cites_path, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
year_pattern = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text)]
    if not years:
        return None
    # Heuristic: take the max year as publication year
    return max(years)

records = []
for doc in paper_docs:
    text = doc.get('text', '') or ''
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    # crude contribution classification via keyword
    contrib = 'empirical' if re.search(r"empirical", text, re.I) else ''
    if 'empirical' not in contrib:
        continue
    title = (doc.get('filename') or '').replace('.txt','')
    if not title:
        continue
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cites_df = pd.DataFrame(citations)
# clean citation counts and aggregate if needed
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = papers_df.merge(cites_df, left_on='title', right_on='title', how='left')

result = merged[['title', 'total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_S0PTExgxghOnm3uoZgX1mD5E': 'file_storage/call_S0PTExgxghOnm3uoZgX1mD5E.json', 'var_call_W8cOEzND1SanxVZ9MIkWkbzn': 'file_storage/call_W8cOEzND1SanxVZ9MIkWkbzn.json'}

exec(code, env_args)
