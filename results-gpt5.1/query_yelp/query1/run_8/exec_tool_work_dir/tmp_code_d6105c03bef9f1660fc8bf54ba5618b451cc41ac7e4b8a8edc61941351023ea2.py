code = """import json
biz_records = var_call_e1eGOJ0u9nfyskdQwjTTEFUW
# convert businessid_ prefixes to businessref_
ids = [r['business_id'].replace('businessid_','businessref_') for r in biz_records]
placeholders = ','.join(["'"+i+"'" for i in ids])
query = f"SELECT AVG(rating) as avg_rating FROM review WHERE business_ref IN ({placeholders});"
result = json.dumps(query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_hU7wQqLbUl5TtcHdMvaRQMAf': [], 'var_call_TMxiD1V0gHYrNeTjpqSgnIdj': ['review', 'tip', 'user'], 'var_call_e1eGOJ0u9nfyskdQwjTTEFUW': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
