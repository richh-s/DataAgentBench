code = """import pandas as pd
import json

df_b = pd.DataFrame(var_call_oN5UU4kEDx9IzdquHnFSNpAQ)
df_r = pd.DataFrame(var_call_Jq0MItDLQDroLNiu0z77VMhZ)

# Convert numeric fields
if 'num_of_reviews' in df_b.columns:
    df_b['num_of_reviews'] = pd.to_numeric(df_b['num_of_reviews'], errors='coerce').fillna(0).astype(int)
if 'avg_rating' in df_r.columns:
    df_r['avg_rating'] = pd.to_numeric(df_r['avg_rating'], errors='coerce')
if 'review_count' in df_r.columns:
    df_r['review_count'] = pd.to_numeric(df_r['review_count'], errors='coerce').fillna(0).astype(int)

# Merge
df = pd.merge(df_b, df_r, on='gmap_id', how='inner')

# Sort by avg_rating desc, then review_count desc
df_sorted = df.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

# Select top 5
top5 = df_sorted.head(5)

result = []
for _, row in top5.iterrows():
    result.append({
        'gmap_id': row['gmap_id'],
        'name': row.get('name', None),
        'description': row.get('description', None),
        'num_of_reviews': int(row['num_of_reviews']) if not pd.isna(row['num_of_reviews']) else None,
        'avg_rating': float(round(row['avg_rating'], 6)) if not pd.isna(row['avg_rating']) else None,
        'review_count': int(row['review_count']) if not pd.isna(row['review_count']) else None
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oN5UU4kEDx9IzdquHnFSNpAQ': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}], 'var_call_Jq0MItDLQDroLNiu0z77VMhZ': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}]}

exec(code, env_args)
