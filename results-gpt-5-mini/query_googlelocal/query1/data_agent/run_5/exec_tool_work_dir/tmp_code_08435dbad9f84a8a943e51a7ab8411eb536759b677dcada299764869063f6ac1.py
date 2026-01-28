code = """import json
# Accessing stored query results
business_rows = var_call_eaXowRtAIsqjGWc2oySCjk3O
rating_rows = var_call_tRDlvq6TYX91PozA6HmtJAp8

# Build business map
biz_map = {r['gmap_id']: r for r in business_rows}

# Combine records
combined = []
for r in rating_rows:
    gid = r.get('gmap_id')
    biz = biz_map.get(gid, {})
    try:
        avg = float(r.get('avg_rating')) if r.get('avg_rating') is not None else None
    except:
        avg = None
    try:
        rc = int(r.get('review_count')) if r.get('review_count') is not None else None
    except:
        rc = None
    # num_of_reviews may be string in business DB
    no_rev = biz.get('num_of_reviews')
    try:
        no_rev = int(no_rev) if no_rev is not None else None
    except:
        no_rev = None
    combined.append({
        'name': biz.get('name'),
        'gmap_id': gid,
        'description': biz.get('description'),
        'num_of_reviews': no_rev,
        'avg_rating': avg,
        'review_count': rc
    })

# Sort by avg_rating desc
combined_sorted = sorted(combined, key=lambda x: (-(x['avg_rating'] if x['avg_rating'] is not None else -999), -(x['review_count'] if x['review_count'] is not None else 0)))

# Top 5
top5 = combined_sorted[:5]

# Ensure JSON serializable (already is)
output = top5

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_d0T8LYht5mW4kN9VWIYAz3vz': ['review'], 'var_call_lGmfVRB6V2kCV53lFVUcioQn': ['business_description'], 'var_call_eaXowRtAIsqjGWc2oySCjk3O': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35'}], 'var_call_tRDlvq6TYX91PozA6HmtJAp8': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
