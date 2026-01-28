code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_zxmP2N1ythXvq4sZsdHCsF1q)

def extract_year_anywhere(t):
    m = re.search(r'\b(20\d{2})\b', t)
    return int(m.group(1)) if m else None

rows=[]
for d in docs:
    title = re.sub(r'\.txt$', '', d.get('filename',''))
    text = d.get('text','') or ''
    y = extract_year_anywhere(text)
    rows.append({'title':title,'year_any':y})
df=pd.DataFrame(rows)
counts=df['year_any'].value_counts(dropna=False).head(20).to_dict()
print('__RESULT__:')
print(json.dumps(counts, default=str))"""

env_args = {'var_call_ZjAkTSdwoqJbLuHfgc7bUzpj': 'file_storage/call_ZjAkTSdwoqJbLuHfgc7bUzpj.json', 'var_call_zxmP2N1ythXvq4sZsdHCsF1q': 'file_storage/call_zxmP2N1ythXvq4sZsdHCsF1q.json', 'var_call_6xnYjoga4VeUErqVbO2PFFs8': [], 'var_call_YLagQu91x1hYidUD5jdPbGwc': {'docs_total': 99, 'docs_head_contains_2016': 0}}

exec(code, env_args)
