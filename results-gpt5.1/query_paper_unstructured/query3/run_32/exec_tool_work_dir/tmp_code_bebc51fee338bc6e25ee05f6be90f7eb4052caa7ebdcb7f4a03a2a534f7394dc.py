code = """import json, pandas as pd, re

with open(var_call_oP8Jo2y8WWNNIfSuV5jJQzLi, 'r') as f:
    papers = json.load(f)
with open(var_call_AUmVEBi7PU2wgq9QWaLuLDJY, 'r') as f:
    citations = json.load(f)

YEAR_RE = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    years = [int(y) for y in YEAR_RE.findall(text)]
    if not years:
        return None
    return max(years)

paper_records = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    if 'empirical' not in text.lower():
        continue
    year = extract_year(text)
    if year is None or year <= 2016:
        continue
    paper_records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(paper_records).drop_duplicates(subset=['title'])

cites_df = pd.DataFrame(citations)
# Ensure correct column names
if 'title' not in cites_df.columns or 'total_citations' not in cites_df.columns:
    raise Exception(str(cites_df.columns))

cites_df['total_citations'] = cites_df['total_citations'].astype(int)

merged = papers_df.merge(cites_df, on='title', how='left')
result = merged[['title', 'total_citations']].sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_oP8Jo2y8WWNNIfSuV5jJQzLi': 'file_storage/call_oP8Jo2y8WWNNIfSuV5jJQzLi.json', 'var_call_AUmVEBi7PU2wgq9QWaLuLDJY': 'file_storage/call_AUmVEBi7PU2wgq9QWaLuLDJY.json', 'var_call_NIR8Urddo7TNHvvT1Oos0USW': {'paper_keys': ['_id', 'filename', 'text'], 'citation_sample': {'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}}}

exec(code, env_args)
