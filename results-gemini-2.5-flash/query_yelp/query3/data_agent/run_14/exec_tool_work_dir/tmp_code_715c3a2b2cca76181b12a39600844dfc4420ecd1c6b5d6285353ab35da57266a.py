code = """import json
import re
raw_output_string = locals()['var_function-call-3617225813010664277']['query_db_response']['results'][0]
start_marker = 'The result is:\n'
end_marker = '\n'
start_index = raw_output_string.find(start_marker) + len(start_marker)
end_index = raw_output_string.rfind(end_marker)
json_data_str = raw_output_string[start_index:end_index]

all_businesses = json.loads(json_data_str)
business_ids_with_parking = [b['business_id'].replace('businessid_', 'businessref_') for b in all_businesses]
business_ids_str = ', '.join(f"'{bid}'" for bid in business_ids_with_parking)

print("__RESULT__:")
print(json.dumps(business_ids_str))"""

env_args = {'var_function-call-3617225813010664277': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}]}

exec(code, env_args)
