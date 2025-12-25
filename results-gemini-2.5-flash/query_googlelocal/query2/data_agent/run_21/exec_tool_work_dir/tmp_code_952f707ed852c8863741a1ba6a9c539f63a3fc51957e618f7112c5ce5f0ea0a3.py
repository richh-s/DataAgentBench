code = """import pandas as pd
import json

# Load the massage business gmap_ids from the previous step
massage_gmap_ids = locals()['var_function-call-2542138238953869688']

# Load the full review data from the stored JSON file
with open(locals()['var_function-call-16049751316104457870'], 'r') as f:
    review_data = json.load(f)

review_df = pd.DataFrame(review_data)

# Convert 'rating' to numeric, handling potential errors and coercing to NaN
review_df['rating'] = pd.to_numeric(review_df['rating'], errors='coerce')

# Filter out NaN ratings if any
review_df = review_df.dropna(subset=['rating'])

# Filter reviews for massage therapy businesses
massage_reviews_df = review_df[review_df['gmap_id'].isin(massage_gmap_ids)]

# Calculate the average rating for each massage business
average_ratings_df = massage_reviews_df.groupby('gmap_id')['rating'].mean().reset_index()

# Filter for businesses with an average rating of at least 4.0
high_rated_massage_businesses = average_ratings_df[average_ratings_df['rating'] >= 4.0]

# Load the full business data again to get the names
with open(locals()['var_function-call-2056214235904761986'], 'r') as f:
    business_data = json.load(f)
business_df = pd.DataFrame(business_data)

# Merge with business data to get business names
final_result_df = pd.merge(high_rated_massage_businesses, business_df[['gmap_id', 'name']], on='gmap_id')

# Format the output as a list of dictionaries with business name and average rating
output = final_result_df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_function-call-18320300112929708067': ['business_description'], 'var_function-call-18308021375892395550': [], 'var_function-call-14762917165535927528': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'name': 'City Textile'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'name': 'San Soo Dang'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'name': 'Nova Fabrics'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'name': 'Nobel Textile Co'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'name': 'Matrix International Textiles'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.', 'name': 'Vons Chicken'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'name': 'Angel-A Massage'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.', 'name': 'Dunn-Edwards Paints'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'name': 'Elite Massage'}], 'var_function-call-12322790892699588211': [], 'var_function-call-2056214235904761986': 'file_storage/function-call-2056214235904761986.json', 'var_function-call-2542138238953869688': ['gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21'], 'var_function-call-16049751316104457870': 'file_storage/function-call-16049751316104457870.json'}

exec(code, env_args)
