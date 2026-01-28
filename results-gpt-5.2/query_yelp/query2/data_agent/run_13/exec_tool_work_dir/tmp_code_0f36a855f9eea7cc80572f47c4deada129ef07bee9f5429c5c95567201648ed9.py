code = """import json, re, pandas as pd

# load business docs
path = var_call_ZkkA4ZnjI4eljPSM6zMgMWTR
with open(path, 'r') as f:
    biz = json.load(f)

def extract_state(doc):
    # prefer explicit state field if present
    st = doc.get('state')
    if st:
        return st
    desc = doc.get('description') or ''
    # match ', XX' state code
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    return m.group(1) if m else None

rows=[]
for d in biz:
    rc = d.get('review_count')
    try:
        rc = int(rc)
    except Exception:
        rc = None
    rows.append({
        'business_id': d.get('business_id'),
        'state': extract_state(d),
        'review_count': rc
    })

df = pd.DataFrame(rows).dropna(subset=['state','review_count'])
state_reviews = df.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
if state_reviews.empty:
    out = {'error':'No state/review_count data found'}
else:
    top_state = state_reviews.iloc[0]['state']
    top_total_reviews = int(state_reviews.iloc[0]['review_count'])
    top_business_ids = df.loc[df['state']==top_state, 'business_id'].dropna().unique().tolist()
    # map businessid_ -> businessref_
    top_business_refs = [bid.replace('businessid_','businessref_',1) if isinstance(bid,str) else bid for bid in top_business_ids]
    # query reviews for those businesses and compute avg rating
    # chunk to avoid huge IN clause
    avg_parts=[]
    total_sum=0.0
    total_n=0
    import math
    chunk_size=500
    for i in range(0, len(top_business_refs), chunk_size):
        chunk = top_business_refs[i:i+chunk_size]
        # build SQL safely by quoting strings
        in_list = ','.join(["'"+c.replace("'","''")+"'" for c in chunk])
        q = f"SELECT AVG(rating) AS avg_rating, COUNT(*) AS n, SUM(rating) AS s FROM review WHERE business_ref IN ({in_list});"
        res = __import__('builtins')
        # use query_db tool not accessible here; so compute later outside python? 
    
# Can't call query_db from python environment; output intermediate info
out = {
    'top_state': top_state if not state_reviews.empty else None,
    'top_total_reviews_from_business_meta': top_total_reviews if not state_reviews.empty else None,
    'top_business_ref_count': len(top_business_refs) if not state_reviews.empty else 0,
    'top_business_refs_sample': top_business_refs[:5] if not state_reviews.empty else []
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zztlAUKkWO6PCSGpXAC4vrvf': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_t92ai8Wyd4Hsb3FnECZiHhlS': ['checkin', 'business'], 'var_call_KXWQobtv0E88xpJlinKAd6w2': ['review', 'tip', 'user'], 'var_call_ZkkA4ZnjI4eljPSM6zMgMWTR': 'file_storage/call_ZkkA4ZnjI4eljPSM6zMgMWTR.json'}

exec(code, env_args)
