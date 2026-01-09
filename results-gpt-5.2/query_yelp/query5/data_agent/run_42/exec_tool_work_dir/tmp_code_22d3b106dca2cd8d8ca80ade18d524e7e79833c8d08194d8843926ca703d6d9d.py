code = """import json, re, pandas as pd
from collections import Counter

# load mongo results
path = var_call_XHQPp75j7hTfjFCH9ywzKeQd
with open(path, 'r') as f:
    biz = json.load(f)

# extract US state from description: pattern ' in City, ST,' or end
state_re = re.compile(r"\b[A-Za-z .'-]+,\s*([A-Z]{2})\b")

rows=[]
for r in biz:
    desc = r.get('description') or ''
    m = state_re.search(desc)
    st = m.group(1) if m else None
    rows.append({'business_id': r.get('business_id'), 'state': st})

df = pd.DataFrame(rows).dropna(subset=['business_id','state'])
# keep US states only (exclude Canadian provinces like AB)
us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
df = df[df['state'].isin(us_states)]

# find top state by count
counts = df['state'].value_counts()
top_state = counts.index[0]

# list business ids in that state
biz_ids = df.loc[df['state']==top_state,'business_id'].tolist()

# map to businessref_
refs = ['businessref_'+bid.split('businessid_',1)[1] if isinstance(bid,str) and bid.startswith('businessid_') else None for bid in biz_ids]
refs = [x for x in refs if x]

# chunk refs for SQL IN
chunks = [refs[i:i+5000] for i in range(0,len(refs),5000)]

import duckdb
# we'll query via query_db tool separately; here just output needed artifacts
out = {'top_state': top_state, 'wifi_business_count': int(counts.iloc[0]), 'business_refs': refs[:10], 'total_refs': len(refs)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8vHgR5qYPxufpIJOAW7PW5Cx': [], 'var_call_XHQPp75j7hTfjFCH9ywzKeQd': 'file_storage/call_XHQPp75j7hTfjFCH9ywzKeQd.json'}

exec(code, env_args)
