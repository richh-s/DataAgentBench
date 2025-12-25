code = """import json

raw_result_string = locals()['var_function-call-6581138237843065961']['query_db_response']['results'][0]
json_start_tag = "The result is:\n"
start_index = raw_result_string.find(json_start_tag) + len(json_start_tag)
json_data_string = raw_result_string[start_index:]

business_with_parking_data = json.loads(json_data_string)
business_ids_with_parking = [item['business_id'] for item in business_with_parking_data]
business_refs_with_parking = [bid.replace('businessid_', 'businessref_') for bid in business_ids_with_parking]

__RESULT__:
print(json.dumps(business_refs_with_parking))"""

env_args = {'var_function-call-6581138237843065961': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}]}

exec(code, env_args)
