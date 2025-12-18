code = """import json
import re

# The raw string contains extra text around the actual JSON array.
raw_output_string = locals()['var_function-call-112503369141994388']['results'][0]

# Use regex to find the JSON array part of the string.
# This pattern looks for a string that starts with '[' and ends with ']', capturing everything in between.
match = re.search(r'(\[.*\])', raw_output_string, re.DOTALL)

if match:
    json_string = match.group(1)
else:
    json_string = '[]' # Default to an empty list if no JSON array is found

business_data = json.loads(json_string)
business_ids = [item['business_id'] for item in business_data]

# Transform business_id to business_ref format
transformed_business_refs = [f"businessref_{bid.split('_')[1]}" for bid in business_ids]

print("__RESULT__:")
print(json.dumps(transformed_business_refs))"""

env_args = {'var_function-call-112503369141994388': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
