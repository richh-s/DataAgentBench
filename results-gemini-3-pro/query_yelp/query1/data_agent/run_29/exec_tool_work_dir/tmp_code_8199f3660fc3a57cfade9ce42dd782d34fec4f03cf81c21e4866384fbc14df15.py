code = """import json

# Load the result from the previous step
data = locals()['var_function-call-12754685981999529559']

# If it's a file path, load it. If it's a list, use it directly.
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        businesses = json.load(f)
else:
    businesses = data

# Extract business IDs and filter strictly if needed (though query did it)
# Just to be safe, ensure 'Indianapolis' and 'IN' are in description
indy_businesses = []
for b in businesses:
    desc = b.get('description', '')
    if 'Indianapolis' in desc and 'IN' in desc:
        indy_businesses.append(b['business_id'])

# Transform IDs
# businessid_X -> businessref_X
indy_refs = [bid.replace('businessid_', 'businessref_') for bid in indy_businesses]

print(f"Found {len(indy_businesses)} businesses in Indianapolis.")
print(f"First few refs: {indy_refs[:5]}")

# Prepare the formatted string for SQL IN clause
# If list is empty, handle it
if not indy_refs:
    sql_list = "('')"
else:
    # SQL strings need quotes
    sql_list = "(" + ", ".join([f"'{ref}'" for ref in indy_refs]) + ")"

print("__RESULT__:")
print(json.dumps(sql_list))"""

env_args = {'var_function-call-12754685981999529559': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}]}

exec(code, env_args)
