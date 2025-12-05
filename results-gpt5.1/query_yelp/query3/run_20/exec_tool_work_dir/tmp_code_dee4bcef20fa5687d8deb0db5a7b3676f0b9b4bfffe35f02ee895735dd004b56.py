code = """import json, pandas as pd
review_businesses = pd.DataFrame(var_call_YzwrpcEhY5rQvM0w9gnaXezr)
review_businesses['business_id'] = review_businesses['business_ref'].str.replace('businessref_','businessid_', regex=False)
with open(var_call_iKNruq2FuJpUpwALHXPThzV2, 'r') as f:
    business_attrs = pd.DataFrame(json.load(f))
# normalize attributes presence
business_attrs['has_parking_or_bike'] = business_attrs['attributes'].apply(lambda a: isinstance(a, dict) and (('BusinessParking' in a and a['BusinessParking'] not in [None, 'None']) or ('BikeParking' in a and str(a['BikeParking']) != 'False')))
merged = pd.merge(review_businesses[['business_id']].drop_duplicates(), business_attrs[['business_id','has_parking_or_bike']], on='business_id', how='left')
count = int(merged[merged['has_parking_or_bike'] == True]['business_id'].nunique())
import json as _json
result = _json.dumps(count)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_tOO6APvEUvZ7x6DNWDHbRNiq': ['business', 'checkin'], 'var_call_YzwrpcEhY5rQvM0w9gnaXezr': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_iKNruq2FuJpUpwALHXPThzV2': 'file_storage/call_iKNruq2FuJpUpwALHXPThzV2.json'}

exec(code, env_args)
