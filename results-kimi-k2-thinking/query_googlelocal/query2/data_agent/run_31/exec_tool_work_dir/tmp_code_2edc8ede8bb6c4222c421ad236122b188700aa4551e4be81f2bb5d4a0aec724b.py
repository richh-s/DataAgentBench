code = """import json

# Get massage businesses
massage_businesses = var_functions.query_db:5

# Get average ratings
avg_ratings = var_functions.query_db:10

# Create a dictionary for easy lookup
rating_dict = {item['gmap_id']: float(item['average_rating']) for item in avg_ratings}

# Filter massage therapy businesses with average rating >= 4.0 and store results
results = []
for business in massage_businesses:
    gmap_id = business['gmap_id']
    if gmap_id in rating_dict and rating_dict[gmap_id] >= 4.0:
        results.append({
            'business_name': business['name'],
            'average_rating': round(rating_dict[gmap_id], 2)
        })

# Sort by average rating (descending)
results_sorted = sorted(results, key=lambda x: x['average_rating'], reverse=True)

# Print in the required format
print('__RESULT__:')
print(json.dumps(results_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'average_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'average_rating': '3.875'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}, {'gmap_id': 'gmap_28', 'average_rating': '3.875'}, {'gmap_id': 'gmap_33', 'average_rating': '2.125'}]}

exec(code, env_args)
