code = """import json

# Load businesses from file
businesses = json.load(open(var_call_wFNTlM4QAV9TUcC6xkswH3Wg, 'r'))

# Map business_id to attributes
biz_map = {b.get('business_id'): b.get('attributes') for b in businesses}

# Extract target ids
review_refs = var_call_5PF0SDjuAlSgAHKzbH0odTuj
target_ids = ['businessid_' + r['business_ref'].split('_', 1)[1] for r in review_refs if 'business_ref' in r]

count = 0
for bid in target_ids:
    attrs = biz_map.get(bid)
    if not attrs:
        continue
    s = str(attrs)
    has_bike = 'BikeParking' in s and 'True' in s
    has_business = 'BusinessParking' in s and 'True' in s
    if has_bike or has_business:
        count += 1

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_ahykiNY0zABwSHlCxeCTCLuE': ['checkin', 'business'], 'var_call_YaeHjrzfmwQaqjHlu4h3b9gG': ['review', 'tip', 'user'], 'var_call_5PF0SDjuAlSgAHKzbH0odTuj': [{'business_ref': 'businessref_13'}, {'business_ref': 'businessref_79'}, {'business_ref': 'businessref_66'}, {'business_ref': 'businessref_25'}, {'business_ref': 'businessref_59'}, {'business_ref': 'businessref_67'}, {'business_ref': 'businessref_15'}, {'business_ref': 'businessref_91'}, {'business_ref': 'businessref_46'}, {'business_ref': 'businessref_47'}, {'business_ref': 'businessref_73'}, {'business_ref': 'businessref_24'}, {'business_ref': 'businessref_36'}, {'business_ref': 'businessref_17'}, {'business_ref': 'businessref_43'}, {'business_ref': 'businessref_99'}, {'business_ref': 'businessref_80'}, {'business_ref': 'businessref_86'}, {'business_ref': 'businessref_62'}, {'business_ref': 'businessref_8'}, {'business_ref': 'businessref_57'}, {'business_ref': 'businessref_37'}, {'business_ref': 'businessref_40'}, {'business_ref': 'businessref_83'}, {'business_ref': 'businessref_82'}, {'business_ref': 'businessref_35'}, {'business_ref': 'businessref_45'}, {'business_ref': 'businessref_77'}, {'business_ref': 'businessref_27'}, {'business_ref': 'businessref_20'}, {'business_ref': 'businessref_22'}, {'business_ref': 'businessref_14'}, {'business_ref': 'businessref_28'}, {'business_ref': 'businessref_26'}, {'business_ref': 'businessref_4'}, {'business_ref': 'businessref_68'}], 'var_call_wFNTlM4QAV9TUcC6xkswH3Wg': 'file_storage/call_wFNTlM4QAV9TUcC6xkswH3Wg.json'}

exec(code, env_args)
