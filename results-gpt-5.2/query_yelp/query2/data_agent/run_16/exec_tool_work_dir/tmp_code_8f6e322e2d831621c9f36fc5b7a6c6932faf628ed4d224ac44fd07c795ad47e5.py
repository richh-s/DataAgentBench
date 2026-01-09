code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_records(var_call_NFEvdMmwAZrZR9o392X4YuFv)
dfb = pd.DataFrame(biz)

pat = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2}),")
st = dfb['description'].astype(str).str.extract(pat, expand=False)

out = {
  'dtype': str(st.dtype),
  'head': [None if pd.isna(x) else str(x) for x in st.head(20).tolist()],
  'non_null': int(st.notna().sum())
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NFEvdMmwAZrZR9o392X4YuFv': 'file_storage/call_NFEvdMmwAZrZR9o392X4YuFv.json', 'var_call_S7DU8KadOMgbH0YSvnrEUPHf': 'file_storage/call_S7DU8KadOMgbH0YSvnrEUPHf.json', 'var_call_HTO75oPyIwPVZTi0znAPIaAS': {'state': None, 'total_review_count': None, 'average_rating': None}, 'var_call_wQOFaHByNd8FnmkIxqJ2KWLZ': {'non_null_ex1': 0, 'non_null_ex2': 0, 'sample': [{'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'ex1': nan, 'ex2': nan}, {'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'ex1': nan, 'ex2': nan}]}}

exec(code, env_args)
