code = """import json
import re
import pandas as pd

# Load previous results
# Review counts
review_counts_raw = locals()['var_function-call-3161015109475125821']
# Business info
business_info_raw = locals()['var_function-call-14798061160419285580']
if isinstance(business_info_raw, str):
    with open(business_info_raw, 'r') as f:
        business_info = json.load(f)
else:
    business_info = business_info_raw

# Create DataFrame for review counts
df_reviews = pd.DataFrame(review_counts_raw)
# Convert review_count to int
df_reviews['review_count'] = df_reviews['review_count'].astype(int)
# Normalize business_ref to business_id: 'businessref_X' -> 'businessid_X'
df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_')

# Create DataFrame for businesses
df_business = pd.DataFrame(business_info)
# Keep only id and description
df_business = df_business[['business_id', 'description']]

# Merge
merged = pd.merge(df_reviews, df_business, on='business_id', how='left')

# Function to extract categories
def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    # Regex to find the list of categories
    # Patterns observed: "services in ...", "including ...", "destination for ..."
    # We look for the part after these phrases
    match = re.search(r'(?:services in|including|destination for)\s+(.*?)(\.|$)', desc)
    if match:
        cat_str = match.group(1)
        # Split by comma and 'and'
        # Replace ' and ' with ',' first to handle "A, B, and C" -> "A, B, C"
        cat_str = cat_str.replace(' and ', ', ')
        parts = [c.strip() for c in cat_str.split(',')]
        return [p for p in parts if p]
    return []

# Explode categories
category_counts = {}

for _, row in merged.iterrows():
    cats = extract_categories(row['description'])
    count = row['review_count']
    for cat in cats:
        category_counts[cat] = category_counts.get(cat, 0) + count

# Sort and get top 5
sorted_cats = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_cats[:5]

print("__RESULT__:")
print(json.dumps([cat for cat, count in top_5]))"""

env_args = {'var_function-call-16920037178816059437': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3161015109475125821': [{'business_ref': 'businessref_79', 'review_count': '5'}, {'business_ref': 'businessref_13', 'review_count': '3'}, {'business_ref': 'businessref_44', 'review_count': '3'}, {'business_ref': 'businessref_9', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_25', 'review_count': '1'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_6', 'review_count': '4'}, {'business_ref': 'businessref_71', 'review_count': '1'}, {'business_ref': 'businessref_91', 'review_count': '1'}, {'business_ref': 'businessref_16', 'review_count': '1'}, {'business_ref': 'businessref_55', 'review_count': '1'}, {'business_ref': 'businessref_29', 'review_count': '1'}, {'business_ref': 'businessref_39', 'review_count': '1'}, {'business_ref': 'businessref_67', 'review_count': '3'}, {'business_ref': 'businessref_15', 'review_count': '3'}, {'business_ref': 'businessref_33', 'review_count': '3'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_51', 'review_count': '3'}, {'business_ref': 'businessref_37', 'review_count': '3'}, {'business_ref': 'businessref_57', 'review_count': '4'}, {'business_ref': 'businessref_8', 'review_count': '2'}, {'business_ref': 'businessref_62', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '2'}, {'business_ref': 'businessref_97', 'review_count': '1'}, {'business_ref': 'businessref_72', 'review_count': '1'}, {'business_ref': 'businessref_85', 'review_count': '1'}, {'business_ref': 'businessref_42', 'review_count': '1'}, {'business_ref': 'businessref_21', 'review_count': '4'}, {'business_ref': 'businessref_26', 'review_count': '2'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_4', 'review_count': '1'}, {'business_ref': 'businessref_88', 'review_count': '2'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '4'}, {'business_ref': 'businessref_82', 'review_count': '2'}, {'business_ref': 'businessref_40', 'review_count': '3'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_61', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '3'}, {'business_ref': 'businessref_3', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '4'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '4'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_76', 'review_count': '1'}], 'var_function-call-14798061160419285580': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}]}

exec(code, env_args)
