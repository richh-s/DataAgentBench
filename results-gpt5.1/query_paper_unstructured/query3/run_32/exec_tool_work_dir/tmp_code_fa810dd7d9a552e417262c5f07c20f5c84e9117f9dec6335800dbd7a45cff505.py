code = """import re, json, pandas as pd

# Load full results from files
with open(var_call_oP8Jo2y8WWNNIfSuV5jJQzLi, 'r') as f:
    papers = json.load(f)
with open(var_call_AUmVEBi7PU2wgq9QWaLuLDJY, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
YEAR_RE = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    years = [int(y) for y in YEAR_RE.findall(text)]
    if not years:
        return None
    # Heuristic: take the most recent year in the text
    return max(years)

records = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # Check contribution type by keyword 'empirical'
    if 'empirical' not in text.lower():
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cites_df = pd.DataFrame(citations)
# citation totals already aggregated
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = papers_df.merge(cites_df, on='title', how='left')
result = merged[['title', 'total_citations']].sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_oP8Jo2y8WWNNIfSuV5jJQzLi': 'file_storage/call_oP8Jo2y8WWNNIfSuV5jJQzLi.json', 'var_call_AUmVEBi7PU2wgq9QWaLuLDJY': 'file_storage/call_AUmVEBi7PU2wgq9QWaLuLDJY.json'}

exec(code, env_args)
