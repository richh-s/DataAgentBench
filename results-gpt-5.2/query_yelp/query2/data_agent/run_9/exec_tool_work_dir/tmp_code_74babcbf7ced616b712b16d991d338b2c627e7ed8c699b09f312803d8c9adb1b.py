code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_0FCafEWNzDCyxFVfMTQjn1fl)
dfb = pd.DataFrame(biz)

# improved state regex: two-letter code followed by comma or end
pat = re.compile(r',\s*([A-Z]{2})(?=,|\.|\s|$)')

def get_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb['description'].map(get_state)

out = {
    "n_state_nonnull": int(dfb['state'].notna().sum()),
    "sample_states": dfb['state'].dropna().unique()[:20].tolist(),
    "state_counts": dfb['state'].value_counts().head(10).to_dict()
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0FCafEWNzDCyxFVfMTQjn1fl': 'file_storage/call_0FCafEWNzDCyxFVfMTQjn1fl.json', 'var_call_d2B8rtRoEAk1d7rH7WdBrch3': 'file_storage/call_d2B8rtRoEAk1d7rH7WdBrch3.json', 'var_call_ILw30yE0blAuVTLXSApnwEqn': {'error': 'No state/review_count data parsed'}, 'var_call_MzpxbkPSXKoeEN2LtPHl09Vd': {'n_rows': 100, 'n_state_nonnull': 0, 'sample_states': [], 'review_count_null': 0, 'review_count_min': 5.0, 'review_count_max': 1742.0, 'sample_desc': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.']}}

exec(code, env_args)
