code = """import json, re, pandas as pd
path = var_call_hYdBVPZoafj93rSXpf5sW6zR
with open(path, 'r', encoding='utf-8') as f:
    citing_recs = json.load(f)

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    m = re.search(r'is (?:owned by|assigned to|belonging to)\s+(.+?)\s+(?:and has|with pub\.|and has publication|and has pub\.|and has publication no\.|and has publication number)', patents_info)
    if m:
        return m.group(1).strip(' .')
    m = re.search(r'^(.+?)\s+holds\s+the\s+', patents_info)
    if m:
        return m.group(1).strip(' .')
    return None

subclass_pat = re.compile(r'^([A-Z]\d{2}[A-Z])')
rows=[]
for r in citing_recs:
    assignee = extract_assignee(r.get('Patents_info',''))
    if not assignee:
        continue
    if assignee.strip().upper()=='UNIV CALIFORNIA':
        continue
    cpc_raw = r.get('cpc')
    if not cpc_raw:
        continue
    try:
        cpcs=json.loads(cpc_raw)
    except Exception:
        cpcs=[]
    for c in cpcs:
        if c.get('first') is True and c.get('code'):
            m=subclass_pat.match(c['code'])
            if m:
                rows.append({'citing_assignee':assignee, 'subclass':m.group(1)})

df=pd.DataFrame(rows)
if len(df)==0:
    out={'pairs':[], 'subclasses':[], 'n_pairs':0, 'n_subclasses':0}
else:
    df=df.drop_duplicates()
    subclasses=sorted(df['subclass'].unique().tolist())
    out={'pairs': df.to_dict(orient='records'), 'subclasses': subclasses, 'n_pairs': int(len(df)), 'n_subclasses': int(len(subclasses))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cGYV4EzbzLcu7btsG54GNN9l': ['publicationinfo'], 'var_call_HljcxoqtuUiRffWjKX9wzs2M': ['cpc_definition'], 'var_call_Wp1cJFhxJ95itKiyJEfq9T95': 'file_storage/call_Wp1cJFhxJ95itKiyJEfq9T95.json', 'var_call_hYdBVPZoafj93rSXpf5sW6zR': 'file_storage/call_hYdBVPZoafj93rSXpf5sW6zR.json'}

exec(code, env_args)
