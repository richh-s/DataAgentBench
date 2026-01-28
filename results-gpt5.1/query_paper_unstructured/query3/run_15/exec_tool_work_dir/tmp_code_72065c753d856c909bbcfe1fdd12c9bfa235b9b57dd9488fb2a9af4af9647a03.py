code = """import re, json, pandas as pd

with open(var_call_c7tUt2A91ZGDU2PwVp6CSgZj, 'r') as f:
    papers = json.load(f)
with open(var_call_EVLnousZR6IkuWPvHEZqiFG2, 'r') as f:
    citations = json.load(f)

year_pattern = re.compile(r'\b(20[0-9]{2}|19[0-9]{2})\b')

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text)]
    if not years:
        return None
    cand = [y for y in years if 2000 <= y <= 2025]
    return min(cand) if cand else None

rows = []
for p in papers:
    text = p.get('text', '') or ''
    contrib_match = re.search(r'contribution[s]?[^\n]*', text, re.IGNORECASE)
    has_empirical = False
    if contrib_match:
        seg = contrib_match.group(0)
        if re.search('empirical', seg, re.IGNORECASE):
            has_empirical = True
    if (not has_empirical) and re.search('empirical', text, re.IGNORECASE):
        has_empirical = True
    year = extract_year(text)
    title = (p.get('filename') or '').replace('.txt','')
    rows.append({'title': title, 'year': year, 'has_empirical': has_empirical})

import pandas as pd
paper_df = pd.DataFrame(rows)

paper_emp = paper_df[(paper_df['has_empirical']) & (paper_df['year'].notna()) & (paper_df['year'] > 2016)]

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(paper_emp, cit_df, on='title', how='inner')

result = merged[['title', 'total_citations']].drop_duplicates().sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_c7tUt2A91ZGDU2PwVp6CSgZj': 'file_storage/call_c7tUt2A91ZGDU2PwVp6CSgZj.json', 'var_call_EVLnousZR6IkuWPvHEZqiFG2': 'file_storage/call_EVLnousZR6IkuWPvHEZqiFG2.json'}

exec(code, env_args)
