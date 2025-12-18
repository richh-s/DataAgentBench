code = """import json

# The actual result is inside the 'results' list, as a string containing a JSON array.
raw_json_string = locals()['var_function-call-112503369141994388']['query_db_response']['results'][0]

# Parse the string into a Python list of dictionaries
business_data = json.loads(raw_json_string)

# Extract business_ids and transform them to business_ref format
business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_data]

# Prepare the business_refs for SQL IN clause
business_refs_str = ", ".join([f"'{ref}'" for ref in business_refs])

print("__RESULT__:")
print(json.dumps(business_refs_str))"""

env_args = {'var_function-call-112503369141994388': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
