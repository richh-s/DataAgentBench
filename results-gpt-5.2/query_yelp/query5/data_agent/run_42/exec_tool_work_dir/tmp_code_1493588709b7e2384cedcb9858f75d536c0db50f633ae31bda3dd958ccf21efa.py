code = """import json, re, pandas as pd

path = var_call_XHQPp75j7hTfjFCH9ywzKeQd
with open(path, 'r') as f:
    biz = json.load(f)

state_re = re.compile(r"\bin\s+[A-Za-z .'-]+,\s*([A-Z]{2})\b")
rows=[]
for r in biz:
    desc = r.get('description') or ''
    m = state_re.search(desc)
    st = m.group(1) if m else None
    rows.append({'business_id': r.get('business_id'), 'state': st})

df = pd.DataFrame(rows)

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
df = df.dropna(subset=['business_id','state'])
df = df[df['state'].isin(us_states)]

if df.empty:
    out = {'error':'No US state parsed from descriptions', 'sample_descriptions': [ (biz[i].get('description') or '')[:120] for i in range(min(5,len(biz))) ]}
else:
    counts = df['state'].value_counts()
    top_state = counts.index[0]
    biz_ids = df.loc[df['state']==top_state,'business_id'].tolist()
    refs = ['businessref_'+bid.split('businessid_',1)[1] for bid in biz_ids if isinstance(bid,str) and bid.startswith('businessid_')]
    out = {'top_state': top_state, 'wifi_business_count': int(counts.iloc[0]), 'refs': refs, 'total_refs': len(refs)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8vHgR5qYPxufpIJOAW7PW5Cx': [], 'var_call_XHQPp75j7hTfjFCH9ywzKeQd': 'file_storage/call_XHQPp75j7hTfjFCH9ywzKeQd.json'}

exec(code, env_args)
