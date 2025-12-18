code = """import json
import re

# Access the raw output dictionary from the previous query_db call.
# The variable var_function-call-17782452261993070973 holds the entire response object.
raw_output_dict = locals()['var_function-call-17782452261993070973']

# Navigate to the string that contains the actual JSON array.
# This string is inside 'query_db_response', then 'results', and it's the first element of that list.
full_string_with_json_array = raw_output_dict['query_db_response']['results'][0]

# Use a regular expression to find and extract the JSON array string itself.
# The pattern `r'\[.*\]'` looks for a literal '[', then any characters (`.`), 
# any number of times (`*`), and finally a literal ']'. `re.DOTALL` allows '.' to match newlines.
match = re.search(r'\[.*\]', full_string_with_json_array, re.DOTALL)

if match:
    json_array_string = match.group(0)
    
    # Parse the extracted JSON string into a Python list of dictionaries.
    businesses_la_data = json.loads(json_array_string)
    
    gmap_ids = []
    business_names_map = {}
    for business in businesses_la_data:
        gmap_ids.append(business['gmap_id'])
        business_names_map[business['gmap_id']] = business['name']
    
    # Format the gmap_ids into a comma-separated string, enclosed in single quotes, suitable for a SQL IN clause.
    gmap_ids_for_sql = ", ".join([f"'{gmap_id}'" for gmap_id in gmap_ids])
    
    # Output the formatted gmap_ids and the business names map as a JSON string.
    print('__RESULT__:')
    print(json.dumps({
        'gmap_ids_for_sql': gmap_ids_for_sql,
        'business_names_map': business_names_map
    }))
else:
    # If the JSON array string couldn't be found, print an error message.
    print('__RESULT__:')
    print(json.dumps("Error: Could not extract JSON array from the business_database query result."))"""

env_args = {'var_function-call-17782452261993070973': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
