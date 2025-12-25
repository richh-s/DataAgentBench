code = """import json

tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Find the starting point of the actual JSON array
start_marker = "The result is:\n"
start_idx = tool_output_str.find(start_marker)

business_refs = []
if start_idx != -1:
    # Get the substring that potentially contains the JSON array
    json_potential_str = tool_output_str[start_idx + len(start_marker):].strip()
    
    # Find the actual start and end of the JSON array within this substring
    array_start_idx = json_potential_str.find('[')
    array_end_idx = json_potential_str.rfind(']')
    
    if array_start_idx != -1 and array_end_idx != -1:
        json_array_str = json_potential_str[array_start_idx : array_end_idx + 1]
        business_ids_list = json.loads(json_array_str)
        business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]

print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
