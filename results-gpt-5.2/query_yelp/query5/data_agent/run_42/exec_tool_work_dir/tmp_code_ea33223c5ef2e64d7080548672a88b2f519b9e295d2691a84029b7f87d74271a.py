code = """import json, re, pandas as pd

path = var_call_XHQPp75j7hTfjFCH9ywzKeQd
with open(path, 'r') as f:
    biz = json.load(f)

# match ', ST,' after city or directly after city
state_re = re.compile(r",\s*([A-Z]{2})\s*(?:,|\.)")
rows=[]
for r in biz:
    desc = r.get('description') or ''
    m = state_re.search(desc)
    st = m.group(1) if m else None
    rows.append({'business_id': r.get('business_id'), 'state': st})

df = pd.DataFrame(rows).dropna(subset=['business_id','state'])
us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
df = df[df['state'].isin(us_states)]

counts = df['state'].value_counts()
top_state = counts.index[0]
biz_ids = df.loc[df['state']==top_state,'business_id'].tolist()
refs = ['businessref_'+bid.split('businessid_',1)[1] for bid in biz_ids if isinstance(bid,str) and bid.startswith('businessid_')]

out = {'top_state': top_state, 'wifi_business_count': int(counts.iloc[0]), 'total_refs': len(refs)}
# store refs to file? just output first few
out['refs_preview']=refs[:20]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8vHgR5qYPxufpIJOAW7PW5Cx': [], 'var_call_XHQPp75j7hTfjFCH9ywzKeQd': 'file_storage/call_XHQPp75j7hTfjFCH9ywzKeQd.json', 'var_call_zfbDCe9crYWuOc6XNeywxFo6': {'error': 'No US state parsed from descriptions', 'sample_descriptions': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a ra', 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in th', 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & S', 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations,', 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging f']}}

exec(code, env_args)
