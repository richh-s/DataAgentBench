code = """import re, json, os, json as js
import pandas as pd


def load_var(name):
    val = name
    if isinstance(val, str) and os.path.isfile(val):
        with open(val, 'r') as f:
            return js.load(f)
    return val

papers = load_var(var_call_2bKqeoRvFThFA0LVCty3rEoV)
citations = load_var(var_call_CUyaDzkmuLyaHJzlKyDP8D7o)

records = []
year_pattern = re.compile(r"CHI (20[0-2][0-9])|\b(20[0-2][0-9]|19[9][0-9])\b")

for doc in papers:
    text = doc.get('text','')
    if 'empirical' not in text.lower():
        continue
    years = []
    for m in year_pattern.findall(text):
        if m[0]:
            years.append(int(m[0]))
        elif m[1]:
            years.append(int(m[1]))
    pub_year = None
    for y in sorted(set(years)):
        if 1990 <= y <= 2025:
            pub_year = y
            break
    if not pub_year or pub_year <= 2016:
        continue
    title = doc.get('filename','').rsplit('.txt',1)[0]
    records.append({'title': title, 'year': pub_year})

papers_df = pd.DataFrame(records).drop_duplicates(subset=['title'])

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(cit_df, papers_df, on='title', how='inner')

result = merged[['title','total_citations']].sort_values('title').to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_2bKqeoRvFThFA0LVCty3rEoV': 'file_storage/call_2bKqeoRvFThFA0LVCty3rEoV.json', 'var_call_CUyaDzkmuLyaHJzlKyDP8D7o': 'file_storage/call_CUyaDzkmuLyaHJzlKyDP8D7o.json'}

exec(code, env_args)
