code = """import json,re
import pandas as pd
# Load reviews data (could be a filepath or a list)
if isinstance(var_call_CIQFcCTooCbifDW8foGpuULA, str):
    with open(var_call_CIQFcCTooCbifDW8foGpuULA, 'r') as f:
        reviews = json.load(f)
else:
    reviews = var_call_CIQFcCTooCbifDW8foGpuULA

businesses = var_call_tbZn5Q2YngUNfESVBjbdUoB5

# Create DataFrames
df_reviews = pd.DataFrame(reviews)
# Ensure rating numeric
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')
else:
    df_reviews['rating'] = None

# Map business_ref to business_id
if 'business_ref' in df_reviews.columns:
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_reviews['business_id'] = None

df_business = pd.DataFrame(businesses)

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'in [^,]+, ([A-Z]{2})', desc)
    if m:
        return m.group(1)
    m2 = re.search(r', ([A-Z]{2}),', desc)
    if m2:
        return m2.group(1)
    return None

if 'description' in df_business.columns:
    df_business['state'] = df_business['description'].apply(extract_state)
else:
    df_business['state'] = None

# Merge reviews with business states
df = df_reviews.merge(df_business[['business_id', 'state']], on='business_id', how='left')
# Keep only reviews with a detected state
df = df[df['state'].notna()]

# Group by state
if not df.empty:
    grp = df.groupby('state').agg(review_count=('rating', 'size'), average_rating=('rating', 'mean')).reset_index()
    grp = grp.sort_values(['review_count', 'average_rating'], ascending=[False, False])
    top = grp.iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": float(round(top['average_rating'], 4))}
else:
    result = {"state": None, "review_count": 0, "average_rating": None}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vR8C2ks1FphRJR3Hcl9Ry0QX': ['business', 'checkin'], 'var_call_JBEBaywXQLU71zpCPbrgV0xS': ['review', 'tip', 'user'], 'var_call_tbZn5Q2YngUNfESVBjbdUoB5': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_CIQFcCTooCbifDW8foGpuULA': 'file_storage/call_CIQFcCTooCbifDW8foGpuULA.json'}

exec(code, env_args)
