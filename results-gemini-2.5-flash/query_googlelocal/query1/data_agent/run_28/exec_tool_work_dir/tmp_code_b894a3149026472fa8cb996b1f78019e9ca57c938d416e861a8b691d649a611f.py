code = """import json

# Access the raw result from the previous query_db call
db_result_obj = locals()['var_function-call-1486450293147361286']

# Extract the string containing the list of dictionaries
# This is a string, NOT a list of dictionaries directly
result_containing_json_string = db_result_obj['query_db_response']['results'][0]

# Find the start and end of the actual JSON array within the string
json_start_index = result_containing_json_string.find('[')
json_end_index = result_containing_json_string.rfind(']')

extracted_gmap_id_list = ""
extracted_business_names = {}

if json_start_index != -1 and json_end_index != -1:
    # Extract the pure JSON array string
    pure_json_array_str = result_containing_json_string[json_start_index : json_end_index + 1]
    
    # Parse the JSON string into a Python list of dictionaries
    parsed_business_data = json.loads(pure_json_array_str)
    
    # Extract gmap_ids and create a dictionary for business names
    gmap_ids_list = [business['gmap_id'] for business in parsed_business_data]
    extracted_business_names = {business['gmap_id']: business['name'] for business in parsed_business_data}
    
    # Format gmap_ids for use in a SQL IN clause
    extracted_gmap_id_list = ', '.join([f"'{gmap_id}'" for gmap_id in gmap_ids_list])

print('__RESULT__:')
print(json.dumps({
    'gmap_id_list': extracted_gmap_id_list,
    'business_names': extracted_business_names
}))"""

env_args = {'var_function-call-8585540486501776057': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_function-call-14517030998906174209': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-1486450293147361286': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
