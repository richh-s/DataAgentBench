code = """business_list = [
    {"gmap_id": "gmap_22", "name": "Angel-A Massage"},
    {"gmap_id": "gmap_25", "name": "Elite Massage"},
    {"gmap_id": "gmap_33", "name": "Happy Spa & Massage (Formerly Hawaii Massage & Spa)"},
    {"gmap_id": "gmap_24", "name": "SUSY massage"},
    {"gmap_id": "gmap_20", "name": "Aurora Massage"},
    {"gmap_id": "gmap_21", "name": "Orient Massage"},
    {"gmap_id": "gmap_28", "name": "Good Massage"}
]

ratings_list = [
    {"gmap_id": "gmap_20", "avg_rating": 4.178571428571429},
    {"gmap_id": "gmap_22", "avg_rating": 4.333333333333333},
    {"gmap_id": "gmap_25", "avg_rating": 5.0}
]

# Create a dictionary for quick lookup
rating_map = {item['gmap_id']: item['avg_rating'] for item in ratings_list}

result = []
for bus in business_list:
    gid = bus['gmap_id']
    if gid in rating_map:
        result.append({
            "name": bus['name'],
            "average_rating": rating_map[gid]
        })

print("__RESULT__:")
import json
print(json.dumps(result))"""

env_args = {'var_function-call-17783408432297871559': ['business_description'], 'var_function-call-10374105728413835436': [], 'var_function-call-12945880079368130120': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'name': 'Vons Chicken', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Dunn-Edwards Paints', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-12949741235065287105': [], 'var_function-call-7677772113752617862': [{'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'MISC': 'None'}, {'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'MISC': 'None'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}'}, {'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.', 'MISC': '{"Health & safety": ["Mask required", "Staff wear masks"], "Accessibility": ["Wheelchair accessible entrance"]}'}, {'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.', 'MISC': 'None'}], 'var_function-call-15930647768117461074': [{'count': '7'}], 'var_function-call-7905189208244848456': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-18240810372838715218': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}]}

exec(code, env_args)
