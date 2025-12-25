code = """import json
import pandas as pd

# Load Mongo result (list of businesses)
businesses = locals()['var_function-call-8311609942689815108']
# businesses is a list of dicts: [{'business_id': 'businessid_52', ...}, ...]

# Load SQL result (list of reviews) - from file
file_path = locals()['var_function-call-12726174086641226747']
with open(file_path, 'r') as f:
    reviews = json.load(f)

# Extract business_ids and convert to business_ref format
# Mongo ID: businessid_52 -> DuckDB Ref: businessref_52
target_business_refs = set()
for b in businesses:
    bid = b['business_id']
    # Replace prefix
    if bid.startswith('businessid_'):
        ref = 'businessref_' + bid[len('businessid_'):]
        target_business_refs.add(ref)

# Filter reviews
filtered_ratings = []
for r in reviews:
    if r['business_ref'] in target_business_refs:
        filtered_ratings.append(r['rating'])

# Calculate average
if not filtered_ratings:
    avg_rating = 0.0
else:
    # ratings might be strings or ints. The preview showed "rating": "2", so likely strings.
    # Convert to float/int
    ratings_numeric = [float(x) for x in filtered_ratings]
    avg_rating = sum(ratings_numeric) / len(ratings_numeric)

print("__RESULT__:")
print(json.dumps(avg_rating))"""

env_args = {'var_function-call-14512234543992835438': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_function-call-9481710469065113594': [{'business_ref': 'businessref_34', 'rating': '2'}, {'business_ref': 'businessref_89', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}, {'business_ref': 'businessref_66', 'rating': '2'}, {'business_ref': 'businessref_95', 'rating': '1'}], 'var_function-call-8311609942689815108': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16'}], 'var_function-call-12726174086641226747': 'file_storage/function-call-12726174086641226747.json'}

exec(code, env_args)
