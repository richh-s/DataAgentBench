code = """import json

raw_output_string = locals()['var_function-call-5487041508530290549']['query_db_response']['results'][0]

# Define the separator string that marks the beginning of the JSON data
separator = '\n\nThe result is:\n'

# Find the index of the separator
start_index = raw_output_string.find(separator)

if start_index != -1:
    # Extract the substring after the separator and strip leading/trailing whitespace
    json_part = raw_output_string[start_index + len(separator):].strip()
    
    # Load the JSON string into a Python list of dictionaries
    businesses_with_parking_data = json.loads(json_part)
    
    # Extract business_id and convert to business_ref format
    business_refs_with_parking = [
        business['business_id'].replace('businessid_', 'businessref_')
        for business in businesses_with_parking_data
    ]
    result = json.dumps(business_refs_with_parking)
else:
    result = json.dumps({"error": "Could not find the JSON data in the input string."})

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-5487041508530290549': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}]}

exec(code, env_args)
