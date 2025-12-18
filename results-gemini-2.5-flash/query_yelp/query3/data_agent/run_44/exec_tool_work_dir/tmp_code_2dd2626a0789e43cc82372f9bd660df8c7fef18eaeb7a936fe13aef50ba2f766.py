code = """import pandas as pd
import json
business_data_str = locals()['var_function-call-14344633744705754954']['results'][0]
business_data_list = json.loads(business_data_str)
business_ids_with_parking = [b['business_id'] for b in business_data_list if 'business_id' in b]
print('__RESULT__:')
print(pd.Series(business_ids_with_parking).to_json(orient='records'))"""

env_args = {'var_function-call-14344633744705754954': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BikeParking': 'True'}}]}

exec(code, env_args)
