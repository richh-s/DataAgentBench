code = """import json

# Load valid businesses
path_biz = locals()['var_function-call-11697219084862012695']
with open(path_biz, 'r') as f:
    businesses = json.load(f)

# Load ratings
ratings_data = locals()['var_function-call-13657885615843415677']
# Convert ratings list to dict
ratings_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_data}

# Merge
final_list = []
for b in businesses:
    gid = b['gmap_id']
    if gid in ratings_map:
        b['avg_rating'] = ratings_map[gid]
        final_list.append(b)

# Sort by rating desc
# Secondary sort by num_of_reviews desc? 
# The business dict has 'num_of_reviews' as a string, let's convert for tie breaking
for b in final_list:
    try:
        b['num_reviews_int'] = int(b.get('num_of_reviews', 0))
    except:
        b['num_reviews_int'] = 0

final_list.sort(key=lambda x: (x['avg_rating'], x['num_reviews_int']), reverse=True)

top_5 = final_list[:5]

# Format output
result = []
for b in top_5:
    result.append({
        "name": b['name'],
        "hours": b['hours'],
        "average_rating": b['avg_rating']
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11274278717337983726': ['business_description'], 'var_function-call-5679228863261529158': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-10625289044817991517': [{'count': '79'}], 'var_function-call-4041812981108132417': 'file_storage/function-call-4041812981108132417.json', 'var_function-call-11697219084862012695': 'file_storage/function-call-11697219084862012695.json', 'var_function-call-10319754412031917834': ['gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_11', 'gmap_61', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60'], 'var_function-call-15097456142815917549': "'gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_11', 'gmap_61', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60'", 'var_function-call-13657885615843415677': [{'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
