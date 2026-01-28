code = """import json
import pandas as pd
import re

# Load previous tool results from storage variables
reviews = json.load(open(var_call_83VRfpeZUZe8CLe2uO0Riv8b, 'r'))
business = var_call_aSghSrXfXdz9AT2Wnv3JQfdt

# Create DataFrames
rev_df = pd.DataFrame(reviews)
bus_df = pd.DataFrame(business)

# Normalize types
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Convert business_ref (businessref_#) to business_id (businessid_#)
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Extract state from business description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try to find a two-letter state code after a comma
    m = re.search(r',\s*([A-Z]{2})(?:[,\s]|$)', desc)
    if m:
        return m.group(1)
    # Fallback: look for 'in City, ST' pattern
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    return None

bus_df['state'] = bus_df['description'].apply(extract_state)

# Merge reviews with business on business_id
merged = rev_df.merge(bus_df[['business_id', 'state']], on='business_id', how='left')

# Drop rows without state or without rating
merged = merged[merged['state'].notna() & merged['rating'].notna()].copy()

# Group by state: count reviews and average rating
grp = merged.groupby('state').agg(review_count=('rating', 'size'), average_rating=('rating', 'mean')).reset_index()

# If no data, return empty
if grp.empty:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    # Find state with max reviews
    max_row = grp.loc[grp['review_count'].idxmax()]
    result = {
        'state': str(max_row['state']),
        'review_count': int(max_row['review_count']),
        'average_rating': round(float(max_row['average_rating']), 2)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o0aBuLB23kfwRZyqDkNKCVFb': ['business', 'checkin'], 'var_call_qUm9z3LCp3VnZdiR1hH7qQKX': ['review', 'tip', 'user'], 'var_call_aSghSrXfXdz9AT2Wnv3JQfdt': [{'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_83VRfpeZUZe8CLe2uO0Riv8b': 'file_storage/call_83VRfpeZUZe8CLe2uO0Riv8b.json'}

exec(code, env_args)
