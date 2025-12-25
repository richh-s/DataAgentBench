code = """businesses = locals()['var_function-call-3834548385751235976']
ratings = locals()['var_function-call-14818806228320043565']

# Convert ratings to a dict for easier lookup
rating_dict = {item['gmap_id']: float(item['avg_rating']) for item in ratings}

# Merge
merged_list = []
for bus in businesses:
    gmap_id = bus['gmap_id']
    name = bus['name']
    avg_rating = rating_dict.get(gmap_id, 0.0) # Default to 0 if no reviews found (though query suggests all had reviews)
    merged_list.append({'name': name, 'avg_rating': avg_rating})

# Sort
sorted_businesses = sorted(merged_list, key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = sorted_businesses[:5]

print("__RESULT__:")
import json
print(json.dumps(top_5))"""

env_args = {'var_function-call-4782269035179926205': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-14504583307197578290': [{'count': '7'}], 'var_function-call-3834548385751235976': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-14818806228320043565': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}]}

exec(code, env_args)
