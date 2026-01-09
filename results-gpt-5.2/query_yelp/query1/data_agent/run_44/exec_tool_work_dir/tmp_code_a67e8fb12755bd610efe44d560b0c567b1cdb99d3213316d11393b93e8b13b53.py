code = """import json
biz_ids = [r['business_id'] for r in var_call_YlfIdX1A5Gw3V0VS0Rbd9VYG]
# map businessid_x -> businessref_x
biz_refs = ['businessref_' + bid.split('businessid_')[1] for bid in biz_ids if 'businessid_' in bid]
print('__RESULT__:')
print(json.dumps({'biz_refs': biz_refs}))"""

env_args = {'var_call_YlfIdX1A5Gw3V0VS0Rbd9VYG': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
