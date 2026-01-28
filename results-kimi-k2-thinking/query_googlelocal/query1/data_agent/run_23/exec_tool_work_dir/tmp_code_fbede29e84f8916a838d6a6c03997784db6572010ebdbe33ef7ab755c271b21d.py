code = """import json
import pandas as pd

# Load the review data
review_file = locals().get('var_functions.query_db:5')
if isinstance(review_file, str):
    with open(review_file, 'r') as f:
        reviews = json.load(f)
else:
    reviews = review_file

# Load the business data
business_file = locals().get('var_functions.query_db:8')
if isinstance(business_file, str):
    with open(business_file, 'r') as f:
        la_businesses = json.load(f)
else:
    la_businesses = business_file

# Create DataFrames
reviews_df = pd.DataFrame(reviews)
business_df = pd.DataFrame(la_businesses)

# Ensure rating is numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Get Los Angeles businesses from business_df (already filtered by query)
la_gmap_ids = business_df['gmap_id'].tolist()

# Filter reviews for LA businesses
la_reviews_df = reviews_df[reviews_df['gmap_id'].isin(la_gmap_ids)]

# Calculate average rating per business
avg_ratings = la_reviews_df.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating']

# Join with business info
result_df = business_df.merge(avg_ratings, on='gmap_id', how='inner')

# Convert num_of_reviews to numeric
result_df['num_of_reviews'] = pd.to_numeric(result_df['num_of_reviews'])

# Sort by avg_rating descending
result_df = result_df.sort_values('avg_rating', ascending=False)

# Get top 5
top_5 = result_df.head(5)

# Create output with business name, avg rating, and num of reviews
output = []
for _, row in top_5.iterrows():
    output.append({
        'name': row['name'],
        'average_rating': round(row['avg_rating'], 2),
        'num_of_reviews': row['num_of_reviews'],
        'description': row['description']
    })

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}]}

exec(code, env_args)
