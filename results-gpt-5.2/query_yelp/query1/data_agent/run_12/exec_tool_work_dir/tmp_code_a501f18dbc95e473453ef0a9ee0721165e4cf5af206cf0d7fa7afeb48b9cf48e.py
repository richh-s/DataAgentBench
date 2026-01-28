code = """import json
# business ids from mongo query
biz_ids = [r['business_id'] for r in var_call_6ExAvuDyYMSqQQyMEV8W6Sov]
# convert businessid_ -> businessref_
biz_refs = [bid.replace('businessid_','businessref_',1) for bid in biz_ids]
result = json.dumps({'biz_refs': biz_refs, 'count': len(biz_refs)})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Q76HMijXMPX5tRQ0XZmfp8V6': [], 'var_call_6ExAvuDyYMSqQQyMEV8W6Sov': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
