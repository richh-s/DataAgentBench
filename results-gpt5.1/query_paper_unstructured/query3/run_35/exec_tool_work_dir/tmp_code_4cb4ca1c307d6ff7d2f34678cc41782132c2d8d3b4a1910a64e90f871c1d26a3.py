code = """import re, json, pandas as pd
from pathlib import Path

# Load full results for papers and citations
with open(var_call_EULIMl6zDz8YLz2d1z4pg5Sa, 'r') as f:
    papers = json.load(f)
with open(var_call_nOqzOufOsztauC4aXgX8PTr5, 'r') as f:
    cits = json.load(f)

# Helper to extract year from text (look for CHI 2018 style or (2018) etc.)
YEAR_RE = re.compile(r'(19|20)\d{2}')

def extract_year(text):
    # Look near venue patterns like CHI 2018, CSCW '17 etc.
    # Simplest: first year that appears >=2000
    years = [int(y) for y in YEAR_RE.findall(text)]
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
    # very rough contribution classification: if 'empirical' appears, mark empirical
    if 'empirical' not in text.lower():
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cits_df = pd.DataFrame(cits)
# citation counts are strings per preview, convert
cits_df['total_citations'] = cits_df['total_citations'].astype(int)

# Join on exact title match
merged = papers_df.merge(cits_df, left_on='title', right_on='title', how='left')

result = merged[['title','total_citations']].fillna(0).to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_EULIMl6zDz8YLz2d1z4pg5Sa': 'file_storage/call_EULIMl6zDz8YLz2d1z4pg5Sa.json', 'var_call_nOqzOufOsztauC4aXgX8PTr5': 'file_storage/call_nOqzOufOsztauC4aXgX8PTr5.json'}

exec(code, env_args)
