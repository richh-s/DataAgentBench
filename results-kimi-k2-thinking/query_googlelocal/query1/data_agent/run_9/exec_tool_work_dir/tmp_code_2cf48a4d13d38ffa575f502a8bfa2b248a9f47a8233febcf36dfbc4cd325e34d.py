code = """import json
import pandas as pd

# Load Los Angeles businesses
la_businesses = locals()['var_functions.query_db:6']
la_gmap_ids = [b['gmap_id'] for b in la_businesses]

# Load reviews from file
reviews_file = locals()['var_functions.query_db:5']
with open(reviews_file, 'r') as f:
    all_reviews = json.load(f)

# Filter reviews for LA businesses
la_reviews = [r for r in all_reviews if r['gmap_id'] in la_gmap_ids]

# Convert to DataFrame for analysis
reviews_df = pd.DataFrame(la_reviews)
reviews_df['rating'] = reviews_df['rating'].astype(int)

# Calculate average rating per business
avg_ratings = reviews_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

# Merge with business info
business_df = pd.DataFrame(la_businesses)
result = pd.merge(business_df, avg_ratings, on='gmap_id')

# Sort by average rating descending and get top 5
top_5 = result.sort_values('avg_rating', ascending=False).head(5)

# Prepare output
output = []
for _, row in top_5.iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(row['avg_rating'], 2),
        'review_count': int(row['review_count']),
        'description': row['description']
    })

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
