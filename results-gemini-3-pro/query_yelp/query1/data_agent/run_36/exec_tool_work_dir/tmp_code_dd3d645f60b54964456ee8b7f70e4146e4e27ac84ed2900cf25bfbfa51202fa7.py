code = """ratings_data = locals()['var_function-call-2897166651186781145']
# ratings_data is a list of dicts like {'rating': '3'} or {'rating': 3}
# DuckDB usually returns the type of the column. The output showed "3" in quotes in the preview? 
# "The result is: [{"rating": "3"}, ...]" suggests they are strings? Or maybe just JSON formatting.
# I'll handle both.

values = []
for r in ratings_data:
    val = r['rating']
    values.append(float(val))

if len(values) > 0:
    avg_rating = sum(values) / len(values)
else:
    avg_rating = 0

print("__RESULT__:")
print(avg_rating)"""

env_args = {'var_function-call-15988406535249627409': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_function-call-14302379153309768124': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65'], 'var_function-call-16623191028114861952': "SELECT rating FROM review WHERE business_ref IN ('businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65')", 'var_function-call-2897166651186781145': [{'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '1'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}]}

exec(code, env_args)
