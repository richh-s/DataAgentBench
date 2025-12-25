code = """import json

# The output of the previous execute_python call is a JSON string.
# We need to parse this string to get the Python dictionary.
prev_python_result_str = locals()['var_function-call-16548434304143759758']['execute_python_response']['results'][0]

# Extract the JSON object from the string by finding the first and last curly braces.
start_index = prev_python_result_str.find('{')
end_index = prev_python_result_str.rfind('}')
clean_json_str = prev_python_result_str[start_index : end_index + 1]

parsed_data = json.loads(clean_json_str)

most_common_state = parsed_data['most_common_state']
business_ids_in_state = parsed_data['business_ids_in_state']

# Transform business_id (e.g., 'businessid_49') to business_ref (e.g., 'businessref_49').
business_refs = [biz_id.replace('businessid_', 'businessref_') for biz_id in business_ids_in_state]

# Create a comma-separated string of business_refs for the SQL IN clause.
# Ensure proper quoting for SQL string literals.
if business_refs:
    business_refs_sql = ", ".join([f"'{ref}'" for ref in business_refs])
else:
    business_refs_sql = "'''" # An empty string for IN clause will result in no matches

# Prepare the result for the next tool call, which will be a SQL query.
result_for_sql_query = {
    "most_common_state": most_common_state,
    "business_refs_sql_in_clause": business_refs_sql
}

print('__RESULT__:')
print(json.dumps(result_for_sql_query))"""

env_args = {'var_function-call-16548434304143759753': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
