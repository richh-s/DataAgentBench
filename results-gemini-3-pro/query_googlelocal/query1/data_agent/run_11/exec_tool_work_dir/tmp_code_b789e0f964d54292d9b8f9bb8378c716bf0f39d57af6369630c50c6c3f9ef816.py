code = """la_businesses = locals()['var_function-call-17565305056253761424']
gmap_ids = [b['gmap_id'] for b in la_businesses]
formatted_ids = ", ".join([f"'{gid}'" for gid in gmap_ids])
query = f"SELECT gmap_id, AVG(rating) as avg_rating FROM review WHERE gmap_id IN ({formatted_ids}) GROUP BY gmap_id ORDER BY avg_rating DESC LIMIT 5"
print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-7933422113418436164': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-17565305056253761424': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
