code = """import json, re, pandas as pd

# load business records
path = var_call_dtW7NITWm1gHbpR4tjr0Pp9j
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    return m.group(1) if m else None

rows=[]
for r in biz:
    state = r.get('state') or extract_state(r.get('description',''))
    rc = r.get('review_count')
    try:
        rc = int(rc)
    except Exception:
        rc = None
    rows.append({'business_id': r.get('business_id'), 'state': state, 'review_count': rc})

df = pd.DataFrame(rows)
state_reviews = df.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()
state_reviews = state_reviews.sort_values('review_count', ascending=False)
if state_reviews.empty:
    out = {'error':'No state/review_count data available in business collection'}
else:
    top_state = state_reviews.iloc[0]['state']
    total_reviews = int(state_reviews.iloc[0]['review_count'])
    out = {'top_state': top_state, 'total_reviews': total_reviews}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zViZpGsdRdg1VNbLPtLyzkCi': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_614YImrtp8Irq4IOg2sNt1AN': ['checkin', 'business'], 'var_call_6bdIU9mIjIFtAuFPHu6kIbXh': ['review', 'tip', 'user'], 'var_call_dtW7NITWm1gHbpR4tjr0Pp9j': 'file_storage/call_dtW7NITWm1gHbpR4tjr0Pp9j.json'}

exec(code, env_args)
