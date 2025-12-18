code = """import json

# Access the string containing the JSON data
json_string_with_extra_info = locals()['var_function-call-8585540486501776057']['query_db_response']['results'][0]

# Extract the pure JSON array string from the response string
start_index = json_string_with_extra_info.find('[')
end_index = json_string_with_extra_info.rfind(']')

if start_index != -1 and end_index != -1:
    pure_json_array_str = json_string_with_extra_info[start_index : end_index + 1]
    # Parse the JSON array string
    business_data = json.loads(pure_json_array_str)
    # Extract gmap_ids
    gmap_ids = [business['gmap_id'] for business in business_data]
    # Format gmap_ids for SQL IN clause
    gmap_id_list = ', '.join([f"'{gmap_id}'" for gmap_id in gmap_ids])
else:
    gmap_id_list = ""

print('__RESULT__:')
print(json.dumps(gmap_id_list))"""

env_args = {'var_function-call-8585540486501776057': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
