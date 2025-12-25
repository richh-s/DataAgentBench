code = """ids = [item['business_id'] for item in locals()['var_function-call-147862100875464376']]
# Convert businessid_X to businessref_X
refs = [id.replace('businessid_', 'businessref_') for id in ids]
# Format for SQL IN clause
refs_str = "', '".join(refs)
query = f"SELECT AVG(rating) as average_rating FROM review WHERE business_ref IN ('{refs_str}')"
print("__RESULT__:")
print(f'"{query}"')"""

env_args = {'var_function-call-147862100875464376': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
