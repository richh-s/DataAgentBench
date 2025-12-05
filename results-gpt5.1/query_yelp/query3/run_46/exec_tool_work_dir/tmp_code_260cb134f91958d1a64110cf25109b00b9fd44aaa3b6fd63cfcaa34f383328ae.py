code = """import json, pandas as pd, os

# Load full business attributes result from JSON file
path = var_call_M1MMmoLivXc05539s8vGVKwt
with open(path, 'r') as f:
    business_attr = json.load(f)

# Load business refs with reviews in 2018
review_businesses = pd.DataFrame(var_call_FzhT7cdipUWCe3IqzYm3CCqv)

# Convert business_ref (businessref_x) to business_id (businessid_x)
review_businesses['business_id'] = review_businesses['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Filter businesses that offer BusinessParking or BikeParking
business_df = pd.DataFrame(business_attr)

# Normalize attributes to check for presence of keys and truthy values

def has_parking_or_bike(attrs):
    if not isinstance(attrs, dict):
        return False
    # BikeParking is simple True/False stored as string
    bike = attrs.get('BikeParking')
    if isinstance(bike, str) and bike == 'True':
        return True
    # BusinessParking is stored as a string representation of dict or "None"
    bp = attrs.get('BusinessParking')
    if isinstance(bp, str):
        if bp == 'None':
            return False
        # consider that any dict-like string implies some kind of parking option is described, count as offering parking
        if bp.strip().startswith('{') or bp.strip().startswith("{u'"):
            return True
    return False

business_df['offers_parking_or_bike'] = business_df['attributes'].apply(has_parking_or_bike)

eligible_businesses = business_df[business_df['offers_parking_or_bike']][['business_id']]

# Join with review businesses
merged = review_businesses.merge(eligible_businesses, on='business_id', how='inner')

count_businesses = int(merged['business_id'].nunique())

result = json.dumps(count_businesses)

print('__RESULT__:')
print(result)"""

env_args = {'var_call_M1MMmoLivXc05539s8vGVKwt': 'file_storage/call_M1MMmoLivXc05539s8vGVKwt.json', 'var_call_FzhT7cdipUWCe3IqzYm3CCqv': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_59'}]}

exec(code, env_args)
