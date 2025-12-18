code = """import json

# Access the raw result string which contains the JSON array along with other text
raw_output_string = locals()['var_function-call-9193542354770348498']['query_db_response']['results'][0]

# Find the start and end of the JSON array within the string
start_index = raw_output_string.find('[')
end_index = raw_output_string.rfind(']')

business_refs = []

if start_index != -1 and end_index != -1 and end_index > start_index:
    # Extract only the JSON array string
    json_array_string = raw_output_string[start_index : end_index + 1]
    
    try:
        # Parse the JSON string into a Python list of dictionaries
        all_businesses_data = json.loads(json_array_string)
        
        # Extract business_id and convert to business_ref format
        business_ids = [business['business_id'] for business in all_businesses_data]
        business_refs = [business_id.replace('businessid_', 'businessref_') for business_id in business_ids]
    except json.JSONDecodeError as e:
        # In case of a JSON parsing error, log it or handle appropriately
        print(f'Error decoding JSON: {e}')
        print(f'Problematic JSON string snippet: {json_array_string[:200]}...')
else:
    print('Could not find a valid JSON array in the output string.')

print('__RESULT__:')
print(json.dumps(business_refs))"""

env_args = {'var_function-call-9137637729015947126': [], 'var_function-call-9193542354770348498': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}]}

exec(code, env_args)
