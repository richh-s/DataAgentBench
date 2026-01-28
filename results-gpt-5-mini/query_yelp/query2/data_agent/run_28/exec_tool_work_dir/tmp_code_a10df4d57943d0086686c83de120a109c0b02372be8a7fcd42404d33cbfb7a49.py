code = """import pandas as pd
import json
import re

# Load business data from storage variable
business_list = var_call_5hvu6MQZtAfhx0nQwA2AMdhU

# Load reviews data from file path stored in var_call_4zqkVTUwDUgVt5SwQoVawlfz
reviews_path = var_call_4zqkVTUwDUgVt5SwQoVawlfz
with open(reviews_path, 'r') as f:
    reviews_list = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(business_list)
rdf = pd.DataFrame(reviews_list)

# Normalize business_id and extract state from description
# Ensure review_count numeric
if 'review_count' in bdf.columns:
    bdf['review_count'] = pd.to_numeric(bdf['review_count'], errors='coerce')

# Function to extract state code from description
state_pattern = re.compile(r"\b([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try to find patterns like 'in City, ST,' or ', ST,' near end
    # Look for ' in <city>, <ST>' first
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    # fallback: find last occurrence of comma + space + two upper letters
    m2 = re.findall(r',\s*([A-Z]{2})(?:[,\s]|$)', desc)
    if m2:
        return m2[-1]
    # fallback: any two-letter uppercase token
    m3 = state_pattern.search(desc)
    if m3:
        return m3.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Build mapping from businessref to state
# business.business_id like 'businessid_49' corresponds to review.business_ref 'businessref_49'
# We'll extract the numeric suffix to join
bdf['suffix'] = bdf['business_id'].astype(str).str.replace(r'^\D+', '', regex=True)
rdf['suffix'] = rdf['business_ref'].astype(str).str.replace(r'^\D+', '', regex=True)

# Merge reviews with business states
merged = rdf.merge(bdf[['suffix','state']], on='suffix', how='left')

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')

# Filter out rows without state
merged_valid = merged[merged['state'].notnull()].copy()

# Group by state: count reviews and average rating
grp = merged_valid.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

# Find state with max review_count
if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    top = grp.sort_values(['review_count','average_rating'], ascending=[False,False]).iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": float(round(top['average_rating'],3))}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5hvu6MQZtAfhx0nQwA2AMdhU': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_4zqkVTUwDUgVt5SwQoVawlfz': 'file_storage/call_4zqkVTUwDUgVt5SwQoVawlfz.json'}

exec(code, env_args)
