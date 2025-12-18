code = """import json

tool_output = locals()['var_function-call-7627877634880759450']
raw_string_result = tool_output['query_db_response']['results'][0]

json_start_tag = "The result is:\n"
start_index = raw_string_result.find(json_start_tag)

business_refs = []
if start_index != -1:
    json_part = raw_string_result[start_index + len(json_start_tag):].strip()
    
    json_array_start = json_part.find('[')
    json_array_end = json_part.rfind(']')

    if json_array_start != -1 and json_array_end != -1:
        clean_json_str = json_part[json_array_start : json_array_end + 1]
        business_ids_list = json.loads(clean_json_str)
        business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids_list]

print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
