code = """import json
import pandas as pd

# Load query results from storage variables
bus = pd.DataFrame(var_call_7m4vD756nelC25wDaR5XABuF)
rev = pd.DataFrame(var_call_yVXWO6qd13ifeueKzx9KABcH)

if not rev.empty:
    rev['avg_rating'] = rev['avg_rating'].astype(float)
    rev['review_count'] = rev['review_count'].astype(int)

merged = rev.merge(bus, on='gmap_id', how='left')
merged = merged.sort_values(['avg_rating','review_count'], ascending=[False, False])

top5 = merged.head(5).to_dict(orient='records')

out = []
lines = []
rank = 1
for r in top5:
    name = r.get('name')
    gid = r.get('gmap_id')
    avg = round(r.get('avg_rating'), 3) if r.get('avg_rating') is not None else None
    rc = r.get('review_count')
    desc = r.get('description')
    out.append({'rank': rank, 'gmap_id': gid, 'name': name, 'avg_rating': avg, 'review_count': rc, 'description': desc})
    lines.append(str(rank) + '. ' + str(name) + ' - ' + str(avg) + ' (based on ' + str(rc) + ' reviews) - gmap_id: ' + str(gid))
    rank += 1

plain = chr(10).join(lines)
res = {'plain_text': plain, 'structured': out}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_7m4vD756nelC25wDaR5XABuF': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_yVXWO6qd13ifeueKzx9KABcH': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
