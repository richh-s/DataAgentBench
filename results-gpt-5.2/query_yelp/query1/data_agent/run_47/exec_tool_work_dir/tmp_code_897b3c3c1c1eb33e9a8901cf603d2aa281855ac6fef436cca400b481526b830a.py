code = """import json
biz_ids = [r['business_id'] for r in var_call_bDUSycNeMlCHtFAHK0b3WJW9]
biz_refs = ['businessref_' + x[len('businessid_'):] if x.startswith('businessid_') else x for x in biz_ids]
# Build SQL
in_list = ','.join(["'"+s.replace("'","''")+"'" for s in biz_refs])
sql = f"SELECT AVG(rating) AS avg_rating, COUNT(*) AS review_count FROM review WHERE business_ref IN ({in_list});"
print('__RESULT__:')
print(json.dumps({'sql': sql, 'business_count': len(biz_refs)}))"""

env_args = {'var_call_PxSslBynkRUDo0XZ4LE17jch': [], 'var_call_tEH8OvfVCdf2of6YP3eNfjCL': {'avg_rating': None, 'business_count': 0, 'review_count': 0}, 'var_call_wrJclx9MZdivVqkGiegn2h0V': [{'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_call_bDUSycNeMlCHtFAHK0b3WJW9': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
