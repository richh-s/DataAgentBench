code = """import json
business_rows = var_call_4qfnsM2o6phCglHtSCKLdcCM
review_rows = var_call_BV2V00kpUF4BhYM7ad23FxGM
biz_map = {r['gmap_id']: r for r in business_rows}
merged = []
for r in review_rows:
    gid = r['gmap_id']
    if gid in biz_map:
        try:
            avg = float(r['avg_rating'])
        except:
            avg = None
        try:
            cnt = int(r['review_count'])
        except:
            cnt = None
        merged.append({
            'gmap_id': gid,
            'name': biz_map[gid].get('name'),
            'description': biz_map[gid].get('description'),
            'avg_rating': avg,
            'review_count': cnt
        })

# sort
merged_sorted = sorted(merged, key=lambda x: (-(x['avg_rating'] if x['avg_rating'] is not None else -9999), -(x['review_count'] if x['review_count'] is not None else -9999)))

# top5
top5 = merged_sorted[:5]
lines = []
lines.append('Top 5 businesses in Los Angeles, CA by average rating (highest to lowest):')
for i, b in enumerate(top5, start=1):
    if b['avg_rating'] is None:
        avg_str = 'N/A'
    else:
        avg_str = str(round(b['avg_rating'], 3))
    rc = b['review_count'] if b['review_count'] is not None else 'N/A'
    desc = b['description'].strip() if b.get('description') else ''
    line = str(i) + '. ' + str(b['name']) + ' (' + str(b['gmap_id']) + ') - Average rating: ' + avg_str + ' (' + str(rc) + ' reviews) - ' + desc
    lines.append(line)

result_text = '\n'.join(lines)
print('__RESULT__:')
print(json.dumps(result_text))"""

env_args = {'var_call_eg2Uks9Q8RX21LVwTXzx3t6q': ['review'], 'var_call_r2nWFbRvdEzSzieIWxsee6bY': ['business_description'], 'var_call_4qfnsM2o6phCglHtSCKLdcCM': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_BV2V00kpUF4BhYM7ad23FxGM': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
