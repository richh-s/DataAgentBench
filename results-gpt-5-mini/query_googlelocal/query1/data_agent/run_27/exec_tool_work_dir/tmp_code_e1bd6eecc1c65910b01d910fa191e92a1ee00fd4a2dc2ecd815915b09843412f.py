code = """import pandas as pd
import json

# Load previous query results from storage variables
biz_records = var_call_LRl6e4xP7388s2kY5lVRmqJI
rev_records = var_call_LKOEMbCZqxN1hh9JNjWtvdvk

# Create DataFrames
biz = pd.DataFrame(biz_records)
rev = pd.DataFrame(rev_records)

# Normalize and filter businesses located in Los Angeles
biz['description'] = biz['description'].astype(str)
biz_la = biz[biz['description'].str.lower().str.contains('los angeles')].copy()

# Merge with review averages
df = pd.merge(biz_la, rev, on='gmap_id', how='inner')

# Convert numeric fields
df['avg_rating'] = df['avg_rating'].astype(float)
# ensure review counts numeric
try:
    df['review_count'] = df['review_count'].astype(int)
except:
    df['review_count'] = df['review_count'].apply(lambda x: int(x) if str(x).isdigit() else 0)

# Sort by average rating descending, then by review_count descending
df_sorted = df.sort_values(['avg_rating', 'review_count'], ascending=[False, False])

# Take top 5
top5 = df_sorted.head(5)

# Prepare results
result = []
rank = 1
for _, row in top5.iterrows():
    # attempt to convert num_of_reviews to int when possible
    num_reviews = row.get('num_of_reviews', None)
    try:
        num_reviews_conv = int(num_reviews)
    except:
        num_reviews_conv = num_reviews

    result.append({
        'rank': rank,
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': round(float(row['avg_rating']), 6),
        'num_of_reviews': num_reviews_conv,
        'review_count_in_reviews_table': int(row['review_count'])
    })
    rank += 1

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Orgx8tsDyaZnZmyvRTivILig': ['business_description'], 'var_call_SR2pFNzlGWyIVOv165UWib2v': ['review'], 'var_call_LRl6e4xP7388s2kY5lVRmqJI': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.', 'num_of_reviews': '18'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51', 'description': 'Longtime boutique featuring high-quality Persian & Oriental rugs, plus repair & cleaning services. Discover a curated selection of exquisite floor coverings and textiles that enhance any space, conveniently located in La Jolla, CA 92037.', 'num_of_reviews': '18'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}], 'var_call_LKOEMbCZqxN1hh9JNjWtvdvk': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'review_count': '18'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'review_count': '18'}]}

exec(code, env_args)
