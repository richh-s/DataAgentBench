code = """import json
# var_call_GHm1wLfsAnJFs4uAfaPlaLnj is available from previous query_db call
res = var_call_GHm1wLfsAnJFs4uAfaPlaLnj
avg_str = None
if res and isinstance(res, list) and len(res) > 0:
    avg_str = res[0].get('avg_rating')
try:
    avg = float(avg_str) if avg_str is not None else None
except Exception:
    avg = avg_str
output = json.dumps({"avg_rating": avg})
print("__RESULT__:")
print(output)"""

env_args = {'var_call_Z0K5kRY3eZjhu4onA1nOjd20': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}], 'var_call_GHm1wLfsAnJFs4uAfaPlaLnj': [{'avg_rating': '3.547008547008547'}]}

exec(code, env_args)
