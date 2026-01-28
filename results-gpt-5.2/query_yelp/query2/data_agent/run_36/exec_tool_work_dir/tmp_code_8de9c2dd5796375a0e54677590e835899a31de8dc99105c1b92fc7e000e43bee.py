code = """import json, re, pandas as pd

path = var_call_69WtbuZomUc184pwfwh69wdE
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

df = pd.DataFrame(biz)
df['review_count'] = pd.to_numeric(df.get('review_count'), errors='coerce').fillna(0).astype(int)

extract_pat = re.compile(r"\b(?:in|at)\s+[^,\n]+,\s*([A-Z]{2})\b|\b([A-Z]{2})\b\s+location\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = extract_pat.search(desc)
    if m:
        return m.group(1) or m.group(2)
    m2 = re.findall(r",\s*([A-Z]{2})\b", desc)
    if m2:
        return m2[-1]
    return None

df['state'] = df['description'].apply(extract_state)
agg = df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
top_state = agg.iloc[0]['state'] if len(agg) else None

print('__RESULT__:')
print(json.dumps({'top_state': top_state}))"""

env_args = {'var_call_qjFTfWO6kIoUiw3doyE1Ms8R': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_lo5mA6k1fwtSZEXnWjbC6s4S': ['business', 'checkin'], 'var_call_JKf6J49QGnJXfStmw5GMdinE': ['review', 'tip', 'user'], 'var_call_2Kz8AtW45cHaZBC6TihXU0v8': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_69WtbuZomUc184pwfwh69wdE': 'file_storage/call_69WtbuZomUc184pwfwh69wdE.json'}

exec(code, env_args)
