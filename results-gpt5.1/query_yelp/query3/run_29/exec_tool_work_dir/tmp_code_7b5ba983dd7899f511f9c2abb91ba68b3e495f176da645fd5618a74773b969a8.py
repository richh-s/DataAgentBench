code = """import json, pandas as pd, os

reviews = var_call_GbcSdNtxzni8z3iXqiCrucMu
rev_df = pd.DataFrame(reviews)
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

path = var_call_jIA4HcPqaFaZQQSVkKePU1NK
with open(path, 'r') as f:
    biz = json.load(f)

biz_df = pd.DataFrame(biz)[['business_id', 'attributes']]

# normalize attributes: treat non-dict as empty
biz_df['attrs'] = biz_df['attributes'].apply(lambda x: x if isinstance(x, dict) else {})

biz_df['has_parking_or_bike'] = biz_df['attrs'].apply(lambda d: ('BusinessParking' in d and d['BusinessParking'] not in (None, 'None')) or ('BikeParking' in d and d['BikeParking'] == 'True'))

merged = pd.merge(rev_df[['business_id']].drop_duplicates(), biz_df[['business_id', 'has_parking_or_bike']], on='business_id', how='left')

count = int(merged[merged['has_parking_or_bike'] == True]['business_id'].nunique())

import json as _json
res = _json.dumps(count)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_HPgmzNHgFXWW9BVsT2K3JuAy': ['checkin', 'business'], 'var_call_GbcSdNtxzni8z3iXqiCrucMu': [{'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_jIA4HcPqaFaZQQSVkKePU1NK': 'file_storage/call_jIA4HcPqaFaZQQSVkKePU1NK.json'}

exec(code, env_args)
