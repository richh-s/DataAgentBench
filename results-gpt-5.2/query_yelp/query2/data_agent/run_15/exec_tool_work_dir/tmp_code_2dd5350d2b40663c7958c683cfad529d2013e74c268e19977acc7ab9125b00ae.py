code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_AYyXv9LsIzsqcL0IvI0qZ9In)
rev = load_records(var_call_mvUTq4R7LE2uFfV6ZMMwzuo4)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

pat2 = re.compile(r",\s*([A-Z]{2}),")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat2.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].map(extract_state)
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce')

state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]

top_state_biz = biz_df.loc[biz_df['state'] == top_state, ['business_id']].copy()
top_state_biz['business_ref'] = top_state_biz['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
merged = rev_df.merge(top_state_biz[['business_ref']], on='business_ref', how='inner')

avg_rating = float(merged['rating'].mean()) if len(merged) else None

out = {
    'state': top_state,
    'total_reviews': int(state_reviews.loc[top_state]) if pd.notna(state_reviews.loc[top_state]) else None,
    'average_rating': round(avg_rating, 4) if avg_rating is not None else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AYyXv9LsIzsqcL0IvI0qZ9In': 'file_storage/call_AYyXv9LsIzsqcL0IvI0qZ9In.json', 'var_call_mvUTq4R7LE2uFfV6ZMMwzuo4': 'file_storage/call_mvUTq4R7LE2uFfV6ZMMwzuo4.json', 'var_call_vqnJ8cdBH0SxFKkRydbtobWI': {'state_value_counts_head': {'null': 100}}, 'var_call_JGYIMPjpPCyb6MTtqqBVVpgu': {'num_examples_found': 49, 'examples': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'state': 'CA'}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'state': 'MO'}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'state': 'ID'}, {'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'state': 'FL'}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'state': 'IN'}]}}

exec(code, env_args)
