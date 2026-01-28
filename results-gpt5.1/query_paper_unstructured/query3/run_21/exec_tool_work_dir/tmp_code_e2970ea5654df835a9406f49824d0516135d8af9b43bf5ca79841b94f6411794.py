code = """import re, json
import pandas as pd

path_docs = var_call_aohdTWCcfjFzZjP3HdoSk4Nr
with open(path_docs, 'r') as f:
    docs = json.load(f)

records = []
for d in docs:
    text = d.get('text','')[:4000]
    m = re.search(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|IUI|OzCHI|TEI|AH)[^\n]{0,40}?(20[0-2][0-9])', text)
    year = None
    if m:
        year = int(m.group(2))
    else:
        m2 = re.search(r'\b(20[0-2][0-9])\b', text)
        if m2:
            year = int(m2.group(1))
    contrib = 'empirical' if re.search(r'empirical', text, re.I) else None
    title = d['filename'].rsplit('.txt',1)[0]
    records.append({'title': title, 'year': year, 'contribution': contrib})

papers_df = pd.DataFrame(records)

cites = var_call_cCot3gLkBAg1ma3sbN5eUO72
cites_df = pd.DataFrame(cites)
cites_df['total_citations'] = cites_df['total_citations'].astype(int)

empirical_titles = papers_df[(papers_df['contribution']=='empirical') & (papers_df['year']>2016)][['title']]

merged = pd.merge(empirical_titles, cites_df, on='title', how='inner')
result = merged[['title','total_citations']].to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_aohdTWCcfjFzZjP3HdoSk4Nr': 'file_storage/call_aohdTWCcfjFzZjP3HdoSk4Nr.json', 'var_call_cCot3gLkBAg1ma3sbN5eUO72': 'file_storage/call_cCot3gLkBAg1ma3sbN5eUO72.json'}

exec(code, env_args)
