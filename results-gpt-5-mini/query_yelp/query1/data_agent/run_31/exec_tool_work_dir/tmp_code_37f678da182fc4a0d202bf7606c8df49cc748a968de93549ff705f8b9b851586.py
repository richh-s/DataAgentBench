code = """import json
# Access the query result from the reviews aggregation
data = var_call_2PAhlAN2xSLABtN7Hcxsl2FP
# Convert and compute weighted average
total_reviews = 0
sum_ratings = 0.0
for r in data:
    cnt = int(r['cnt'])
    avg = float(r['avg_rating'])
    total_reviews += cnt
    sum_ratings += avg * cnt
overall_average = None
if total_reviews > 0:
    overall_average = sum_ratings / total_reviews
# Prepare result
result = {
    'overall_average_rating': None if overall_average is None else round(overall_average, 4),
    'total_reviews_used': total_reviews,
    'business_count': len(data)
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GsnCm6jWcueVtqC59o5brF2Y': [{'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}, {'business_id': 'businessid_94', 'name': 'Taste of Europe', 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'business_id': 'businessid_90', 'name': "Long John Silver's", 'description': 'Located at 2831 E 38th St in Indianapolis, IN, this establishment offers a diverse menu featuring Fast Food, Seafood, Restaurants, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_16', 'name': 'Fox and Hound English Pub and Grille', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}], 'var_call_rPmAgDyQCLenToBhGgZZ9mMu': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65', 'businessref_94', 'businessref_90', 'businessref_16'], 'var_call_2PAhlAN2xSLABtN7Hcxsl2FP': [{'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'cnt': '6'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439', 'cnt': '41'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'cnt': '6'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0', 'cnt': '3'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666', 'cnt': '30'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'cnt': '18'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'cnt': '4'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'cnt': '9'}]}

exec(code, env_args)
