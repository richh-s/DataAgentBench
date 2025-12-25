code = """import json
la_businesses = locals()['var_function-call-17565305056253761424']
top_ratings = locals()['var_function-call-12979275852293364160']

# Create a lookup for names
name_lookup = {b['gmap_id']: b['name'] for b in la_businesses}

result_list = []
for r in top_ratings:
    gmap_id = r['gmap_id']
    name = name_lookup.get(gmap_id, "Unknown")
    rating = r['avg_rating']
    result_list.append({"name": name, "rating": rating})

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-7933422113418436164': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-17565305056253761424': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-12979275852293364160': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}]}

exec(code, env_args)
