code = """import json

raw_json_string = locals()['var_function-call-5487041508530290549']['query_db_response']['results'][0]
businesses_with_parking_data = json.loads(raw_json_string)

business_refs_with_parking = [
    business['business_id'].replace('businessid_', 'businessref_')
    for business in businesses_with_parking_data
]

print('__RESULT__:')
print(json.dumps(business_refs_with_parking))"""

env_args = {'var_function-call-5487041508530290549': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}]}

exec(code, env_args)
