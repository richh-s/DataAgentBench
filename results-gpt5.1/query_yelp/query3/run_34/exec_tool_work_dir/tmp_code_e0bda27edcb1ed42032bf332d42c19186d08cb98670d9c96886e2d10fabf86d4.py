code = """import json, pandas as pd
business_reviews = pd.DataFrame(var_call_xnq1cRVfZglfwP2Nqp8xtAnf)
# Map business_ref to business_id
business_reviews['business_id'] = business_reviews['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Load full business attributes file if needed
path = var_call_JKYnlCcTcexVtV1BvfZeagjd
with open(path, 'r') as f:
    business_attr = json.load(f)

business_attr_df = pd.DataFrame(business_attr)[['business_id', 'attributes']]

# Filter for businesses with either BusinessParking not null/"None" or BikeParking == "True"

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    bp = attrs.get('BusinessParking')
    bike = attrs.get('BikeParking')
    cond_bp = bp is not None and bp != "None"
    cond_bike = str(bike) == 'True'
    return cond_bp or cond_bike

business_attr_df['has_parking'] = business_attr_df['attributes'].apply(has_parking)
parking_businesses = business_attr_df[business_attr_df['has_parking']][['business_id']]

# Inner join with businesses that had reviews in 2018
merged = pd.merge(business_reviews, parking_businesses, on='business_id', how='inner')
count = int(merged['business_id'].nunique())

res = json.dumps(count)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_JKYnlCcTcexVtV1BvfZeagjd': 'file_storage/call_JKYnlCcTcexVtV1BvfZeagjd.json', 'var_call_xnq1cRVfZglfwP2Nqp8xtAnf': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}]}

exec(code, env_args)
