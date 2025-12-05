code = """import json, pandas as pd
# load review business_refs
review_businesses = [r['business_ref'] for r in var_call_Stb8GRBaYfnAJFqlfs9uW80K]
# map to business_ids
biz_ids = set(['businessid_' + ref.split('_')[1] for ref in review_businesses])
# load full business file
with open(var_call_xPAWg3whWJr0ReCJwZnuulhs, 'r') as f:
    business_data = json.load(f)

count = 0
for rec in business_data:
    bid = rec.get('business_id')
    if bid not in biz_ids:
        continue
    attrs = rec.get('attributes')
    if not isinstance(attrs, dict):
        continue
    has_bike = attrs.get('BikeParking') == 'True'
    has_business = 'BusinessParking' in attrs and attrs.get('BusinessParking') not in [None, 'None']
    if has_bike or has_business:
        count += 1

result = json.dumps(count)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_DHrADQqdyTe1qjGu8bVff04L': ['business', 'checkin'], 'var_call_Stb8GRBaYfnAJFqlfs9uW80K': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_80'}], 'var_call_xPAWg3whWJr0ReCJwZnuulhs': 'file_storage/call_xPAWg3whWJr0ReCJwZnuulhs.json'}

exec(code, env_args)
