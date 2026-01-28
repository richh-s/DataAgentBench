code = """import json
import pandas as pd

# Load results from previous tool calls
business_records = var_call_bbe5l2ZuV5q7PimmxVZjyZmZ
review_stats = var_call_56Z2fh3y5ykPbLrnxJRj6GGu

# Create DataFrames
df_business = pd.DataFrame(business_records)
df_reviews = pd.DataFrame(review_stats)

# Convert numeric fields
if not df_reviews.empty:
    df_reviews['avg_rating'] = pd.to_numeric(df_reviews['avg_rating'], errors='coerce')
    df_reviews['review_count'] = pd.to_numeric(df_reviews['review_count'], errors='coerce').fillna(0).astype(int)

# Merge and sort
merged = pd.merge(df_business, df_reviews, on='gmap_id', how='inner')
merged_sorted = merged.sort_values(by='avg_rating', ascending=False).head(5)

# Build output list
output = []
for idx, row in merged_sorted.reset_index(drop=True).iterrows():
    output.append({
        'rank': int(idx) + 1,
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 3) if pd.notnull(row['avg_rating']) else None,
        'review_count': int(row['review_count']) if 'review_count' in row and pd.notnull(row['review_count']) else None,
        'description': row.get('description', '')
    })

result = json.dumps(output)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_bbe5l2ZuV5q7PimmxVZjyZmZ': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_56Z2fh3y5ykPbLrnxJRj6GGu': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
