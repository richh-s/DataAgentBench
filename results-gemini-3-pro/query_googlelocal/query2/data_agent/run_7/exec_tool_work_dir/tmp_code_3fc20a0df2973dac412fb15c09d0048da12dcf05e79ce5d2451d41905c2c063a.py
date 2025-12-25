code = """import json

# Retrieve the file path for businesses
file_path = locals()['var_function-call-7515093237279247472']
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Create a map of gmap_id to name
id_to_name = {b['gmap_id']: b['name'] for b in businesses}

# Ratings from the previous step
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

# Filter and format
result = []
for r in ratings:
    if r['avg_rating'] >= 4.0:
        name = id_to_name.get(r['gmap_id'], "Unknown")
        result.append(f"{name}: {r['avg_rating']:.2f}")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9281345381939685788': ['business_description'], 'var_function-call-6788931000498659455': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-12525061072558791398': [], 'var_function-call-9386339100634993805': [], 'var_function-call-6254065447532325308': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1', 'hours': 'None', 'MISC': 'None', 'state': 'None'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'MISC': '{"Health & safety": ["Mask required", "Staff wear masks"], "Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.', 'num_of_reviews': '56', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}], 'var_function-call-2377105869888571977': [{'count': '0'}], 'var_function-call-3691123237654773434': [], 'var_function-call-6669768438046150058': [{'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}], 'var_function-call-4461301618740615902': [{'count': '0'}], 'var_function-call-16736916182479192247': [{'name': 'Angel-A Massage'}, {'name': 'Elite Massage'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'name': 'SUSY massage'}, {'name': 'Aurora Massage'}, {'name': 'Orient Massage'}, {'name': 'Good Massage'}], 'var_function-call-9237937699149413685': [], 'var_function-call-15569026002403817882': [{'count': '5'}], 'var_function-call-18341191687158303858': [{'count': '79'}], 'var_function-call-7515093237279247472': 'file_storage/function-call-7515093237279247472.json', 'var_function-call-12325269018617939339': ['gmap_22', 'gmap_25', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28'], 'var_function-call-9012634153553032673': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
