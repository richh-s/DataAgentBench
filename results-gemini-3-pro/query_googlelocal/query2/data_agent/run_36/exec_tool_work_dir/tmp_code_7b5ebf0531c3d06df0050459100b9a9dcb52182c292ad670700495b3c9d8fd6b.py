code = """import json
ids = ["gmap_20", "gmap_22", "gmap_25"]
names = {
    "gmap_20": "Aurora Massage",
    "gmap_22": "Angel-A Massage",
    "gmap_25": "Elite Massage"
}
ratings = {
    "gmap_20": 4.178571428571429,
    "gmap_22": 4.333333333333333,
    "gmap_25": 5.0
}

result = []
for pid in ids:
    result.append({"name": names[pid], "average_rating": ratings[pid]})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8598077439641863820': [], 'var_function-call-7563989624583399716': [{'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'name': 'Vons Chicken', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Dunn-Edwards Paints', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_function-call-5360667592113736999': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}], 'var_function-call-10693045663705286331': [{'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}]}

exec(code, env_args)
