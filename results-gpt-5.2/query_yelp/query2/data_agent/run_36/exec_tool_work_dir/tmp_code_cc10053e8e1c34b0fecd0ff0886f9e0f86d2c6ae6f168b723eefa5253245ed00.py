code = """import json, re, pandas as pd

# Load business records from file path in var_call_69WtbuZomUc184pwfwh69wdE
path = var_call_69WtbuZomUc184pwfwh69wdE
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

df = pd.DataFrame(biz)
# review_count seems stored as string; coerce
if 'review_count' in df.columns:
    df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce').fillna(0).astype(int)

# Extract state from description, pattern ', XX' where XX is 2-letter uppercase
state_pat = re.compile(r'\b([A-Z]{2})\b')

# Prefer pattern ' in City, ST' or ' City, ST,'
extract_pat = re.compile(r'\b(?:in|at)\s+[^,\n]+,\s*([A-Z]{2})\b|\b([A-Z]{2})\b\s+location\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = extract_pat.search(desc)
    if m:
        return m.group(1) or m.group(2)
    # fallback: last occurrence of , ST
    m2 = re.findall(r',\s*([A-Z]{2})\b', desc)
    if m2:
        return m2[-1]
    return None

df['state'] = df['description'].apply(extract_state)

# Aggregate total reviews by state
agg = df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()
agg = agg.sort_values('review_count', ascending=False)

top_state = None
if len(agg) > 0:
    top_state = agg.iloc[0]['state']

out = {'top_state': top_state}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qjFTfWO6kIoUiw3doyE1Ms8R': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_lo5mA6k1fwtSZEXnWjbC6s4S': ['business', 'checkin'], 'var_call_JKf6J49QGnJXfStmw5GMdinE': ['review', 'tip', 'user'], 'var_call_2Kz8AtW45cHaZBC6TihXU0v8': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_69WtbuZomUc184pwfwh69wdE': 'file_storage/call_69WtbuZomUc184pwfwh69wdE.json'}

exec(code, env_args)
