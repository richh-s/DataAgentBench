code = """import pandas as pd
import json
# Data from previous queries
df_business = pd.DataFrame(var_call_4t15oCo7hdEf1HrdBxrgHq9M)
df_reviews = pd.DataFrame(var_call_nsaut2pvy8dDDjmL8Bw3S7kP)
# Convert types
if not df_reviews.empty:
    df_reviews['avg_rating'] = df_reviews['avg_rating'].astype(float)
    df_reviews['num_reviews'] = df_reviews['num_reviews'].astype(int)
# Merge on gmap_id
df_merged = pd.merge(df_reviews, df_business[['gmap_id', 'name', 'description']], on='gmap_id', how='left')
# Sort by avg_rating desc, then num_reviews desc
df_merged = df_merged.sort_values(by=['avg_rating', 'num_reviews'], ascending=[False, False])
# Take top 5
top5 = df_merged.head(5)
# Prepare records
records = []
for _, row in top5.iterrows():
    records.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'average_rating': round(float(row['avg_rating']), 3),
        'num_reviews': int(row['num_reviews']),
        'description': row.get('description', None)
    })
result_json = json.dumps(records)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_4t15oCo7hdEf1HrdBxrgHq9M': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_nsaut2pvy8dDDjmL8Bw3S7kP': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}]}

exec(code, env_args)
