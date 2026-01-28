code = """import json, re, pandas as pd

path = var_call_cCxLkmyacMeLYz7tlUssAvV7
with open(path, 'r') as f:
    biz = json.load(f)

def get_state(desc):
    if not desc:
        return None
    m = re.search(r'\b([A-Z]{2})\b', desc)
    # prefer last two-letter token likely state; take last match
    if not m:
        return None
    matches = re.findall(r'\b([A-Z]{2})\b', desc)
    return matches[-1] if matches else None

rows=[]
for b in biz:
    state = b.get('state') or get_state(b.get('description',''))
    try:
        rc = int(b.get('review_count'))
    except Exception:
        rc = None
    rows.append({'business_id': b.get('business_id'), 'state': state, 'review_count': rc})

dfb = pd.DataFrame(rows)
state_tot = dfb.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

if len(state_tot)==0:
    out={'error':'No state info parsed from business descriptions'}
else:
    top_state = state_tot.iloc[0]['state']
    total_reviews = int(state_tot.iloc[0]['review_count'])
    biz_ids = dfb[dfb['state']==top_state]['business_id'].dropna().unique().tolist()
    biz_refs = ['businessref_' + bid.split('businessid_')[-1] for bid in biz_ids]
    out={'top_state': top_state, 'total_reviews': total_reviews, 'n_biz_in_state': len(biz_refs), 'biz_refs_sample': biz_refs[:10]}

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DFZZpQb6uNwFwRETX2TfLl11': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_xoBymZrxo6zcEEfDlgffaokf': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_jSnYeC5zDu1C0Y7LlaQ8rLTy': [{'n': '2000', 'min_ref': 'businessref_1', 'max_ref': 'businessref_99'}], 'var_call_otvXAWZZfHnOGXPP2ndqaMIB': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}], 'var_call_cCxLkmyacMeLYz7tlUssAvV7': 'file_storage/call_cCxLkmyacMeLYz7tlUssAvV7.json'}

exec(code, env_args)
