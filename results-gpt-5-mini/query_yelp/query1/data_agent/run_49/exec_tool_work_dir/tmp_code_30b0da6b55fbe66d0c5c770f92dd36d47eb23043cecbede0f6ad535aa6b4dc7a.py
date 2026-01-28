code = """import json
# var_call_9huglAQsE5QOL0YcmtRND9up is available from previous query
data = var_call_9huglAQsE5QOL0YcmtRND9up
# Convert strings to numeric and compute weighted average across reviews
total_reviews = 0
weighted_sum = 0.0
for row in data:
    count = int(row['review_count'])
    avg = float(row['avg_rating'])
    total_reviews += count
    weighted_sum += avg * count
overall_avg = None
if total_reviews > 0:
    overall_avg = weighted_sum / total_reviews
# Also compute unweighted average of per-business averages for reference
unweighted_sum = sum(float(r['avg_rating']) for r in data)
num_businesses = len(data)
unweighted_avg = unweighted_sum / num_businesses if num_businesses > 0 else None
# Prepare result string
if overall_avg is None:
    message = "No reviews found for businesses in Indianapolis, Indiana."
else:
    message = f"The average rating of all businesses located in Indianapolis, Indiana is {overall_avg:.4f} based on {total_reviews} reviews across {num_businesses} businesses. (Unweighted average of business averages = {unweighted_avg:.4f})"
# Print result following required format
print("__RESULT__:")
print(json.dumps(message))"""

env_args = {'var_call_FJdfJgrfFqArLgtohgP7tQ6g': ['checkin', 'business'], 'var_call_3HuITjVOcDeToIEALbi1friu': [{'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_call_9huglAQsE5QOL0YcmtRND9up': [{'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'review_count': '4'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'review_count': '9'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'review_count': '18'}]}

exec(code, env_args)
