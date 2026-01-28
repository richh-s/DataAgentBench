code = """import json, re, pandas as pd

path = var_call_gnpcyeq3NsDyPXRY5WHdS50d
with open(path, 'r') as f:
    biz = json.load(f)

rows=[]
state_re = re.compile(r',\s*([A-Z]{2})\b')
for b in biz:
    desc = b.get('description') or ''
    m = state_re.findall(desc)
    state = m[-1] if m else None
    rc = b.get('review_count')
    try:
        rc_int = int(rc)
    except Exception:
        rc_int = None
    rows.append({'business_id': b.get('business_id'), 'state': state, 'review_count': rc_int})

df = pd.DataFrame(rows)
df = df[df['state'].notna()]
if df.empty:
    res={'error':'Could not parse any state from business descriptions.'}
else:
    state_totals = df.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
    top_state = state_totals.iloc[0]['state']
    biz_ids = df[df['state']==top_state]['business_id'].dropna().unique().tolist()
    biz_refs = [bid.replace('businessid_','businessref_',1) for bid in biz_ids]
    res={'top_state': top_state, 'total_reviews': int(state_totals.iloc[0]['review_count']), 'business_refs': biz_refs}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Z7RSppvq4ywaE1GSzScoEdrn': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_8fkZW2OhzNc5RqanX2BaBkPy': ['checkin', 'business'], 'var_call_5wTjv0Z8jNXCpuZf4VhS5mS0': ['review', 'tip', 'user'], 'var_call_gnpcyeq3NsDyPXRY5WHdS50d': 'file_storage/call_gnpcyeq3NsDyPXRY5WHdS50d.json'}

exec(code, env_args)
