code = """import json, re
import pandas as pd

# Load data from storage variables
businesses = var_call_8OFKxgaVzHgJgMY9djEanppl
# var_call_lZmRttBv8Pzc064QJaUFRaa8 is a filepath to a JSON file with the reviews
with open(var_call_lZmRttBv8Pzc064QJaUFRaa8, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize types
if 'review_count' in df_b.columns:
    df_b['review_count'] = pd.to_numeric(df_b['review_count'], errors='coerce')

# Extract state from description using regex (two-letter state abbreviations)
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

df_b['state'] = df_b.get('description', '').apply(extract_state)

# Prepare reviews: convert rating to numeric and map business_ref -> business_id
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

if 'business_ref' in df_r.columns:
    df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_r['business_id'] = None

# Merge reviews with business states
df_merged = df_r.merge(df_b[['business_id', 'state']], on='business_id', how='left')

# Filter out rows without state or without rating
df_merged = df_merged[df_merged['state'].notna() & df_merged['rating'].notna()]

# Group by state to get counts and average rating
grp = df_merged.groupby('state').agg(review_count=('rating', 'count'), average_rating=('rating', 'mean')).reset_index()

if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    best = grp.loc[grp['review_count'].idxmax()]
    result = {
        "state": str(best['state']),
        "review_count": int(best['review_count']),
        "average_rating": round(float(best['average_rating']), 2)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dVDQKJmfHPp9d7FPGQP6jiAE': ['business', 'checkin'], 'var_call_plK4ltDd1O3Ctx1mY9p0kb6b': ['review', 'tip', 'user'], 'var_call_8OFKxgaVzHgJgMY9djEanppl': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_lZmRttBv8Pzc064QJaUFRaa8': 'file_storage/call_lZmRttBv8Pzc064QJaUFRaa8.json'}

exec(code, env_args)
