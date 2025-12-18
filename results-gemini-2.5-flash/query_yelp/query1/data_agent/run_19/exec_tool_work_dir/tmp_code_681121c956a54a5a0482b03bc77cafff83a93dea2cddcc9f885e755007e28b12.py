code = """import json
business_ids_raw = locals()['var_function-call-7627877634880759450']['results'][0]
business_ids_json_str = business_ids_raw.split('The result is:\n', 1)[1].strip()
business_ids = json.loads(business_ids_json_str)
business_refs = [f'businessref_{d['business_id'].split('_')[1]}' for d in business_ids]
print("__RESULT__:")
print(json.dumps(business_refs))"""

env_args = {'var_function-call-7627877634880759450': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
