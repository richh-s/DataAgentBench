code = """import json, pandas as pd
biz = pd.DataFrame(var_call_uLw6tlIZ9rsdq1jE5m9Xqkuz)
# map businessid_X -> businessref_X
biz['business_ref'] = biz['business_id'].str.replace('businessid_','businessref_', regex=False)
refs = biz['business_ref'].tolist()
print('__RESULT__:')
print(json.dumps({'refs': refs, 'n': len(refs)}))"""

env_args = {'var_call_82R1n38vOiowThOkjQ9Q7tgn': [], 'var_call_g4g8muKdZXidEgOXFZQb8DU2': [{'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_call_uLw6tlIZ9rsdq1jE5m9Xqkuz': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}]}

exec(code, env_args)
