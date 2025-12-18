code = """import json
import pandas as pd
raw_output_string = locals()['var_function-call-3617225813010664277']['query_db_response']['results'][0]
# Extract the JSON part from the raw output string
json_start_index = raw_output_string.find('[')
json_end_index = raw_output_string.rfind(']') + 1
json_string = raw_output_string[json_start_index:json_end_index]

all_businesses = json.loads(json_string)
business_ids_with_parking = [b['business_id'].replace('businessid_', 'businessref_') for b in all_businesses]
business_ids_str = ', '.join(f"'{bid}'" for bid in business_ids_with_parking)

print("__RESULT__:")
print(json.dumps(business_ids_str))"""

env_args = {'var_function-call-3617225813010664277': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33'}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}]}

exec(code, env_args)
