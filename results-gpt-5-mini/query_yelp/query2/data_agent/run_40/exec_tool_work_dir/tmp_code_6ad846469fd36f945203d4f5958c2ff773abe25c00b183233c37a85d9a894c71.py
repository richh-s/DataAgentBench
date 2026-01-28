code = """import json
import pandas as pd
import re

# Load business documents from storage
businesses = var_call_VPdHaYNuQoA8E8X3o5ZRaoGm

# Build business dataframe
df_b = pd.DataFrame(businesses)
# Create business_ref to match review.business_ref
if 'business_id' in df_b.columns:
    df_b['business_ref'] = df_b['business_id'].str.replace('businessid_', 'businessref_')
else:
    df_b['business_ref'] = None

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2}),', desc)
    if m:
        return m.group(1)
    m2 = re.search(r',\s*([A-Z]{2})\b', desc)
    if m2:
        return m2.group(1)
    return None

if 'description' in df_b.columns:
    df_b['state'] = df_b['description'].apply(extract_state)
else:
    df_b['state'] = None

# Load reviews (result stored in a JSON file path)
reviews_file = var_call_ObFQV1meyVCW9G1Yhq12GqCV
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

df_r = pd.DataFrame(reviews)
# Convert rating to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with businesses on business_ref
if 'business_ref' not in df_r.columns:
    df_r['business_ref'] = None

df_merged = df_r.merge(df_b[['business_ref', 'state']], on='business_ref', how='inner')
# Filter out missing values
df_merged = df_merged[df_merged['state'].notna() & df_merged['rating'].notna()]

# Group by state
if df_merged.empty:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    grp = df_merged.groupby('state').agg(total_reviews=('rating', 'count'), average_rating=('rating', 'mean')).reset_index()
    maxrow = grp.loc[grp['total_reviews'].idxmax()]
    result = {"state": str(maxrow['state']), "total_reviews": int(maxrow['total_reviews']), "average_rating": round(float(maxrow['average_rating']), 2)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Xi2U3h3T7JpQjXKIn4Mruidu': ['business', 'checkin'], 'var_call_yf85dpCe9KxAGT7jgApchMmg': ['review', 'tip', 'user'], 'var_call_VPdHaYNuQoA8E8X3o5ZRaoGm': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_ObFQV1meyVCW9G1Yhq12GqCV': 'file_storage/call_ObFQV1meyVCW9G1Yhq12GqCV.json'}

exec(code, env_args)
