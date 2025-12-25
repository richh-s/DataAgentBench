code = """import json
business_data = locals()['var_function-call-112503369141994388']['query_db_response']['results']
business_refs = [f"businessref_{d['business_id'].split('_')[1]}" for d in business_data]
business_refs_str = ", ".join([f"'{ref}'" for ref in business_refs])
print("__RESULT__:")
print(json.dumps(business_refs_str))"""

env_args = {'var_function-call-112503369141994388': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
