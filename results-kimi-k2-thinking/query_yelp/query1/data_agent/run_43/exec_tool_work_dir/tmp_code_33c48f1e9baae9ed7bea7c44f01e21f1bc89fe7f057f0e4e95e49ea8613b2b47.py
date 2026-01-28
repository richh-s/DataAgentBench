code = """import json
import pandas as pd

# Get the business results
business_results = locals()['var_functions.query_db:2']

# Create DataFrame from results
business_df = pd.DataFrame(business_results)

# Extract business IDs and convert to business_ref format
business_ids = business_df['business_id'].tolist()
business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids]

# Get ratings results
ratings_results = locals()['var_functions.query_db:4']

# Create DataFrame from ratings
ratings_df = pd.DataFrame(ratings_results)

# Convert rating to numeric
ratings_df['rating'] = pd.to_numeric(ratings_df['rating'])

# Calculate average rating
average_rating = ratings_df['rating'].mean()
count = len(ratings_df)

# Print result
result = {
    "average_rating": float(average_rating),
    "total_reviews": int(count),
    "businesses_found": len(business_refs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'name': 'Gamestop', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'name': 'Big Lots', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'name': "Pat Flynn's Public House", 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94', 'name': 'Taste of Europe', 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90', 'name': "Long John Silver's", 'description': 'Located at 2831 E 38th St in Indianapolis, IN, this establishment offers a diverse menu featuring Fast Food, Seafood, Restaurants, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16', 'name': 'Fox and Hound English Pub and Grille', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}], 'var_functions.query_db:4': [{'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '5'}, {'rating': '1'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '2'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '1'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '1'}, {'rating': '5'}, {'rating': '3'}, {'rating': '3'}, {'rating': '1'}, {'rating': '1'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '1'}, {'rating': '2'}, {'rating': '3'}, {'rating': '4'}, {'rating': '4'}, {'rating': '2'}, {'rating': '1'}, {'rating': '1'}, {'rating': '1'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '5'}, {'rating': '3'}, {'rating': '5'}, {'rating': '3'}, {'rating': '5'}, {'rating': '5'}, {'rating': '4'}, {'rating': '3'}, {'rating': '2'}, {'rating': '2'}, {'rating': '1'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '4'}, {'rating': '4'}, {'rating': '2'}, {'rating': '4'}, {'rating': '1'}, {'rating': '4'}, {'rating': '5'}, {'rating': '4'}, {'rating': '1'}, {'rating': '2'}, {'rating': '4'}]}

exec(code, env_args)
