code = """import json
# Access previous query results stored in variables
business_records = var_call_okOsVoJwu9Z4d4vTbUGvCi6J
review_stats = var_call_Qqh6DwReSfxXPZLoekAvXiMi

# Build mapping from gmap_id to business info
biz_map = {b['gmap_id']: {'name': b.get('name'), 'description': b.get('description')} for b in business_records}

# Merge review stats with business info
merged = []
for r in review_stats:
    gid = r['gmap_id']
    try:
        avg = float(r['avg_rating'])
    except:
        avg = None
    try:
        nr = int(r['num_reviews'])
    except:
        nr = None
    biz = biz_map.get(gid, {})
    merged.append({
        'gmap_id': gid,
        'name': biz.get('name'),
        'description': biz.get('description'),
        'avg_rating': avg,
        'num_reviews': nr
    })

# Ensure sorted by avg_rating desc, then num_reviews desc
merged_sorted = sorted(merged, key=lambda x: ((-x['avg_rating']) if x['avg_rating'] is not None else 0, -(x['num_reviews'] or 0)))

# Take top 5
top5 = merged_sorted[:5]

# Prepare JSON-serializable string
result_str = json.dumps(top5, ensure_ascii=False)

print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_okOsVoJwu9Z4d4vTbUGvCi6J': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_Qqh6DwReSfxXPZLoekAvXiMi': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}]}

exec(code, env_args)
