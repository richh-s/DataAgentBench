code = """import json

tool_output_str = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]

# Split the string to isolate the JSON array part
parts = tool_output_str.split('The result is:\n')

business_refs = []
if len(parts) > 1:
    json_raw = parts[1].strip() # Get the part after "The result is:\n" and strip whitespace
    
    # The last character might be a newline, which needs to be removed before JSON parsing
    if json_raw.endswith('\n'):
        json_raw = json_raw[:-1]

    try:
        business_ids_list = json.loads(json_raw)
        business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]
    except json.JSONDecodeError as e:
        # Handle potential JSON parsing errors if the string format is unexpected
        print(f"JSON decoding error: {e}")

print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
