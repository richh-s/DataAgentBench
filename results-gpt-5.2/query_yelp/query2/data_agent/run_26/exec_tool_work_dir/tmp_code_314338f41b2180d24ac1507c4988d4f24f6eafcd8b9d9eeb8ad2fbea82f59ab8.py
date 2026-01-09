code = """import json, re, pandas as pd

path = var_call_MTqPlnnUHXd5sHz3APVIcK7GE
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def extract_state(rec):
    # prefer explicit field if present
    st = rec.get('state')
    if st and isinstance(st, str) and len(st.strip())==2:
        return st.strip()
    desc = rec.get('description') or ''
    m = re.search(r'\b([A-Z]{2})\b', desc)
    # better: look for ', XX' patterns
    m2 = re.search(r',\s*([A-Z]{2})\b', desc)
    if m2:
        return m2.group(1)
    if m:
        return m.group(1)
    return None

rows=[]
for r in data:
    rc = r.get('review_count')
    try:
        rc = int(rc)
    except Exception:
        rc = None
    stars = r.get('stars')
    try:
        stars = float(stars) if stars is not None else None
    except Exception:
        stars = None
    st = extract_state(r)
    rows.append({'state': st, 'review_count': rc, 'stars': stars})

df = pd.DataFrame(rows)
df = df.dropna(subset=['state','review_count'])
state_sum = df.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
if len(state_sum)==0:
    out = {'error':'No state/review_count data found'}
else:
    top_state = state_sum.iloc[0]['state']
    top_reviews = int(state_sum.iloc[0]['review_count'])
    avg_stars = df.loc[df['state']==top_state, 'stars'].dropna().mean()
    out = {'state': top_state, 'total_reviews': top_reviews, 'avg_business_rating': (None if pd.isna(avg_stars) else float(avg_stars))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ncJn2ycTKgKxQDkYdSlIk5h2': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_epy1rqrfHZ05nl9GjN5mj5el': ['business', 'checkin'], 'var_call_R16cEHhvJrYqctY1J4qXyxdG': ['review', 'tip', 'user'], 'var_call_MTqPlnUHXd5sHz3APVIcK7GE': 'file_storage/call_MTqPlnUHXd5sHz3APVIcK7GE.json'}

exec(code, env_args)
