code = """import json, re, pandas as pd
from pathlib import Path

# load businesses
biz_path = Path(var_call_HyyvRxS3PLqxHpN0DQ9tGJtw)
biz = json.loads(biz_path.read_text())
dfb = pd.DataFrame(biz)
dfb['review_count'] = pd.to_numeric(dfb.get('review_count'), errors='coerce').fillna(0).astype(int)
pat = re.compile(r",\s*([A-Z]{2})(?:,|\b)")
dfb['state'] = dfb['description'].apply(lambda x: pat.search(x).group(1) if isinstance(x,str) and pat.search(x) else None)
dfb['business_ref'] = dfb['business_id'].astype(str).str.replace('businessid_','businessref_', regex=False)

# top state by business review_count
state_reviews = dfb.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
top_state = state_reviews.iloc[0]['state'] if len(state_reviews) else None

# get reviews from duckdb for businesses in top_state
if top_state is None:
    out = {"state": None, "review_count_total": 0, "avg_rating": None}
else:
    biz_refs = dfb.loc[dfb['state']==top_state,'business_ref'].dropna().unique().tolist()
    # chunk IN queries
    import duckdb
    con = duckdb.connect(database=':memory:')
    # attach existing user_database? Not available here. We'll query via provided storage var_call_4sSC9KgC6JHii0hyJlyKW58q only has ok.
    # So instead use query_db tool results not accessible directly in python.
    
print('__RESULT__:')
print(json.dumps({"top_state": top_state, "n_biz_in_state": 0}))"""

env_args = {'var_call_HyyvRxS3PLqxHpN0DQ9tGJtw': 'file_storage/call_HyyvRxS3PLqxHpN0DQ9tGJtw.json', 'var_call_4sSC9KgC6JHii0hyJlyKW58q': [{'ok': '1'}], 'var_call_siGcoF8XDYUvMdlKCLFQaW5T': {'state': None, 'total_reviews': 0, 'avg_rating_businesses_in_state': None}, 'var_call_YQsf7RVpZytqAs6NzBRLtjXk': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_0p6rbUOrkNZ35EQQZWDRGw43': {'n_sample': 100, 'n_matches': 0, 'unique_states': []}, 'var_call_eWa02WjsUnvnqnImt8HvGnpz': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'], 'var_call_Bca8ZIBREUDVexb83AZwB7OY': {'match': None}, 'var_call_rdRifK2QJqGQjxJskNb1tHli': {'match': 'CA'}, 'var_call_QssEbll6piXkU8O4RTpmvVGd': {'state': 'MO', 'total_reviews': 2243}}

exec(code, env_args)
