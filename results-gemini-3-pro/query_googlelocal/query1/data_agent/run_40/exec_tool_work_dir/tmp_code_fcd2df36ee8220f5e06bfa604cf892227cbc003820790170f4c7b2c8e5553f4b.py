code = """import json

businesses = locals()['var_function-call-4614853989014513015']
ratings = locals()['var_function-call-1032746523254724806']

# Convert ratings list to dict for easier lookup
rating_map = {item['gmap_id']: float(item['avg_rating']) for item in ratings}

joined_data = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_map:
        joined_data.append({
            'name': b['name'],
            'avg_rating': rating_map[gid],
            'gmap_id': gid
        })

# Sort by avg_rating descending
sorted_data = sorted(joined_data, key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = sorted_data[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-7493376285719765559': ['business_description'], 'var_function-call-7493376285719767374': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-4614853989014513015': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-1032746523254724806': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
