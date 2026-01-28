code = """import json
# Access the stored query results
r = var_call_T2Yy1LMW3gqK1ZcBz5pvcgek
b = var_call_otpFzah5TRLVSgMigQB7yaLF

# Convert counts to int and build mapping for business names
for rec in r:
    rec['high_count'] = int(rec['high_count'])

name_map = {rec['gmap_id']: rec['name'] for rec in b}

# Sort r by high_count desc and take top 3
r_sorted = sorted(r, key=lambda x: x['high_count'], reverse=True)
top3 = r_sorted[:3]

# Build output list with names and counts
output = []
for rec in top3:
    gid = rec['gmap_id']
    name = name_map.get(gid, None)
    output.append({'gmap_id': gid, 'name': name, 'high_rating_review_count_2019': rec['high_count']})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_T2Yy1LMW3gqK1ZcBz5pvcgek': [{'gmap_id': 'gmap_20', 'high_count': '8'}, {'gmap_id': 'gmap_53', 'high_count': '7'}, {'gmap_id': 'gmap_40', 'high_count': '6'}, {'gmap_id': 'gmap_35', 'high_count': '6'}, {'gmap_id': 'gmap_72', 'high_count': '5'}, {'gmap_id': 'gmap_62', 'high_count': '5'}, {'gmap_id': 'gmap_46', 'high_count': '5'}, {'gmap_id': 'gmap_17', 'high_count': '4'}, {'gmap_id': 'gmap_69', 'high_count': '3'}, {'gmap_id': 'gmap_56', 'high_count': '3'}], 'var_call_otpFzah5TRLVSgMigQB7yaLF': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'description': ' This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
