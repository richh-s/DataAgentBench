code = """import json, pandas as pd, os

# Load full business attributes result from file
path = var_call_S59Tze9jcES1CJnGxiQX8CjA
with open(path, 'r') as f:
    business_attr = json.load(f)

reviews_2018 = pd.DataFrame(var_call_UXIAkFBHFduGnpx7Ez5PH6HO)

# Map business_ref -> business_id by replacing prefix
reviews_2018['business_id'] = reviews_2018['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

biz_attr_df = pd.DataFrame(business_attr)

# Keep only businesses with either BusinessParking present (not "None") or BikeParking == "True"

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    bike = attrs.get('BikeParking') == 'True'
    bp = attrs.get('BusinessParking')
    has_bp = isinstance(bp, str) and bp != 'None'
    return bike or has_bp

biz_attr_df['has_parking'] = biz_attr_df['attributes'].apply(has_parking)

biz_with_parking = biz_attr_df[biz_attr_df['has_parking']][['business_id']].drop_duplicates()

# Join with 2018-reviewed businesses
merged = pd.merge(reviews_2018[['business_id']].drop_duplicates(), biz_with_parking, on='business_id', how='inner')

count = int(merged['business_id'].nunique())

import json as _json
result = _json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_S59Tze9jcES1CJnGxiQX8CjA': 'file_storage/call_S59Tze9jcES1CJnGxiQX8CjA.json', 'var_call_K1m99l8W8b1LgY6IyRr7rhEg': [{'business_id': 'businessid_41', 'attributes': 'None'}, {'business_id': 'businessid_1', 'attributes': 'None'}, {'business_id': 'businessid_70', 'attributes': 'None'}, {'business_id': 'businessid_42', 'attributes': 'None'}, {'business_id': 'businessid_28', 'attributes': 'None'}, {'business_id': 'businessid_78', 'attributes': 'None'}, {'business_id': 'businessid_79', 'attributes': 'None'}, {'business_id': 'businessid_72', 'attributes': 'None'}, {'business_id': 'businessid_23', 'attributes': 'None'}], 'var_call_1w7bpoztnoobU2nckDdYd5Z5': [{'1': '1'}], 'var_call_UXIAkFBHFduGnpx7Ez5PH6HO': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}]}

exec(code, env_args)
