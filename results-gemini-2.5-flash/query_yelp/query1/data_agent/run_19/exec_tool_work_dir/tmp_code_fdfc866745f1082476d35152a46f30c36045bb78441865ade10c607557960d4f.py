code = """import json
import re

tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Use regex to find the JSON array part. It starts with '[' and ends with ']'.
# re.DOTALL allows the match to span multiple lines.
match = re.search(r'\[.*\]', tool_output_str, re.DOTALL)

business_refs = []
if match:
    json_array_str = match.group(0) # Extract the matched JSON array string
    business_ids_list = json.loads(json_array_str)
    # Transform business_id to business_ref format
    business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]

print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
