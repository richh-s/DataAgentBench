code = """import pandas as pd
import json
# Data from previous queries
# var_call_M1DiQ7YbPBNWJqFMk62yoDTX and var_call_WQttozOlLgfpnrZK92ZB37k2 are available
df_bus = pd.DataFrame(var_call_M1DiQ7YbPBNWJqFMk62yoDTX)
df_rev = pd.DataFrame(var_call_WQttozOlLgfpnrZK92ZB37k2)
# Convert numeric fields
for col in ['num_of_reviews']:
    if col in df_bus.columns:
        df_bus[col] = pd.to_numeric(df_bus[col], errors='coerce').fillna(0).astype(int)
for col in ['avg_rating','review_count']:
    if col in df_rev.columns:
        df_rev[col] = pd.to_numeric(df_rev[col], errors='coerce')
        if col=='review_count':
            df_rev[col] = df_rev[col].fillna(0).astype(int)
# Merge
df = pd.merge(df_bus, df_rev, on='gmap_id', how='inner')
# Sort by avg_rating desc
df_sorted = df.sort_values(by='avg_rating', ascending=False)
# Take top 5
top5 = df_sorted.head(5)
# Prepare output
result = []
for _, row in top5.iterrows():
    result.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'description': row.get('description', None),
        'num_of_reviews': int(row.get('num_of_reviews', 0)),
        'avg_rating': float(row.get('avg_rating')) if pd.notnull(row.get('avg_rating')) else None,
        'review_count': int(row.get('review_count', 0))
    })

result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_M1DiQ7YbPBNWJqFMk62yoDTX': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}], 'var_call_WQttozOlLgfpnrZK92ZB37k2': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
