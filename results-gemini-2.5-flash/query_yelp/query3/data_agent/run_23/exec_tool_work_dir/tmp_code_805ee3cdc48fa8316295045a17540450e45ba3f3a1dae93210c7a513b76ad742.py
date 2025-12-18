code = """import json

# 1. Access the raw string result from the previous query_db call
full_output_string = locals()['var_function-call-5487041508530290549']['query_db_response']['results'][0]

# 2. Find the starting and ending indices of the actual JSON array within the string
json_start_index = full_output_string.find('[')
json_end_index = full_output_string.rfind(']')

# Check if both start and end delimiters were found
if json_start_index != -1 and json_end_index != -1:
    # 3. Extract the clean JSON array string
    clean_json_array_string = full_output_string[json_start_index : json_end_index + 1]
    
    # Load the JSON string into a Python list of dictionaries
    businesses_with_parking_data = json.loads(clean_json_array_string)
    
    # 4. Extract business_id and convert to business_ref format
    business_refs_with_parking = [
        business['business_id'].replace('businessid_', 'businessref_')
        for business in businesses_with_parking_data
    ]
    result = json.dumps(business_refs_with_parking)
else:
    result = json.dumps({"error": "Failed to extract the JSON array from the full output string."})

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5487041508530290549': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}]}

exec(code, env_args)
