code = """import json

biz = var_call_F3WbZPTr9vIpukyAvfWEUZHg
biz_ids = [r['business_id'] for r in biz if 'business_id' in r]
# convert businessid_X -> businessref_X
biz_refs = ['businessref_' + b.split('businessid_',1)[1] if b.startswith('businessid_') else b for b in biz_ids]

result = {
    'business_count': len(biz_refs),
    'biz_refs': biz_refs
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_F3WbZPTr9vIpukyAvfWEUZHg': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
