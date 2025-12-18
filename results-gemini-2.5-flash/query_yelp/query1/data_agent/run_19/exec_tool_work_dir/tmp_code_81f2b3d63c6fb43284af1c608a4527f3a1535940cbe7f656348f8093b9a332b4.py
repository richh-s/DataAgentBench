code = """import json
import re

# Access the raw string output from the previous tool call
tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Find the starting and ending markers for the JSON array
start_marker = 'The result is:\n'
end_marker = '\n'

start_index = tool_output_str.find(start_marker)
if start_index != -1:
    json_start = start_index + len(start_marker)
    json_end = tool_output_str.rfind(end_marker, json_start)
    if json_end != -1:
        json_array_str = tool_output_str[json_start:json_end].strip()
        
        # Now parse the JSON string
        business_ids_list = json.loads(json_array_str)
        
        # Extract the numerical part of business_id and prepend 'businessref_'
        business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]
        print("__RESULT__:")
        print(json.dumps(business_refs))
    else:
        print("__RESULT__:")
        print(json.dumps([])) # Handle case where end marker is not found
else:
    print("__RESULT__:")
    print(json.dumps([])) # Handle case where start marker is not found"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
