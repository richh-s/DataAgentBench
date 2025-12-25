code = """import json
import pandas as pd

# Load data
data = locals()['var_function-call-1470036366095591578']
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        reviews = json.load(f)
else:
    reviews = data

# Create DataFrame
df = pd.DataFrame(reviews)
df['rating'] = df['rating'].astype(float)

# Method 1: Average of business averages (Macro)
# Group by business_ref and calculate mean rating for each business
business_avg = df.groupby('business_ref')['rating'].mean()
final_avg_macro = business_avg.mean()

# Method 2: Average of all reviews (Micro)
final_avg_micro = df['rating'].mean()

print(f"Business Averages:\n{business_avg}")
print(f"Macro Average: {final_avg_macro}")
print(f"Micro Average: {final_avg_micro}")

# I will return the Macro Average as it fits "average rating of businesses" better.
# But usually questions like this in SQL context might just want AVG(rating). 
# However, "average rating of businesses" strongly implies the unit is the business.

print("__RESULT__:")
print(json.dumps(final_avg_macro))"""

env_args = {'var_function-call-12754685981999529559': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_function-call-15429731181335069133': "('businessref_52', 'businessref_84', 'businessref_76', 'businessref_87', 'businessref_65')", 'var_function-call-1470036366095591578': [{'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_52', 'rating': '2'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '3'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_87', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '1'}, {'business_ref': 'businessref_52', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '3'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_87', 'rating': '5'}, {'business_ref': 'businessref_52', 'rating': '5'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_84', 'rating': '5'}, {'business_ref': 'businessref_65', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '4'}, {'business_ref': 'businessref_76', 'rating': '5'}]}

exec(code, env_args)
