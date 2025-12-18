code = """import json
businesses_with_parking_raw = locals()['var_function-call-7389110403641624083']['results'][0]
businesses_with_parking = json.loads(business_with_parking_raw)
business_ids = [b['business_id'].replace('businessid_', 'businessref_') for b in businesses_with_parking]
print('__RESULT__:')
print(json.dumps(business_ids))"""

env_args = {'var_function-call-7389110403641624083': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}]}

exec(code, env_args)
