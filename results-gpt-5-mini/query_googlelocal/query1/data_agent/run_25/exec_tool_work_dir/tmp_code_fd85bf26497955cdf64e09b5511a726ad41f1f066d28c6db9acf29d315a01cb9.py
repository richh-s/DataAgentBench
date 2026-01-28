code = """import pandas as pd
import json
# data from previous queries
df_biz = pd.DataFrame(var_call_C1HnNFYql1rFd2SJpuYdtwud)
df_rev = pd.DataFrame(var_call_fEn6Rrqs4h2WepOr4CvuEBfV)
# convert types
if not df_rev.empty:
    df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)
    df_rev['review_count'] = df_rev['review_count'].astype(int)
# merge
df = pd.merge(df_biz, df_rev, on='gmap_id', how='inner')
# sort by avg_rating desc, then review_count desc
df = df.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])
# take top 5
top5 = df.head(5)
# prepare result list
result = []
for _, row in top5.iterrows():
    result.append({
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 6),
        'review_count': int(row['review_count']),
        'description': row.get('description', None)
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_C1HnNFYql1rFd2SJpuYdtwud': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_fEn6Rrqs4h2WepOr4CvuEBfV': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}]}

exec(code, env_args)
