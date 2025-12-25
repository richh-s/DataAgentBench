code = """import json

# Access the result string correctly
raw_output_string = locals()['var_function-call-12258439588567494621']['query_db_response']['results'][0]

# Extract the JSON list string
start_json_index = raw_output_string.find('[')
end_json_index = raw_output_string.rfind(']')
json_list_string = raw_output_string[start_json_index : end_json_index + 1]

# Parse the JSON string into a Python list of dictionaries
business_parking_bike_parking_list = json.loads(json_list_string)

# Extract business_ids and convert to business_ref format
business_ids_with_parking = [b['business_id'] for b in business_parking_bike_parking_list]
business_ref_ids_with_parking = [bid.replace('businessid_', 'businessref_') for bid in business_ids_with_parking]

# Prepare the IN clause for the SQL query
in_clause = ', '.join([f"'{bid}'" for bid in business_ref_ids_with_parking])

print('__RESULT__:')
print(json.dumps(in_clause))"""

env_args = {'var_function-call-12258439588567494621': [{'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}]}

exec(code, env_args)
