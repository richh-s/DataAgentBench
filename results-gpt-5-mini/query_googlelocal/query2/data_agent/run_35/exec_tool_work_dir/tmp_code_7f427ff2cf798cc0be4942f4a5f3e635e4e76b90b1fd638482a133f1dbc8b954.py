code = """import json
# Access the stored query results
business_rows = var_call_5ch4EEC1EDt00l5KDwqsDEVV
review_avgs = var_call_52FxFEmlEqjl6DjjZ6XhIXRF

# Build mapping from gmap_id to business name
biz_map = {b['gmap_id']: b['name'] for b in business_rows}

# Combine results
combined = []
for r in review_avgs:
    gid = r['gmap_id']
    name = biz_map.get(gid, None)
    try:
        avg = float(r['avg_rating'])
    except:
        # If avg_rating already numeric or different format
        avg = float(r.get('avg_rating') or r.get('avg_rating'))
    combined.append({'gmap_id': gid, 'name': name, 'avg_rating': round(avg,2)})

# Sort by avg_rating descending
combined = sorted(combined, key=lambda x: x['avg_rating'], reverse=True)

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(combined, ensure_ascii=False))"""

env_args = {'var_call_1K6upc0mD1nLUZHv491lq6is': [], 'var_call_5ch4EEC1EDt00l5KDwqsDEVV': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_call_52FxFEmlEqjl6DjjZ6XhIXRF': [{'gmap_id': 'gmap_20', 'avg_rating': '4.18', 'num_reviews': '56'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.33', 'num_reviews': '6'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}]}

exec(code, env_args)
