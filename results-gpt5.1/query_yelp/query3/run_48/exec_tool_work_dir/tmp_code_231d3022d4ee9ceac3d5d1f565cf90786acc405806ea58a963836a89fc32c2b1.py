code = """import json, pandas as pd

# Load review business_refs from 2018
review_businesses = pd.DataFrame(var_call_u6C6UaguqnY07ch57ew6wSez)
review_businesses['business_id'] = review_businesses['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Load full business attributes from file if needed
path = var_call_kBYgD4RAH1ADmMVbJsBXODae
with open(path, 'r') as f:
    business_records = json.load(f)

business_df = pd.DataFrame(business_records)[['business_id', 'attributes']]

# Normalize attributes: keep only where attributes is dict and has BikeParking or BusinessParking
mask_has_attrs = business_df['attributes'].apply(lambda x: isinstance(x, dict) and ('BikeParking' in x or 'BusinessParking' in x))
filtered_business = business_df[mask_has_attrs].copy()

# Any value (even 'False' or empty parking dict) counts as "offered either business parking or bike parking"? 
# Here we interpret presence of attribute key as offering that option.

# Join 2018-reviewed businesses with filtered_business on business_id
merged = review_businesses.merge(filtered_business, on='business_id', how='inner')

# Count distinct businesses
count_businesses = merged['business_id'].nunique()

result = json.dumps(int(count_businesses))

print("__RESULT__:")
print(result)"""

env_args = {'var_call_u6C6UaguqnY07ch57ew6wSez': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_99'}], 'var_call_kBnhp4RprsNnJV9f3qTMiDUh': ['checkin', 'business'], 'var_call_kBYgD4RAH1ADmMVbJsBXODae': 'file_storage/call_kBYgD4RAH1ADmMVbJsBXODae.json'}

exec(code, env_args)
