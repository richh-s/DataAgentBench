code = """import json, pandas as pd
rev = pd.DataFrame(var_call_NnWZdbWfGHD4FiGAXvK4x62P)
print('__RESULT__:')
print(json.dumps(rev.to_dict(orient='records')))"""

env_args = {'var_call_NnWZdbWfGHD4FiGAXvK4x62P': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_cnt': '5'}], 'var_call_yQbzpnoaGFp0ZdJRegTFtr9B': 'file_storage/call_yQbzpnoaGFp0ZdJRegTFtr9B.json', 'var_call_HSqc8acVK43azoiL0surb8TK': 'ok'}

exec(code, env_args)
