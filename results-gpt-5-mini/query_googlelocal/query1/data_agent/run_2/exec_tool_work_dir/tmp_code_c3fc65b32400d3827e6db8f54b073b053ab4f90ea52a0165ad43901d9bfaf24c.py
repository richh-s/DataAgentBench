code = """import pandas as pd
import json

# Load data from previous query results
df_bus = pd.DataFrame(var_call_7m4vD756nelC25wDaR5XABuF)
df_rev = pd.DataFrame(var_call_yVXWO6qd13ifeueKzx9KABcH)

# Convert types
if not df_rev.empty:
    df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)
    df_rev['review_count'] = df_rev['review_count'].astype(int)

# Merge
merged = pd.merge(df_rev, df_bus, on='gmap_id', how='left')
merged = merged.sort_values(['avg_rating', 'review_count'], ascending=[False, False])

# Top 5
top5 = merged.head(5)

lines = []
structured = []
i = 1
for _, row in top5.iterrows():
    name = row.get('name', None)
    gid = row['gmap_id']
    avg = round(float(row['avg_rating']), 3) if pd.notna(row['avg_rating']) else None
    rc = int(row['review_count']) if pd.notna(row['review_count']) else None
    desc = row.get('description', None)
    lines.append(str(i) + '. ' + str(name) + ' — ' + str(avg) + ' (based on ' + str(rc) + ' reviews) - gmap_id: ' + str(gid))
    structured.append({'rank': i, 'gmap_id': gid, 'name': name if pd.notna(name) else None, 'avg_rating': avg, 'review_count': rc, 'description': desc if pd.notna(desc) else None})
    i += 1

final_text = '\n'.join(lines)
result_obj = {'plain_text': final_text, 'structured': structured}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_call_7m4vD756nelC25wDaR5XABuF': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_yVXWO6qd13ifeueKzx9KABcH': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
