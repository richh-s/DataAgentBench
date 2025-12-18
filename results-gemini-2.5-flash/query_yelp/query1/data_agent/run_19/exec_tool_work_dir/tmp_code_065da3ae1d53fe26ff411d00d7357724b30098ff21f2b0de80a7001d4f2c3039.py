code = """import json

tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Find the first occurrence of '[' and the last occurrence of ']'
start_index = tool_output_str.find('[')
end_index = tool_output_str.rfind(']')

business_refs = []
if start_index != -1 and end_index != -1:
    # Extract the substring that contains the JSON array
    json_array_str = tool_output_str[start_index : end_index + 1]
    
    # Parse the JSON string into a Python list of dictionaries
    business_ids_list = json.loads(json_array_str)
    
    # Transform business_id (e.g., "businessid_52") to business_ref (e.g., "businessref_52")
    business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]

print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
