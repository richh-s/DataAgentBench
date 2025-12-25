code = """import json, pandas as pd, os

# Load full business attributes result from file
path = var_call_ruV71vgVo4OHuk7QiJkpzni6
if isinstance(path, str) and os.path.isfile(path):
    with open(path, 'r') as f:
        business_attr = json.load(f)
else:
    business_attr = var_call_ruV71vgVo4OHuk7QiJkpzni6

# DataFrames
reviews_2018 = pd.DataFrame(var_call_UT4scewRVP4sMap43tP8x2ua)

# Normalize business_ref to match business_id (businessref_ -> businessid_)
reviews_2018['business_id'] = reviews_2018['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

biz_attr_df = pd.DataFrame(business_attr)

# Filter businesses that have either BusinessParking or BikeParking in attributes and not None/'None'

def has_parking(attrs):
    if not isinstance(attrs, dict):
        return False
    # direct BikeParking flag
    if 'BikeParking' in attrs and attrs['BikeParking'] not in [None, 'None', 'False', False]:
        return True
    # any BusinessParking info that is not None or 'None'
    if 'BusinessParking' in attrs and attrs['BusinessParking'] not in [None, 'None']:
        return True
    return False

biz_attr_df['has_parking'] = biz_attr_df['attributes'].apply(has_parking)

biz_with_parking = biz_attr_df[biz_attr_df['has_parking']][['business_id']].drop_duplicates()

# Inner join to get businesses that (a) received reviews in 2018 and (b) have parking
merged = pd.merge(reviews_2018[['business_id']].drop_duplicates(), biz_with_parking, on='business_id', how='inner')

count = int(len(merged))

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ruV71vgVo4OHuk7QiJkpzni6': 'file_storage/call_ruV71vgVo4OHuk7QiJkpzni6.json', 'var_call_UT4scewRVP4sMap43tP8x2ua': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}]}

exec(code, env_args)
