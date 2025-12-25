code = """import json
import re

# Access the raw string output from the previous tool call
tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Extract the JSON array string from the tool output string
# The regex specifically looks for the content between 'The result is:\n' and the final ']\n'
match = re.search(r'The result is:\n(\[.*?\])\n', tool_output_str, re.DOTALL)

if match:
    json_array_str = match.group(1)
    business_ids_list = json.loads(json_array_str)
    # Extract the numerical part of business_id and prepend 'businessref_'
    business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]
    print("__RESULT__:")
    print(json.dumps(business_refs))
else:
    print("__RESULT__:")
    print(json.dumps([])) # Return empty list if no JSON array found"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
