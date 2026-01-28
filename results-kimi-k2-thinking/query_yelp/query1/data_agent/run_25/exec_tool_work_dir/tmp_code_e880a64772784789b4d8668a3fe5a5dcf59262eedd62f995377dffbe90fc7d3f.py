code = """import json

# Get the reviews data
reviews_data = [
    {"business_ref": "businessref_65", "rating": "3"}, {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "5"}, {"business_ref": "businessref_87", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_87", "rating": "4"}, 
    {"business_ref": "businessref_84", "rating": "5"}, {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_52", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "3"}, {"business_ref": "businessref_65", "rating": "5"}, 
    {"business_ref": "businessref_52", "rating": "5"}, {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_76", "rating": "3"}, {"business_ref": "businessref_52", "rating": "2"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_52", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "3"}, {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_84", "rating": "5"}, {"business_ref": "businessref_76", "rating": "1"}, 
    {"business_ref": "businessref_65", "rating": "3"}, {"business_ref": "businessref_87", "rating": "1"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_87", "rating": "4"}, {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_87", "rating": "1"}, {"business_ref": "businessref_52", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "5"}, {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_65", "rating": "3"}, 
    {"business_ref": "businessref_76", "rating": "4"}, {"business_ref": "businessref_65", "rating": "4"}, 
    {"business_ref": "businessref_87", "rating": "5"}, {"business_ref": "businessref_52", "rating": "5"}, 
    {"business_ref": "businessref_76", "rating": "4"}, {"business_ref": "businessref_84", "rating": "5"}, 
    {"business_ref": "businessref_65", "rating": "4"}, {"business_ref": "businessref_76", "rating": "4"}, 
    {"business_ref": "businessref_76", "rating": "5"}
]

# Calculate average rating
total_rating = 0
total_reviews = len(reviews_data)

for review in reviews_data:
    total_rating += int(review["rating"])

average_rating = total_rating / total_reviews
print('__RESULT__:')
print(json.dumps({"average_rating": average_rating, "total_reviews": total_reviews}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_functions.execute_python:6': ['businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65'], 'var_functions.query_db:8': [{'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_52', 'rating': '2'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '5'}]}

exec(code, env_args)
