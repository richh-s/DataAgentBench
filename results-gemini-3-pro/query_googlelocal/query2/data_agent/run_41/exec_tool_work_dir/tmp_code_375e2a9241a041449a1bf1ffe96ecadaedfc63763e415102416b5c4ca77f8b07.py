code = """businesses = [
    {"gmap_id": "gmap_22", "name": "Angel-A Massage"},
    {"gmap_id": "gmap_25", "name": "Elite Massage"},
    {"gmap_id": "gmap_33", "name": "Happy Spa & Massage (Formerly Hawaii Massage & Spa)"},
    {"gmap_id": "gmap_24", "name": "SUSY massage"},
    {"gmap_id": "gmap_20", "name": "Aurora Massage"},
    {"gmap_id": "gmap_21", "name": "Orient Massage"},
    {"gmap_id": "gmap_28", "name": "Good Massage"}
]

ratings = [
    {"gmap_id": "gmap_20", "average_rating": 4.178571428571429},
    {"gmap_id": "gmap_22", "average_rating": 4.333333333333333},
    {"gmap_id": "gmap_25", "average_rating": 5.0}
]

# Create a dictionary for easier lookup
rating_map = {r['gmap_id']: r['average_rating'] for r in ratings}

results = []
for b in businesses:
    if b['gmap_id'] in rating_map:
        results.append({
            "name": b['name'],
            "rating": rating_map[b['gmap_id']]
        })

# Sort by rating descending
results.sort(key=lambda x: x['rating'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13773535584363565211': ['business_description'], 'var_function-call-6426219777282074831': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-14685591670898640594': [], 'var_function-call-15936418695026787449': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-16573804257345453677': [], 'var_function-call-1765972488923564925': [], 'var_function-call-14160876151670198209': [{'count': '7'}], 'var_function-call-8731732505179527208': [], 'var_function-call-3005399231184841627': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-5196475174759749129': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}]}

exec(code, env_args)
