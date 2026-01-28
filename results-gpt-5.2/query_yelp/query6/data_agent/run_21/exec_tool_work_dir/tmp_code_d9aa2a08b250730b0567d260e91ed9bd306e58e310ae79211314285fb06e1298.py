code = """import json
s = "ok"
print('__RESULT__:')
print(json.dumps(s))"""

env_args = {'var_call_NnWZdbWfGHD4FiGAXvK4x62P': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_yQbzpnoaGFp0ZdJRegTFtr9B': 'file_storage/call_yQbzpnoaGFp0ZdJRegTFtr9B.json'}

exec(code, env_args)
