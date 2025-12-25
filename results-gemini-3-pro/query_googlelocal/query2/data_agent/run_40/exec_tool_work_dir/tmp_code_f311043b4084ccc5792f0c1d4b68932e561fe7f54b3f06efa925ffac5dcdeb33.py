code = """import json

massage_businesses = locals()['var_function-call-5350713441067248847']
ratings = locals()['var_function-call-14227904976371880426']

# Create a dict for easier lookup
rating_map = {r['gmap_id']: float(r['average_rating']) for r in ratings}

results = []
for b in massage_businesses:
    gmap_id = b['gmap_id']
    if gmap_id in rating_map:
        avg_rating = rating_map[gmap_id]
        if avg_rating >= 4.0:
            results.append(f"{b['name']} (Average Rating: {avg_rating:.1f})")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5007988614706420722': [], 'var_function-call-17816984502836671407': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-12620051190098276383': [{'count': '79'}], 'var_function-call-7748127306055849001': 'file_storage/function-call-7748127306055849001.json', 'var_function-call-5350713441067248847': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}], 'var_function-call-14227904976371880426': [{'gmap_id': 'gmap_20', 'average_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'average_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'average_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'average_rating': '3.875'}, {'gmap_id': 'gmap_25', 'average_rating': '5.0'}, {'gmap_id': 'gmap_28', 'average_rating': '3.875'}, {'gmap_id': 'gmap_33', 'average_rating': '2.125'}]}

exec(code, env_args)
