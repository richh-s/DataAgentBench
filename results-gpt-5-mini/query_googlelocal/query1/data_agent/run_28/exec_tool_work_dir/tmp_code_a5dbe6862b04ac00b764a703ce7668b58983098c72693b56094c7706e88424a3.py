code = """import pandas as pd
import json
biz = pd.DataFrame(var_call_PQ3I0W9gtnkKxsFU78gcFGdD)
ratings = pd.DataFrame(var_call_GZ1eu7NamBKvaW3a0hIk6OUf)
ratings['avg_rating'] = ratings['avg_rating'].astype(float)
ratings['num_reviews'] = ratings['num_reviews'].astype(int)
merged = pd.merge(biz, ratings, on='gmap_id', how='inner')
merged = merged.sort_values(['avg_rating', 'num_reviews'], ascending=[False, False]).head(5)
result = []
for idx, row in merged.reset_index(drop=True).iterrows():
    result.append({
        'rank': int(idx+1),
        'name': row['name'],
        'gmap_id': row['gmap_id'],
        'avg_rating': float(row['avg_rating']),
        'num_reviews': int(row['num_reviews']),
        'description': row['description']
    })
json_str = json.dumps(result)
print("__RESULT__:")
print(json_str)"""

env_args = {'var_call_mIu6rbUhw32xbtaqmEUo2Zek': ['business_description'], 'var_call_PQ3I0W9gtnkKxsFU78gcFGdD': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_GZ1eu7NamBKvaW3a0hIk6OUf': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}]}

exec(code, env_args)
