code = """import json

raw_output_string = locals()['var_function-call-5487041508530290549']['query_db_response']['results'][0]

# Find the starting point of the JSON array after the descriptive text
json_start_tag = '\n\nThe result is:\n'
json_start_index = raw_output_string.find(json_start_tag)

if json_start_index != -1:
    # Extract the substring containing the JSON data
    json_data_str = raw_output_string[json_start_index + len(json_start_tag):].strip()
    
    # The extracted string might still have some trailing characters or newlines. 
    # Ensure it's a clean JSON string before parsing.
    # It's an array, so it should start with '[' and end with ']'.
    # Find the last ']' to ensure we only parse the array.
    json_end_index = json_data_str.rfind(']')
    if json_end_index != -1:
        clean_json_data_str = json_data_str[:json_end_index + 1]
        businesses_with_parking_data = json.loads(clean_json_data_str)
        
        # Convert 'businessid_' to 'businessref_'
        business_refs = [
            item['business_id'].replace('businessid_', 'businessref_')
            for item in businesses_with_parking_data
        ]
        result = json.dumps(business_refs)
    else:
        result = json.dumps({"error": "Could not find the closing bracket of the JSON array."})
else:
    result = json.dumps({"error": "Could not find the start of the JSON data in the raw output."})

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5487041508530290549': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}]}

exec(code, env_args)
