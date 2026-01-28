code = """import json
# Accessing previous query results from storage
b = var_call_aKaUcxAWGAOt9L4D5iD4VFsG
r = var_call_yHUr3KE4FLYzRuQcl4VUmcWw
# Map businesses by gmap_id
bus_map = {item['gmap_id']: item for item in b}
combined = []
for rec in r:
    gid = rec['gmap_id']
    name = bus_map.get(gid, {}).get('name')
    desc = bus_map.get(gid, {}).get('description')
    try:
        avg = float(rec.get('avg_rating'))
    except:
        avg = None
    try:
        cnt = int(rec.get('review_count'))
    except:
        cnt = None
    combined.append({'name': name, 'gmap_id': gid, 'description': desc, 'avg_rating': avg, 'review_count': cnt})
# Sort by avg_rating desc, then review_count desc
combined_sorted = sorted(combined, key=lambda x: ((-x['avg_rating']) if x['avg_rating'] is not None else 0, -(x['review_count'] or 0)))
top5 = combined_sorted[:5]
# Round avg_rating for presentation
for it in top5:
    if it['avg_rating'] is not None:
        it['avg_rating'] = round(it['avg_rating'], 3)
# Print result in required format
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_VMyddhy84WVSWfOEd1aCZ3ka': 'file_storage/call_VMyddhy84WVSWfOEd1aCZ3ka.json', 'var_call_aKaUcxAWGAOt9L4D5iD4VFsG': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_yHUr3KE4FLYzRuQcl4VUmcWw': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
