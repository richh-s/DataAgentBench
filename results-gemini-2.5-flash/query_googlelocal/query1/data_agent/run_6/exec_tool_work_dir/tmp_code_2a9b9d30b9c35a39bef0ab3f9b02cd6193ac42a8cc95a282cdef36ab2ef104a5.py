code = """import json
import re

# Access the raw output from the previous query_db call
raw_output_dict = locals()['var_function-call-17782452261993070973']
query_results = raw_output_dict['query_db_response']['results']

businesses_la = []
gmap_ids = []

# The query_results is a list containing a single string which itself contains the JSON array
# We need to extract the JSON array string from that single string
full_string_output = query_results[0]

# Use regex to find the JSON array part of the string
match = re.search(r'\[.*\]', full_string_output, re.DOTALL)

if match:
    json_array_string = match.group(0)
    
    # Parse the JSON string into a Python list of dictionaries
    businesses_data = json.loads(json_array_string)
    
    for business in businesses_data:
        businesses_la.append({'gmap_id': business['gmap_id'], 'name': business['name']})
        gmap_ids.append(business['gmap_id'])
    
    # Prepare the gmap_ids for use in a SQL IN clause
    gmap_ids_for_sql = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])
    
    print('__RESULT__:')
    print(json.dumps({'gmap_ids_for_sql': gmap_ids_for_sql, 'businesses_la': businesses_la}))
else:
    print('__RESULT__:')
    print(json.dumps("Error: Could not extract JSON array from the business_database query result."))"""

env_args = {'var_function-call-17782452261993070973': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
