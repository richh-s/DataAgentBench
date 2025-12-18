code = """import json
import re

raw_string = locals()['var_function-call-112503369141994388']['results'][0]

# Extract the JSON array string using regex
match = re.search(r'\[.*\]', raw_string, re.DOTALL)
if match:
    json_array_string = match.group(0)
else:
    json_array_string = '[]'

business_list = json.loads(json_array_string)
business_ids = [b['business_id'] for b in business_list]
transformed_business_refs = [f"businessref_{bid.split('_')[1]}" for bid in business_ids]
print("__RESULT__:")
print(json.dumps(transformed_business_refs))"""

env_args = {'var_function-call-112503369141994388': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
