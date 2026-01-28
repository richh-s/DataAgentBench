code = """import pandas as pd
import json

# Load results from previous tool calls (available in storage variables)
business = pd.DataFrame(var_call_aUYz7pxurqT9tEVK0vTBNmZX)
reviews = pd.DataFrame(var_call_K4nf9oi2QUsaEkTCeW8N2OZf)

# Convert types
reviews['avg_rating'] = reviews['avg_rating'].astype(float)
reviews['review_count'] = reviews['review_count'].astype(int)

# Merge on gmap_id
merged = reviews.merge(business, on='gmap_id', how='left')

# Sort by avg_rating desc, then review_count desc
merged_sorted = merged.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

# Select top 5
top5 = merged_sorted.head(5)

# Prepare output list
output = []
for _, row in top5.iterrows():
    output.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 3),
        'review_count': int(row['review_count']),
        'description': row.get('description', None)
    })

result_json = json.dumps(output)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_aUYz7pxurqT9tEVK0vTBNmZX': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_K4nf9oi2QUsaEkTCeW8N2OZf': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}]}

exec(code, env_args)
