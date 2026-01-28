code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_RJHJSC2vtW7VyNd5xkEZJROH)
rev = load_records(var_call_Jh3kM2uGdpflwup5BdQlA7Dg)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

state_re = re.compile(r",\s*([A-Z]{2})(?=,)" )

def extract_state(desc):
    if desc is None:
        return None
    m = state_re.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].map(extract_state)
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce')
state_reviews = biz_df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

top = state_reviews.sort_values('review_count', ascending=False).head(1)
if top.empty:
    out = {"state": None, "total_reviews": None, "avg_rating": None}
else:
    top_state = top.iloc[0]['state']
    total_reviews = int(top.iloc[0]['review_count']) if pd.notna(top.iloc[0]['review_count']) else None
    top_biz_refs = set(biz_df.loc[biz_df['state'] == top_state, 'business_ref'].dropna().tolist())
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    avg_rating = rev_df.loc[rev_df['business_ref'].isin(top_biz_refs), 'rating'].mean()
    avg_rating = float(avg_rating) if pd.notna(avg_rating) else None
    out = {"state": top_state, "total_reviews": total_reviews, "avg_rating": avg_rating}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RJHJSC2vtW7VyNd5xkEZJROH': 'file_storage/call_RJHJSC2vtW7VyNd5xkEZJROH.json', 'var_call_Jh3kM2uGdpflwup5BdQlA7Dg': 'file_storage/call_Jh3kM2uGdpflwup5BdQlA7Dg.json', 'var_call_dUQvZY5jHbvdSsBx49DclnPe': {'state': None, 'total_reviews': None, 'avg_rating': None}, 'var_call_ainp1R3yViiB3XtH8A0rvKrj': {'sample_desc': ['Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'], 'extracted_tokens': [[], [], [], [], []]}, 'var_call_fW1WMwS0kh4z7WJYPAUiSrd8': {'extracted': [['CA'], ['MO'], ['ID'], ['FL'], ['IN']]}}

exec(code, env_args)
