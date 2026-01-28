code = """import pandas as pd
import json
# Load data from previous tool results
df_b = pd.DataFrame(var_call_kydIYj1zoGexlaozJz4Dmvyp)
df_r = pd.DataFrame(var_call_K1tQ3qMjUJ70NoN4XyFnqAuP)
# Convert rating to numeric
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
# Aggregate
agg = df_r.groupby('gmap_id').rating.agg(['mean','count']).reset_index()
# Merge with business info
merged = pd.merge(df_b, agg, on='gmap_id', how='left')
# Fill NaN mean with None
merged['mean'] = merged['mean'].round(2)
merged['count'] = merged['count'].fillna(0).astype(int)
# Sort by mean desc then count desc
merged_sorted = merged.sort_values(by=['mean','count'], ascending=[False, False])
# Select top 5
top5 = merged_sorted.head(5)
# Prepare output
out = []
for _, row in top5.iterrows():
    out.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'average_rating': None if pd.isna(row['mean']) else float(row['mean']),
        'review_count': int(row['count']),
        'description': row['description'].strip() if isinstance(row['description'], str) else row['description']
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_kydIYj1zoGexlaozJz4Dmvyp': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_K1tQ3qMjUJ70NoN4XyFnqAuP': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '3'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}]}

exec(code, env_args)
