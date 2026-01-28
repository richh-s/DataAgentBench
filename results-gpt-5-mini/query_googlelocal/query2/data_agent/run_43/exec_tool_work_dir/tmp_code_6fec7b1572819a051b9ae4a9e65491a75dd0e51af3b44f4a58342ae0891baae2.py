code = """import json
# Access stored query results
biz_rows = var_call_GSM3r3ymLxOyaoB0rMZgHSDV
review_aggs = var_call_REHMuDzxI6zVBZ6aFIZpeeo4

# Build mapping from gmap_id to business name
biz_map = {row['gmap_id']: row['name'] for row in biz_rows}

results = []
for r in review_aggs:
    try:
        avg = float(r['avg_rating'])
    except:
        continue
    if avg >= 4.0:
        results.append({
            'gmap_id': r['gmap_id'],
            'name': biz_map.get(r['gmap_id'], None),
            'avg_rating': round(avg, 3),
            'num_reviews': int(r['num_reviews'])
        })

# sort by avg_rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_vxdvMTKaJHRxkEv87ygihben': [], 'var_call_GSM3r3ymLxOyaoB0rMZgHSDV': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_REHMuDzxI6zVBZ6aFIZpeeo4': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}]}

exec(code, env_args)
