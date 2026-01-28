code = """import json
# Access previous query results
reviews = var_call_yQHTfslW1yOm02oirNUsUi84
businesses = var_call_Hi85VBhEXtEAzQj3MCrxagLG
# Build business lookup
biz_lookup = {b['gmap_id']: b for b in businesses}
# Prepare combined records
combined = []
for r in reviews:
    gid = r['gmap_id']
    avg = float(r['avg_rating'])
    cnt = int(r['review_count'])
    biz = biz_lookup.get(gid, {})
    combined.append({
        'name': biz.get('name'),
        'gmap_id': gid,
        'avg_rating': round(avg, 3),
        'review_count': cnt,
        'description': biz.get('description')
    })
# Sort by avg_rating desc, then review_count desc
combined_sorted = sorted(combined, key=lambda x: (-x['avg_rating'], -x['review_count']))
# Take top 5
top5 = combined_sorted[:5]
# Print result following required format
print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_Hi85VBhEXtEAzQj3MCrxagLG': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_yQHTfslW1yOm02oirNUsUi84': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
