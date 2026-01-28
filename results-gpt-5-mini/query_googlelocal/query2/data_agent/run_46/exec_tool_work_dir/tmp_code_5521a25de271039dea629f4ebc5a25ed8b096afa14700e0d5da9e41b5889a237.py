code = """import json
# Accessing previous query results from storage variables
business_rows = var_call_egECnZFqej31fgYGne3bsOA5
rating_rows = var_call_zdHt7pP135JH4HfB0kDoKO2r

# Build mapping from gmap_id to business name
id_to_name = {row['gmap_id']: row.get('name') for row in business_rows}

# Process ratings and select businesses with avg_rating >= 4.0
results = []
for r in rating_rows:
    gid = r['gmap_id']
    try:
        avg = float(r['avg_rating'])
    except Exception:
        continue
    if avg >= 4.0 and gid in id_to_name:
        results.append({'name': id_to_name[gid], 'gmap_id': gid, 'avg_rating': round(avg, 3)})

# Sort by avg_rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

# Prepare JSON string
output = json.dumps(results)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_MSfE1tHfOXmljTDcIZ0dJXMv': [], 'var_call_egECnZFqej31fgYGne3bsOA5': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_zdHt7pP135JH4HfB0kDoKO2r': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'n_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'n_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'n_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'n_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'n_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'n_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'n_reviews': '8'}]}

exec(code, env_args)
