code = """import json
tool_output = locals()['var_function-call-7627877634880759450']['query_db_response']['results'][0]
start_tag = 'The result is:\n'
end_tag = '\n'
start_index = tool_output.find(start_tag) + len(start_tag)
end_index = tool_output.rfind(end_tag)
business_ids_json_str = tool_output[start_index:end_index].strip()
business_ids = json.loads(business_ids_json_str)
business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_ids]
print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
