code = """import json

results = locals()['var_function-call-1866357495502292692']
business_ids = results['business_ids_in_highest_state']
business_refs = [biz_id.replace('businessid_', 'businessref_') for biz_id in business_ids]

print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-8359971907749987780': 'file_storage/function-call-8359971907749987780.json', 'var_function-call-1866357495502292692': {'highest_wifi_state': 'PA', 'highest_wifi_count': 8, 'business_ids_in_highest_state': ['businessid_89', 'businessid_97', 'businessid_67', 'businessid_77', 'businessid_86', 'businessid_40', 'businessid_44', 'businessid_82']}}

exec(code, env_args)
