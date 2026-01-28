code = """import pandas as pd
import json
# Load data from previous query results
biz = pd.DataFrame(var_call_ZRDH4lOERoUzl5n06Q5lMGKB)
rev = pd.DataFrame(var_call_rjgfmLWw2up7LtaeAyKZnVaK)
# Convert numeric fields
rev['avg_rating'] = pd.to_numeric(rev['avg_rating'], errors='coerce')
rev['num_reviews'] = pd.to_numeric(rev['num_reviews'], errors='coerce').fillna(0).astype(int)
# Merge business info with review aggregates
merged = pd.merge(rev, biz, on='gmap_id', how='left')
# Sort by avg_rating desc, then num_reviews desc
merged_sorted = merged.sort_values(by=['avg_rating', 'num_reviews'], ascending=[False, False]).head(5)
# Prepare result list
result = []
for idx, row in merged_sorted.reset_index(drop=True).iterrows():
    result.append({
        'rank': int(idx+1),
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'avg_rating': float(round(row['avg_rating'], 6)) if pd.notna(row['avg_rating']) else None,
        'num_reviews': int(row['num_reviews'])
    })
# Print in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZRDH4lOERoUzl5n06Q5lMGKB': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_rjgfmLWw2up7LtaeAyKZnVaK': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}]}

exec(code, env_args)
