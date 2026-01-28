code = """import json
# access the results from previous query_db calls
business_rows = var_call_8Zh77tBm7Qt8Xe4AmTC8AtFa
review_rows = var_call_CpHGFHyrxMqxZmgwSAa9jlDx
# index business by gmap_id
biz_by_id = {r['gmap_id']: r for r in business_rows}
# merge
merged = []
for r in review_rows:
    gid = r['gmap_id']
    biz = biz_by_id.get(gid, {})
    try:
        avg = float(r.get('avg_rating'))
    except:
        avg = None
    try:
        rc = int(r.get('review_count'))
    except:
        rc = None
    try:
        num_reviews = int(biz.get('num_of_reviews')) if biz.get('num_of_reviews') is not None else None
    except:
        num_reviews = None
    merged.append({
        'gmap_id': gid,
        'name': biz.get('name'),
        'description': biz.get('description'),
        'avg_rating': avg,
        'review_count': rc,
        'num_of_reviews': num_reviews
    })
# sort by avg_rating desc, then review_count desc
merged_sorted = sorted(merged, key=lambda x: ((-x['avg_rating']) if x['avg_rating'] is not None else 0, -(x['review_count'] or 0)))
# top 5
top5 = merged_sorted[:5]
# prepare JSON string
out = json.dumps(top5, ensure_ascii=False)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8Zh77tBm7Qt8Xe4AmTC8AtFa': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}], 'var_call_CpHGFHyrxMqxZmgwSAa9jlDx': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}]}

exec(code, env_args)
