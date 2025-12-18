code = """import json
import re

# Access the raw result string from the first element of the 'results' list
full_output_string = locals()['var_function-call-9193542354770348498']['query_db_response']['results'][0]

# Split the string to get the part after 'The result is:\n'
json_start_indicator = 'The result is:\n'
parts = full_output_string.split(json_start_indicator, 1)

business_refs = []

if len(parts) > 1:
    json_part = parts[1].strip() # Get the part after the indicator and strip leading/trailing whitespace
    
    # The json_part might still have a trailing newline. Ensure it's clean.
    if json_part.endswith('\n'):
        json_part = json_part[:-1]

    try:
        businesses_data = json.loads(json_part)
        # Extract business_id and convert to business_ref format
        business_ids = [b['business_id'] for b in businesses_data]
        business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]
    except json.JSONDecodeError as e:
        # Handle cases where json_part is not a valid JSON string
        print(f'Error decoding JSON: {e}')
        print(f'Problematic JSON string: {json_part[:500]}...') # Print a snippet for debugging
else:
    print(f'Could not find \'{json_start_indicator}\' in the output string.')
    
print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-9137637729015947126': [], 'var_function-call-9193542354770348498': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}]}

exec(code, env_args)
