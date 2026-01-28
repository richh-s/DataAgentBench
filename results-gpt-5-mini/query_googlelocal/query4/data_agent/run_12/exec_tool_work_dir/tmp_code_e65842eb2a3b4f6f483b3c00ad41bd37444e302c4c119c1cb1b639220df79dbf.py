code = """import json
# load results from previous queries
reviews = var_call_damNuWLp6uANrBLbvrxfcPKJ
businesses = var_call_ulbt0PmBqQtlfVaLPRdYBgzM
# build name map
name_map = {b['gmap_id']: b.get('name') for b in businesses}
# convert counts to int
for r in reviews:
    try:
        r['high_rating_count'] = int(r['high_rating_count'])
    except:
        r['high_rating_count'] = 0
# sort and take top 3
reviews_sorted = sorted(reviews, key=lambda x: x['high_rating_count'], reverse=True)
top3 = reviews_sorted[:3]
output = []
for r in top3:
    gid = r['gmap_id']
    output.append({'name': name_map.get(gid, gid), 'high_rating_count': r['high_rating_count']})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_damNuWLp6uANrBLbvrxfcPKJ': [{'gmap_id': 'gmap_20', 'high_rating_count': '8'}, {'gmap_id': 'gmap_53', 'high_rating_count': '7'}, {'gmap_id': 'gmap_40', 'high_rating_count': '6'}, {'gmap_id': 'gmap_35', 'high_rating_count': '6'}, {'gmap_id': 'gmap_72', 'high_rating_count': '5'}, {'gmap_id': 'gmap_62', 'high_rating_count': '5'}, {'gmap_id': 'gmap_46', 'high_rating_count': '5'}, {'gmap_id': 'gmap_17', 'high_rating_count': '4'}, {'gmap_id': 'gmap_69', 'high_rating_count': '3'}, {'gmap_id': 'gmap_56', 'high_rating_count': '3'}], 'var_call_ulbt0PmBqQtlfVaLPRdYBgzM': [{'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_72', 'name': "Zuby's Brake Tires & Wheels"}, {'gmap_id': 'gmap_56', 'name': 'J & T Plumbing Pros'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}, {'gmap_id': 'gmap_62', 'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin'}, {'gmap_id': 'gmap_46', 'name': 'B2Sign, Inc.'}, {'gmap_id': 'gmap_69', 'name': 'Taitz Orly DDS'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
