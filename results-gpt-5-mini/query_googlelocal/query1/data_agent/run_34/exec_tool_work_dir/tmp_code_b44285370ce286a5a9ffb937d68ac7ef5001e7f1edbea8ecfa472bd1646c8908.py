code = """import pandas as pd
import json

# Accessing stored results from previous tool calls
business_records = var_call_4gL2x0bCwj3yi7ZnSEIxT5c8
review_stats = var_call_R6dmKPt4QFwnfe5pTsdpjryy

# Create DataFrames
df_b = pd.DataFrame(business_records)
df_r = pd.DataFrame(review_stats)

# Convert numeric fields
df_r['avg_rating'] = df_r['avg_rating'].astype(float)
if 'review_count' in df_r.columns:
    df_r['review_count'] = df_r['review_count'].astype(int)
else:
    df_r['review_count'] = 0

# Merge on gmap_id
df = pd.merge(df_b, df_r, on='gmap_id', how='inner')

# Sort by average rating descending, then by review_count descending
df_sorted = df.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

# Take top 5
top5 = df_sorted.head(5)

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

result_str = json.dumps(output)
print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_4gL2x0bCwj3yi7ZnSEIxT5c8': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_R6dmKPt4QFwnfe5pTsdpjryy': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
