code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

papers = load_records(var_call_7D71IB9b5byoIC3n4sf6Ll6F)
cits = load_records(var_call_659tsk4v4AqlfjpsZAHm9wT8)

def infer_year(text):
    m = re.search(r'\b(19\d{2}|20\d{2})\b', text)
    if not m:
        return None
    y = int(m.group(1))
    return y

rows = []
for d in papers:
    fn = d.get('filename','')
    title = re.sub(r'\.txt$','', fn)
    text = d.get('text','') or ''
    y = infer_year(text)
    # domain: physical activity must appear as a keyword/topic
    if re.search(r'physical\s+activity', text, flags=re.I):
        if y == 2016:
            rows.append({'title': title})

df_p = pd.DataFrame(rows).drop_duplicates()
df_c = pd.DataFrame(cits)
if not df_p.empty:
    df = df_p.merge(df_c, on='title', how='left')
    df['total_citations'] = pd.to_numeric(df['total_citations'], errors='coerce').fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df[['title','total_citations']].to_dict(orient='records')
else:
    out = []
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7D71IB9b5byoIC3n4sf6Ll6F': 'file_storage/call_7D71IB9b5byoIC3n4sf6Ll6F.json', 'var_call_659tsk4v4AqlfjpsZAHm9wT8': 'file_storage/call_659tsk4v4AqlfjpsZAHm9wT8.json'}

exec(code, env_args)
