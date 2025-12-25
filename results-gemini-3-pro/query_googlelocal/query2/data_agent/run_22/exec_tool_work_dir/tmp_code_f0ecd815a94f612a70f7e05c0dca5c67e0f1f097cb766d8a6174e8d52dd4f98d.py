code = """# merge results
businesses = [
    {"gmap_id": "gmap_22", "name": "Angel-A Massage"},
    {"gmap_id": "gmap_25", "name": "Elite Massage"},
    {"gmap_id": "gmap_33", "name": "Happy Spa & Massage (Formerly Hawaii Massage & Spa)"},
    {"gmap_id": "gmap_24", "name": "SUSY massage"},
    {"gmap_id": "gmap_20", "name": "Aurora Massage"},
    {"gmap_id": "gmap_32", "name": "J B Oriental Inc"},
    {"gmap_id": "gmap_21", "name": "Orient Massage"},
    {"gmap_id": "gmap_28", "name": "Good Massage"}
]

ratings = [
    {"gmap_id": "gmap_20", "avg_rating": 4.178571428571429},
    {"gmap_id": "gmap_21", "avg_rating": 3.933333333333333},
    {"gmap_id": "gmap_22", "avg_rating": 4.333333333333333},
    {"gmap_id": "gmap_24", "avg_rating": 3.875},
    {"gmap_id": "gmap_25", "avg_rating": 5.0},
    {"gmap_id": "gmap_28", "avg_rating": 3.875},
    {"gmap_id": "gmap_32", "avg_rating": 4.166666666666667},
    {"gmap_id": "gmap_33", "avg_rating": 2.125}
]

# Create a dictionary for easier lookup
rating_dict = {item['gmap_id']: item['avg_rating'] for item in ratings}

qualified = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_dict:
        r = rating_dict[gid]
        if r >= 4.0:
            qualified.append({"name": b['name'], "rating": r})

# Sort by rating descending
qualified.sort(key=lambda x: x['rating'], reverse=True)

import json
print("__RESULT__:")
print(json.dumps(qualified))"""

env_args = {'var_function-call-5885585641987015372': ['business_description'], 'var_function-call-5885585641987016707': ['review'], 'var_function-call-12190077604835343351': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'gmap_id': 'gmap_45'}], 'var_function-call-17556683144203984993': [], 'var_function-call-8562984776749068927': [], 'var_function-call-3649821472116695050': [], 'var_function-call-17602129121979066430': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}], 'var_function-call-5366474276884971722': [{'count': '79'}], 'var_function-call-1375595021994511441': 'file_storage/function-call-1375595021994511441.json', 'var_function-call-3052380346951741510': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-7783516357794462478': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'description': ' Experience rejuvenating therapies and soothing body treatments designed to enhance relaxation and well-being in Roseville, CA 95747.'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-2607231314848306943': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
