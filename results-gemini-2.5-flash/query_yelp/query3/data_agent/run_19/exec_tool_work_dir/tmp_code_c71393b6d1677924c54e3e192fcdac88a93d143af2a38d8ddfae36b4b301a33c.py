code = """import json

business_parking_bike_parking_list = locals()['var_function-call-12258439588567494621']['query_db_response']['results']

business_ids_with_parking = [b['business_id'] for b in business_parking_bike_parking_list]

business_ref_ids_with_parking = [bid.replace('businessid_', 'businessref_') for bid in business_ids_with_parking]

print('__RESULT__:')
print(json.dumps(business_ref_ids_with_parking))"""

env_args = {'var_function-call-12258439588567494621': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}]}

exec(code, env_args)
