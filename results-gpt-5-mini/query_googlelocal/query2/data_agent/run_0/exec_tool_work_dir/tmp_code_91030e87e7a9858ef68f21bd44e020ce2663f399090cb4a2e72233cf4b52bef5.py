code = """import json
businesses = var_call_a1DVFAnq9DGQxOxO1t8Fag19
reviews = var_call_KNa4tcnQ3KXDUH7bOYBKSagD
# Build mapping of gmap_id to average rating
map_avg = {r['gmap_id']: float(r['avg_rating']) for r in reviews}
result = []
for b in businesses:
    gid = b['gmap_id']
    if gid in map_avg and map_avg[gid] >= 4.0:
        result.append({'gmap_id': gid, 'name': b['name'], 'avg_rating': round(map_avg[gid], 3)})
# Print result as JSON string per required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EUzhCQGlEJEUsXzFVbRwxxyY': [], 'var_call_RRsSWUgGzbKrRD3oWPmSd2Yd': ['business_description'], 'var_call_a1DVFAnq9DGQxOxO1t8Fag19': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_KNa4tcnQ3KXDUH7bOYBKSagD': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'review_count': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'review_count': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'review_count': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'review_count': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'review_count': '8'}]}

exec(code, env_args)
