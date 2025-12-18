code = """import json

raw_output = locals()['var_function-call-14344633744705754954']['results'][0]

# Extract the JSON array string
json_str_start = raw_output.find('[')
json_str_end = raw_output.rfind(']')
json_array_str = raw_output[json_str_start : json_str_end + 1]

business_data = json.loads(json_array_str)

business_ids_with_parking = [b['business_id'] for b in business_data]

print('__RESULT__:')
print(json.dumps(business_ids_with_parking))"""

env_args = {'var_function-call-14344633744705754954': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}]}

exec(code, env_args)
