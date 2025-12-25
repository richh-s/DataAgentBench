code = """import json

data = locals()['var_function-call-14154448410546726092']
# data is a list of dicts: [{'business_id': 'businessid_52'}, ...]

# Extract IDs and change prefix
business_refs = []
for item in data:
    bid = item['business_id']
    # replace businessid_ with businessref_
    bref = bid.replace('businessid_', 'businessref_')
    business_refs.append(bref)

# Format for SQL IN clause
sql_list = ", ".join([f"'{x}'" for x in business_refs])
print("__RESULT__:")
print(json.dumps(sql_list))"""

env_args = {'var_function-call-14154448410546726092': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}]}

exec(code, env_args)
