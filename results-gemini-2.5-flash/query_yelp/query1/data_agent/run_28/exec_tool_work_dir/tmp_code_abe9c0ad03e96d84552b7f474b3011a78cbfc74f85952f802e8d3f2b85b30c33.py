code = """import json
db_response_string = locals()['var_function-call-112503369141994388']['results'][0]
start_index = db_response_string.find('[')
end_index = db_response_string.rfind(']') + 1
json_list_string = db_response_string[start_index:end_index]
business_data = json.loads(json_list_string)
business_ids = [item['business_id'] for item in business_data]
transformed_business_refs = [f"businessref_{bid.split('_')[1]}" for bid in business_ids]
print("__RESULT__:")
print(json.dumps(transformed_business_refs))"""

env_args = {'var_function-call-112503369141994388': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
