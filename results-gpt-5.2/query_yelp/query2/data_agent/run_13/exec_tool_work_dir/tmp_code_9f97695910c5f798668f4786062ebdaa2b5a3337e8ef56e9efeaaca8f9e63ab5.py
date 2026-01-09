code = """import json, re, pandas as pd
path = var_call_ZkkA4ZnjI4eljPSM6zMgMWTR
with open(path,'r') as f:
    biz=json.load(f)

def extract_state(doc):
    st=doc.get('state')
    if st:
        return st
    desc=doc.get('description') or ''
    m=re.search(r',\s*([A-Z]{2})\b', desc)
    return m.group(1) if m else None

rows=[]
for d in biz:
    rc=d.get('review_count')
    try:
        rc=int(rc)
    except Exception:
        rc=None
    rows.append({'state':extract_state(d),'review_count':rc,'business_id':d.get('business_id')})

df=pd.DataFrame(rows)
# keep only 2-letter states
mask=df['state'].apply(lambda x: isinstance(x,str) and len(x)==2)
df=df[mask & df['review_count'].notna()]
state_reviews=df.groupby('state',as_index=False)['review_count'].sum().sort_values('review_count',ascending=False)
if state_reviews.empty:
    out={'error':'no state reviews'}
else:
    top_state=state_reviews.iloc[0]['state']
    top_total=int(state_reviews.iloc[0]['review_count'])
    top_refs=[bid.replace('businessid_','businessref_',1) for bid in df[df['state']==top_state]['business_id'].dropna().unique().tolist()]
    out={'top_state':top_state,'top_total_reviews_from_business_meta':top_total,'top_business_refs':top_refs}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zztlAUKkWO6PCSGpXAC4vrvf': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_t92ai8Wyd4Hsb3FnECZiHhlS': ['checkin', 'business'], 'var_call_KXWQobtv0E88xpJlinKAd6w2': ['review', 'tip', 'user'], 'var_call_ZkkA4ZnjI4eljPSM6zMgMWTR': 'file_storage/call_ZkkA4ZnjI4eljPSM6zMgMWTR.json', 'var_call_xuUzUMrGqNRnbXrB0fOXzJE8': {'top_state': None, 'top_total_reviews_from_business_meta': None, 'top_business_ref_count': 0, 'top_business_refs_sample': []}}

exec(code, env_args)
