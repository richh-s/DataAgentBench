code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_zxmP2N1ythXvq4sZsdHCsF1q)
rows=[]
for d in docs:
    title = re.sub(r'\.txt$', '', d.get('filename',''))
    text = d.get('text','') or ''
    head = text[:4000]
    years = re.findall(r'\b(20\d{2})\b', head)
    rows.append({'title':title, 'head_years': years[:10], 'head': head})
df=pd.DataFrame(rows)
# count titles where head contains 2016
mask=df['head'].str.contains(r'\b2016\b')
res={'docs_total':len(df), 'docs_head_contains_2016': int(mask.sum())}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ZjAkTSdwoqJbLuHfgc7bUzpj': 'file_storage/call_ZjAkTSdwoqJbLuHfgc7bUzpj.json', 'var_call_zxmP2N1ythXvq4sZsdHCsF1q': 'file_storage/call_zxmP2N1ythXvq4sZsdHCsF1q.json', 'var_call_6xnYjoga4VeUErqVbO2PFFs8': []}

exec(code, env_args)
