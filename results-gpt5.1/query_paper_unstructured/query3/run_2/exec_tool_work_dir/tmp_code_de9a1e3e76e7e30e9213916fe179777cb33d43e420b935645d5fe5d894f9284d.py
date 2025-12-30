code = """import re, json, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_uLJTeZlWKZHjQvuNomf3W3Tj, 'r') as f:
    papers = json.load(f)
with open(var_call_YQ0mViRvzGEZnCPDnLPVtPTJ, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text (look for CHI 2018, 2019, etc. or copyright year)
year_pattern = re.compile(r'\b(20[0-2][0-9])\b')
venue_pattern = re.compile(r'CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH', re.I)

records = []
for doc in papers:
    text = doc.get('text', '')
    # contribution: must contain 'empirical'
    if 'empirical' not in text.lower():
        continue
    years = [int(y) for y in year_pattern.findall(text)]
    year = min(years) if years else None
    if year is None or year <= 2016:
        continue
    m = venue_pattern.search(text)
    venue = m.group(0) if m else None
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year, 'venue': venue})

papers_df = pd.DataFrame(records)

cites_df = pd.DataFrame(citations)
# clean citation counts and titles
cites_df['total_citations'] = cites_df['total_citations'].astype(int)
cites_df['title_clean'] = cites_df['title'].str.strip('"')

merged = papers_df.merge(cites_df, left_on='title', right_on='title_clean', how='left')

result = merged[['title','total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_uLJTeZlWKZHjQvuNomf3W3Tj': 'file_storage/call_uLJTeZlWKZHjQvuNomf3W3Tj.json', 'var_call_YQ0mViRvzGEZnCPDnLPVtPTJ': 'file_storage/call_YQ0mViRvzGEZnCPDnLPVtPTJ.json'}

exec(code, env_args)
