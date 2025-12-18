code = """import json

# Access the raw output from the previous query_db call
raw_output_dict = locals()['var_function-call-17782452261993070973']

# The actual query results are nested. Access the 'results' list inside 'query_db_response'.
# The 'results' list contains a single string, which holds the JSON array along with other text.
result_string_with_noise = raw_output_dict['query_db_response']['results'][0]

# Find the starting and ending indices of the actual JSON array within the string.
# The JSON array starts with '[' and ends with ']'.
json_start_index = result_string_with_noise.find('[')
json_end_index = result_string_with_noise.rfind(']')

# Check if both start and end delimiters were found
if json_start_index != -1 and json_end_index != -1:
    # Extract the pure JSON array string using slicing
    pure_json_array_string = result_string_with_noise[json_start_index : json_end_index + 1]
    
    # Parse the extracted JSON string into a Python list of dictionaries
    businesses_la_data = json.loads(pure_json_array_string)
    
    gmap_ids = []
    business_names = {}
    for business in businesses_la_data:
        gmap_ids.append(business['gmap_id'])
        business_names[business['gmap_id']] = business['name']
    
    # Prepare the gmap_ids for use in a SQL IN clause (e.g., 'id1', 'id2', ...)
    gmap_ids_for_sql = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])
    
    # Return both the formatted gmap_ids and the mapping of gmap_id to business names
    print('__RESULT__:')
    print(json.dumps({'gmap_ids_for_sql': gmap_ids_for_sql, 'business_names': business_names}))
else:
    print('__RESULT__:')
    print(json.dumps("Error: Could not extract JSON array from the business_database query result."))"""

env_args = {'var_function-call-17782452261993070973': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
