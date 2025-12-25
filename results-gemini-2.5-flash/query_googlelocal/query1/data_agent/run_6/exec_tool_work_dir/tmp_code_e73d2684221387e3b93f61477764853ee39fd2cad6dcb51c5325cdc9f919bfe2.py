code = """import json

# The entire dictionary output from the query_db tool
query_db_result = locals()['var_function-call-17782452261993070973']

# Access the list of results which is stored under 'results' key within 'query_db_response'
results_list_from_db = query_db_result['query_db_response']['results']

# The actual JSON array is the first (and only) element of this list, as a string
json_string_with_noise = results_list_from_db[0]

# Now, we need to extract only the JSON array part from this string.
# We will use string slicing by finding the first '[' and the last ']'
json_start = json_string_with_noise.find('[')
json_end = json_string_with_noise.rfind(']')

if json_start != -1 and json_end != -1:
    pure_json_array_string = json_string_with_noise[json_start : json_end + 1]
    
    # Attempt to parse the extracted JSON string
    businesses_la_data = json.loads(pure_json_array_string)
    
    gmap_ids = []
    business_names = {}
    for business in businesses_la_data:
        gmap_ids.append(business['gmap_id'])
        business_names[business['gmap_id']] = business['name']
    
    # Format gmap_ids for a SQL IN clause
    gmap_ids_for_sql = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])
    
    # Return the extracted gmap_ids and a dictionary mapping gmap_id to business name
    print('__RESULT__:')
    print(json.dumps({'gmap_ids_for_sql': gmap_ids_for_sql, 'business_names': business_names}))
else:
    print('__RESULT__:')
    print(json.dumps("Error: Could not find JSON array in the query result string."))"""

env_args = {'var_function-call-17782452261993070973': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
