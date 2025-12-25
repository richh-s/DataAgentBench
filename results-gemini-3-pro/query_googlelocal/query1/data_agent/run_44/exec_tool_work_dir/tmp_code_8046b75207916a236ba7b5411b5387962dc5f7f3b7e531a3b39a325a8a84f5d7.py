code = """ids = [item['gmap_id'] for item in locals()['var_function-call-12240159531678146068']]
ids_str = "', '".join(ids)
query = f"SELECT gmap_id, AVG(rating) as avg_rating FROM review WHERE gmap_id IN ('{ids_str}') GROUP BY gmap_id"
print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-17124961816867055470': ['business_description'], 'var_function-call-12217518646542164476': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-12240159531678146068': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
