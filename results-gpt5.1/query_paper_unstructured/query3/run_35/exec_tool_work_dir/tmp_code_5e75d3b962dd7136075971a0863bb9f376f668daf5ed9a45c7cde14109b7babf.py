code = """import re, json, pandas as pd
from pathlib import Path

with open(var_call_EULIMl6zDz8YLz2d1z4pg5Sa, 'r') as f:
    papers = json.load(f)
with open(var_call_nOqzOufOsztauC4aXgX8PTr5, 'r') as f:
    cits = json.load(f)

YEAR_RE = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    years = []
    for match in YEAR_RE.finditer(text):
        y = int(match.group(0))
        years.append(y)
    for y in years:
        if y >= 2000:
            return y
    return None

records = []
for doc in papers:
    text = doc.get('text','')
    year = extract_year(text)
    if not year or year <= 2016:
        continue
    if 'empirical' not in text.lower():
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cits_df = pd.DataFrame(cits)
# ensure correct dtypes
cits_df['total_citations'] = cits_df['total_citations'].astype(int)

merged = papers_df.merge(cits_df, on='title', how='left')

result = merged[['title','total_citations']].fillna(0)
result['total_citations'] = result['total_citations'].astype(int)

out = result.to_json(orient='records')
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EULIMl6zDz8YLz2d1z4pg5Sa': 'file_storage/call_EULIMl6zDz8YLz2d1z4pg5Sa.json', 'var_call_nOqzOufOsztauC4aXgX8PTr5': 'file_storage/call_nOqzOufOsztauC4aXgX8PTr5.json', 'var_call_SpMrtl3x5iaBtpTU72ah6cRs': ['title', 'total_citations']}

exec(code, env_args)
