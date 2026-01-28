code = """import json
# Access previous query results from storage variables
business_rows = var_call_LFH3WdEAwsio3amI8uFpctmd
rating_rows = var_call_okxIsN9IgpdxtYWfLMoJYMoD

# Build lookup
businesses = {item['gmap_id']: item for item in business_rows}
ratings = {r['gmap_id']: {'avg_rating': float(r['avg_rating']), 'review_count': int(r['review_count'])} for r in rating_rows}

# Merge
merged = []
for gid, b in businesses.items():
    if gid in ratings:
        merged.append({
            'gmap_id': gid,
            'name': b.get('name'),
            'description': b.get('description'),
            'avg_rating': ratings[gid]['avg_rating'],
            'review_count': ratings[gid]['review_count']
        })

# Sort by avg_rating desc, then by review_count desc, then name
merged_sorted = sorted(merged, key=lambda x: (-x['avg_rating'], -x['review_count'], x['name']))

top5 = merged_sorted[:5]

# Prepare JSON-serializable output
output = top5

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_LFH3WdEAwsio3amI8uFpctmd': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_call_okxIsN9IgpdxtYWfLMoJYMoD': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
