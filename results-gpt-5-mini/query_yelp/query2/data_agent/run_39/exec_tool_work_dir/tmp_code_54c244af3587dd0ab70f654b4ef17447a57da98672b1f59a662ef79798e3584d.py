code = """import json
import pandas as pd
import re

# Load variables from storage
business_docs = var_call_tdZu5anAVoAtrAnQRO1jP5mI
reviews_path_or_list = var_call_wgcxYCeG1A37yqhpF8Cletdg

# Load reviews: if reviews_path_or_list is a string, treat as file path
if isinstance(reviews_path_or_list, str):
    with open(reviews_path_or_list, 'r') as f:
        reviews = json.load(f)
else:
    reviews = reviews_path_or_list

# Create DataFrames
df_business = pd.DataFrame(business_docs)
df_reviews = pd.DataFrame(reviews)

# Ensure rating numeric
if 'rating' in df_reviews.columns:
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract state from business description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for pattern like ', XX,' or ', XX ' where XX are uppercase letters
    m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if m:
        return m.group(1)
    # Try other pattern: ' in City, ST,' or 'City, ST'
    m2 = re.search(r',\s*([A-Z]{2})$', desc.strip())
    if m2:
        return m2.group(1)
    return None

if 'description' in df_business.columns:
    df_business['state'] = df_business['description'].apply(extract_state)
else:
    df_business['state'] = None

# Map business_ref to business_id by replacing prefix
if 'business_ref' in df_reviews.columns:
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_reviews['business_id'] = None

# Merge reviews with business states
df_merged = df_reviews.merge(df_business[['business_id','state']], on='business_id', how='left')

# Filter to rows with a state
df_merged = df_merged[df_merged['state'].notna()]

# Group by state to get review counts and average rating
grouped = df_merged.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

# If no grouped results, return None
if grouped.empty:
    result = None
else:
    # Find state with max review_count
    max_row = grouped.sort_values(['review_count','state'], ascending=[False,True]).iloc[0]
    result = {
        'state': str(max_row['state']),
        'review_count': int(max_row['review_count']),
        'average_rating': float(round(max_row['average_rating'], 2))
    }

# Print per required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tdZu5anAVoAtrAnQRO1jP5mI': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_wgcxYCeG1A37yqhpF8Cletdg': 'file_storage/call_wgcxYCeG1A37yqhpF8Cletdg.json'}

exec(code, env_args)
