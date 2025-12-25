code = """import json
biz_ids_1 = [b['business_id'] for b in var_call_xwlH8KMr7Jj9fwvgR8oXNjUs]
biz_ids_2 = [b['business_id'] for b in var_call_cRXstARlK1sj68liCvqKyCjc]
all_ids = sorted(set(biz_ids_1 + biz_ids_2))
result = json.dumps(all_ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_xwlH8KMr7Jj9fwvgR8oXNjUs': [], 'var_call_cRXstARlK1sj68liCvqKyCjc': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
