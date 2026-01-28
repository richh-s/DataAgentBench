code = """import json
# var_call_vy1TeI7z7HQe5KJxkC3rbo6H is available from previous Mongo query
docs = var_call_vy1TeI7z7HQe5KJxkC3rbo6H
ids = [d['business_id'] for d in docs]
refs = [i.replace('businessid_', 'businessref_') for i in ids]
# construct SQL
in_list = ",".join("'{}'".format(r) for r in refs)
sql = "SELECT AVG(rating) as avg_rating FROM review WHERE business_ref IN (" + in_list + ");"
out = {"business_refs": refs, "sql": sql}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_CHAfkHriPCzOLQWQCl97jDjF': ['business', 'checkin'], 'var_call_DcKqgsXZ7v3E0pNTrmngmsYz': ['review', 'tip', 'user'], 'var_call_vy1TeI7z7HQe5KJxkC3rbo6H': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}]}

exec(code, env_args)
