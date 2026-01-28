code = """import json
import numpy as np

# Get the ratings from the query result
ratings_data = [{"rating": "3"}, {"rating": "5"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "4"}, {"rating": "3"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "3"}, {"rating": "2"}, {"rating": "4"}, {"rating": "5"}, {"rating": "3"}, {"rating": "3"}, {"rating": "5"}, {"rating": "1"}, {"rating": "3"}, {"rating": "1"}, {"rating": "4"}, {"rating": "3"}, {"rating": "4"}, {"rating": "4"}, {"rating": "1"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "3"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}, {"rating": "5"}, {"rating": "4"}, {"rating": "5"}, {"rating": "4"}, {"rating": "4"}, {"rating": "5"}]

# Extract ratings and convert to integers
ratings = [int(item["rating"]) for item in ratings_data]

# Calculate average
average_rating = np.mean(ratings)

# Print result in required format
result = {
    "average_rating": round(average_rating, 2),
    "total_reviews": len(ratings)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_functions.query_db:5': [{'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '1'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}]}

exec(code, env_args)
