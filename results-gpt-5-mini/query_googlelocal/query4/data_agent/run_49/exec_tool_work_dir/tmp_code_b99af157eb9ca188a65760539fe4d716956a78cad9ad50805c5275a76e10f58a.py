code = """import json
# var_call_hnt5zbSXAMPZM57FczBguUrv and var_call_eA7bbZw8CUoAqsQy1FveVRQD are available from previous tool calls
records = var_call_hnt5zbSXAMPZM57FczBguUrv
biz = var_call_eA7bbZw8CUoAqsQy1FveVRQD
# Build mapping from gmap_id to name
name_map = {b['gmap_id']: b.get('name') for b in biz}
# Take top 3 from records (already ordered)
top3 = []
for r in records[:3]:
    gid = r['gmap_id']
    count = int(r['high_reviews'])
    top3.append({
        'gmap_id': gid,
        'name': name_map.get(gid),
        'high_rating_review_count_2019': count
    })
# Print result as JSON string
print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_hnt5zbSXAMPZM57FczBguUrv': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}], 'var_call_eA7bbZw8CUoAqsQy1FveVRQD': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'description': ' This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews.'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'description': ' Offering comprehensive medical care and personalized health solutions in Encino, CA 91436, this clinic specializes in diagnosing and treating a wide range of health conditions.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
