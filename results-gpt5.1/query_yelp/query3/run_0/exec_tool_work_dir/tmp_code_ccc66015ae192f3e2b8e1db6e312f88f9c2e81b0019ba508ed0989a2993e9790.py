code = """import json, pandas as pd

df_review = pd.DataFrame(var_call_d0pWIpaOdDHLM4yUZ6cBuu8c)

path = var_call_PFL3nlPugXouzVxZG5SLmnsW
with open(path, 'r') as f:
    business_attr = json.load(f)

df_bus = pd.DataFrame(business_attr)

df_bus['has_parking_or_bike'] = df_bus['attributes'].apply(lambda a: bool(a) and (('BusinessParking' in a and a['BusinessParking'] not in [None, "None"]) or ('BikeParking' in a and a['BikeParking'] == 'True')))

# map prefixes
review_bids = df_review['business_ref'].str.replace('businessref_', 'businessid_', regex=False).unique()

result_count = df_bus[df_bus['has_parking_or_bike'] & df_bus['business_id'].isin(review_bids)]['business_id'].nunique()

import json as _json
out = _json.dumps(int(result_count))
print("__RESULT__:")
print(out)"""

env_args = {'var_call_d0pWIpaOdDHLM4yUZ6cBuu8c': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}], 'var_call_PFL3nlPugXouzVxZG5SLmnsW': 'file_storage/call_PFL3nlPugXouzVxZG5SLmnsW.json'}

exec(code, env_args)
