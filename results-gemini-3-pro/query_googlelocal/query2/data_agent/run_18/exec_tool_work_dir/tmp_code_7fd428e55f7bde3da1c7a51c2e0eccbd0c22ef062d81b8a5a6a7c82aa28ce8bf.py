code = """import json

businesses = [
    {"gmap_id": "gmap_22", "name": "Angel-A Massage"}, 
    {"gmap_id": "gmap_25", "name": "Elite Massage"}, 
    {"gmap_id": "gmap_33", "name": "Happy Spa & Massage (Formerly Hawaii Massage & Spa)"}, 
    {"gmap_id": "gmap_24", "name": "SUSY massage"}, 
    {"gmap_id": "gmap_20", "name": "Aurora Massage"}, 
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
    {"gmap_id": "gmap_33", "avg_rating": 2.125}
]

# Convert ratings to dict for easy lookup
rating_map = {r['gmap_id']: r['avg_rating'] for r in ratings}

result_list = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_map:
        avg = rating_map[gid]
        if avg >= 4.0:
            result_list.append({"name": b['name'], "average_rating": avg})

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-11402244118421909496': ['business_description'], 'var_function-call-11402244118421906793': ['review'], 'var_function-call-2892149849529187797': [], 'var_function-call-15774698624045172324': [{'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'description': ' This professional headquarters in McClellan Park, CA 95652, serves as a central hub for strategic operations and management activities.'}, {'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'description': ' Experience rejuvenating therapies and soothing body treatments designed to enhance relaxation and well-being in Roseville, CA 95747.'}, {'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'description': ' This convenient transit hub in El Centro, CA 92243 offers a reliable pick-up and drop-off point for travelers and commuters alike.'}, {'description': ' Located in San Diego, CA 92108, this firm specializes in providing expert technical guidance and innovative solutions for complex engineering challenges.'}, {'description': ' This Sacramento-based company specializes in providing a wide range of entryway solutions and high-quality doors for residential and commercial needs, located in Sacramento, CA 95834.'}, {'description': ' Located in Hanford, CA 93230, this shop offers a wide selection of automotive components and accessories to meet all your vehicle maintenance needs.'}], 'var_function-call-3792840469430870159': [], 'var_function-call-6337519805429178370': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}], 'var_function-call-6137192567287899319': [{'MISC': 'None'}], 'var_function-call-14600773780178381830': [{'count': '7'}], 'var_function-call-7352993736079296275': [{'count': '79'}], 'var_function-call-11862073427200848701': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-15036344552115092719': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
