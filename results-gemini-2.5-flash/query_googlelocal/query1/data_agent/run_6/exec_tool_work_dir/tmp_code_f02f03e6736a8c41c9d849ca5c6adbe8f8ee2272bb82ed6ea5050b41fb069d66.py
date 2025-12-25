code = """import json

# Access the raw output from the previous query_db call
raw_output = locals()['var_function-call-17782452261993070973']

# The actual business data is in 'query_db_response' -> 'results' which is a list of JSON strings.
business_json_strings = raw_output['query_db_response']['results']

businesses_la_data = []
for json_str in business_json_strings:
    # Each item in the list is a string representation of a JSON object. We need to parse it.
    # However, the string contains additional text like '\nThe tool query_db was executed successfully.\n\nThe result is stored under key...' 
    # and then the actual JSON. We need to extract only the JSON part.
    
    # Find the start and end of the actual JSON array within the string
    json_start = json_str.find('[')
    json_end = json_str.rfind(']')
    
    if json_start != -1 and json_end != -1:
        pure_json_array_string = json_str[json_start : json_end + 1]
        businesses_la_data.extend(json.loads(pure_json_array_string))
    else:
        print('__RESULT__:')
        print(json.dumps("Error: Could not extract JSON array from one of the result strings."))
        exit() # Exit if we can't parse the input properly

gmap_ids = []
business_names = {}
for business in businesses_la_data:
    gmap_ids.append(business['gmap_id'])
    business_names[business['gmap_id']] = business['name']

# Prepare the gmap_ids for use in a SQL IN clause
gmap_ids_for_sql = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])

# Return both the formatted gmap_ids and the mapping of gmap_id to business names
print('__RESULT__:')
print(json.dumps({'gmap_ids_for_sql': gmap_ids_for_sql, 'business_names': business_names}))"""

env_args = {'var_function-call-17782452261993070973': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
