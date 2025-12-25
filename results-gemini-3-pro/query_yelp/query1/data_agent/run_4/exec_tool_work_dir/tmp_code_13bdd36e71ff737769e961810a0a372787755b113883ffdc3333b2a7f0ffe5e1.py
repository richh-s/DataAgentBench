code = """import json
results = [
    {"business_ref": "businessref_87", "avg_rating": 3.3333333333333335},
    {"business_ref": "businessref_52", "avg_rating": 4.166666666666667},
    {"business_ref": "businessref_84", "avg_rating": 5.0},
    {"business_ref": "businessref_65", "avg_rating": 3.8333333333333335},
    {"business_ref": "businessref_76", "avg_rating": 3.5555555555555554}
]

avg_ratings = [r["avg_rating"] for r in results]
final_avg = sum(avg_ratings) / len(avg_ratings)
print("__RESULT__:")
print(json.dumps(final_avg))"""

env_args = {'var_function-call-12855300519507406502': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_function-call-5192856011108809389': [{'avg(rating)': '3.86046511627907'}], 'var_function-call-2912876273890816750': [{'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}]}

exec(code, env_args)
