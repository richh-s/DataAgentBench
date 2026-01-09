code = """import json, re
import pandas as pd

path_docs = var_call_pONdyw50sb8NZA80JP0fAXqz
with open(path_docs,'r',encoding='utf-8') as f:
    docs = json.load(f)

# classify physical activity domain by presence of exact phrase in keywords/author keywords

def is_physical_activity(text):
    t = (text or '').lower()
    return 'physical activity' in t

def is_published_2016(text):
    t = text or ''
    # look for common headers like CHI '16, Ubicomp '16 etc.
    if re.search(r"\b'16\b", t):
        return True
    if re.search(r"\b2016\b", t):
        # avoid citation years in references by checking first 1200 chars
        return bool(re.search(r"\b2016\b", t[:1500]))
    return False

rows=[]
for d in docs:
    text=d.get('text','')
    if is_physical_activity(text) and is_published_2016(text):
        title=d.get('filename','')
        if title.lower().endswith('.txt'):
            title=title[:-4]
        rows.append({'title':title})

papers=pd.DataFrame(rows).drop_duplicates()

cit=pd.DataFrame(var_call_07x0yUYHFpKHUO0aSEKZ8XxZ)
if not cit.empty:
    cit['total_citations']=cit['total_citations'].astype(int)

if papers.empty:
    out=[]
else:
    res=papers.merge(cit,on='title',how='left')
    res['total_citations']=res['total_citations'].fillna(0).astype(int)
    res=res.sort_values(['total_citations','title'],ascending=[False,True])
    out=res.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dPoUNT5xhNGGm3c8MaJEw98c': 'file_storage/call_dPoUNT5xhNGGm3c8MaJEw98c.json', 'var_call_07x0yUYHFpKHUO0aSEKZ8XxZ': 'file_storage/call_07x0yUYHFpKHUO0aSEKZ8XxZ.json', 'var_call_4chAd5HemSoiqXxUuhBB5aan': [], 'var_call_L3D3qgldH6ZaJrob9qTtR7Lm': 'file_storage/call_L3D3qgldH6ZaJrob9qTtR7Lm.json', 'var_call_pONdyw50sb8NZA80JP0fAXqz': 'file_storage/call_pONdyw50sb8NZA80JP0fAXqz.json'}

exec(code, env_args)
