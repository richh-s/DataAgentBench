code = """import json

businesses = locals()['var_function-call-7636677952850686977']
ratings = locals()['var_function-call-4350825812881269043']

# Create a dict for ratings
rating_map = {item['gmap_id']: item['avg_rating'] for item in ratings}

# Merge
result_list = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_map:
        result_list.append({
            "name": b['name'],
            "avg_rating": float(rating_map[gid])
        })

# Sort by avg_rating descending
result_list.sort(key=lambda x: x['avg_rating'], reverse=True)

# Take top 5
top_5 = result_list[:5]

# Format just the names as per query "What are the top 5 businesses..." usually implies names.
# But providing names and ratings is clearer. The examples output JSON. 
# I will output the list of names.

top_5_names = [x['name'] for x in top_5]

print("__RESULT__:")
print(json.dumps(top_5_names))"""

env_args = {'var_function-call-12486049114034286734': ['business_description'], 'var_function-call-10578564631471440736': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-12436368601455090090': [{'count': '7'}], 'var_function-call-7636677952850686977': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_function-call-4350825812881269043': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}]}

exec(code, env_args)
