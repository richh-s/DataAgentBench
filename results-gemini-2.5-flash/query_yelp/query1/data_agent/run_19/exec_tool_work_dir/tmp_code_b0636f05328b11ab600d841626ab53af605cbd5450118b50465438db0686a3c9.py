code = """import json

tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Find the starting position of the actual JSON array
json_start_tag = 'The result is:\n'
start_index = tool_output_str.find(json_start_tag)

if start_index != -1:
    # Adjust start_index to point to the beginning of the JSON array
    start_of_json_array = start_index + len(json_start_tag)
    
    # Find the end of the JSON array (before the last newline character)
    # We need to find the last ']' and include it.
    end_of_json_array = tool_output_str.rfind(']', start_of_json_array)
    
    if end_of_json_array != -1:
        # Slice the string to get only the JSON array part
        json_array_str = tool_output_str[start_of_json_array : end_of_json_array + 1].strip()
        
        # Parse the JSON string into a Python list of dictionaries
        business_ids_list = json.loads(json_array_str)
        
        # Transform business_id to business_ref format
        business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]
        
        print("__RESULT__:")
        print(json.dumps(business_refs))
    else:
        print("__RESULT__:")
        print(json.dumps([])) # Handle case where ']' is not found after the start tag
else:
    print("__RESULT__:")
    print(json.dumps([])) # Handle case where 'The result is:\n' is not found"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
