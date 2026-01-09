code = """import json, re
import pandas as pd

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cites = load_records(var_call_BcWhDTVY3BnFEfednxP48zAS)
docs = load_records(var_call_pvTCjSMWywozLbTWbJxMrYkz)

# Build set of CHI paper titles from docs by heuristic: venue contains 'CHI' in header lines
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    head = text[:2000]
    if re.search(r'\bCHI\b', head):
        # try to avoid matching OzCHI etc by requiring CHI ' plus year pattern or 'CHI ' followed by apostrophe
        if re.search(r"\bCHI\s*'?\d{2}\b", head) or re.search(r"\bCHI\s*\d{4}\b", head) or re.search(r"\bProceedings of the SIGCHI\b", head):
            chi_titles.add(title)

# Join with citations 2020 and sum counts
rows=[]
for r in cites:
    t=r.get('title')
    if t in chi_titles:
        try:
            cc=int(r.get('citation_count'))
        except Exception:
            cc=0
        rows.append({'title':t,'citation_count_2020':cc})

df=pd.DataFrame(rows)
if df.empty:
    out={'total_citations_2020_for_CHI_papers':0,'num_chi_papers_cited_in_2020':0}
else:
    out={'total_citations_2020_for_CHI_papers':int(df['citation_count_2020'].sum()),
         'num_chi_papers_cited_in_2020':int(df['title'].nunique())}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BcWhDTVY3BnFEfednxP48zAS': 'file_storage/call_BcWhDTVY3BnFEfednxP48zAS.json', 'var_call_pvTCjSMWywozLbTWbJxMrYkz': 'file_storage/call_pvTCjSMWywozLbTWbJxMrYkz.json'}

exec(code, env_args)
