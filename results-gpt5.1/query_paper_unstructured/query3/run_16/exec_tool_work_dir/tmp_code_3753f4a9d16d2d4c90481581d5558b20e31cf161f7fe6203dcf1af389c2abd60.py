code = """import re, json
import pandas as pd

# load full mongo result
path = var_call_yU7n6oyG5GOi1ltrGVteuccw
with open(path, 'r') as f:
    papers = json.load(f)

rows = []
for doc in papers:
    text = doc.get('text','')
    # extract year via CHI-style pattern like 'CHI 2018' or standalone 4-digit year 20xx
    year = None
    m = re.search(r'(19|20)\d{2}', text)
    if m:
        year = int(m.group(0))
    # crude contribution detection: presence of 'empirical' in text already filtered; tag as empirical
    contribution = 'empirical'
    title = doc.get('filename','').replace('.txt','')
    rows.append({'title': title, 'year': year, 'contribution': contribution})

papers_df = pd.DataFrame(rows)

# filter empirical and year>2016
empirical_recent = papers_df[(papers_df['contribution'].str.contains('empirical')) & (papers_df['year']>2016)]

# load citations aggregation
path2 = var_call_0hwNYg3W0s0OoyFRgi372BRv
with open(path2,'r') as f:
    cits = json.load(f)

cits_df = pd.DataFrame(cits)
cits_df['total_citations'] = cits_df['total_citations'].astype(int)

merged = empirical_recent.merge(cits_df, how='left', on='title')

result = merged[['title','total_citations']].dropna(subset=['total_citations']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_yU7n6oyG5GOi1ltrGVteuccw': 'file_storage/call_yU7n6oyG5GOi1ltrGVteuccw.json', 'var_call_0hwNYg3W0s0OoyFRgi372BRv': 'file_storage/call_0hwNYg3W0s0OoyFRgi372BRv.json'}

exec(code, env_args)
