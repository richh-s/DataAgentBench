code = """import json

businesses = [
    {"gmap_id": "gmap_44", "name": "City Textile"},
    {"gmap_id": "gmap_41", "name": "San Soo Dang"},
    {"gmap_id": "gmap_43", "name": "Nova Fabrics"},
    {"gmap_id": "gmap_38", "name": "Nobel Textile Co"},
    {"gmap_id": "gmap_39", "name": "Beads and More"},
    {"gmap_id": "gmap_42", "name": "Ace Jewelry & Loan"},
    {"gmap_id": "gmap_40", "name": "Widows Peak Salon"}
]

ratings = [
    {"gmap_id": "gmap_40", "avg_rating": 4.857142857142857},
    {"gmap_id": "gmap_44", "avg_rating": 4.5},
    {"gmap_id": "gmap_38", "avg_rating": 4.285714285714286},
    {"gmap_id": "gmap_41", "avg_rating": 4.277777777777778},
    {"gmap_id": "gmap_43", "avg_rating": 3.3333333333333335},
    {"gmap_id": "gmap_42", "avg_rating": 3.2857142857142856},
    {"gmap_id": "gmap_39", "avg_rating": 3.2222222222222223}
]

# Create a dictionary for mapping names
name_map = {b['gmap_id']: b['name'] for b in businesses}

# Add name to ratings and sort
results = []
for r in ratings:
    r['name'] = name_map.get(r['gmap_id'])
    results.append(r)

# Sort by rating desc (already sorted but good to be safe)
results.sort(key=lambda x: x['avg_rating'], reverse=True)

top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-6385996974514334384': ['business_description'], 'var_function-call-15352610640277347502': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-10690492812042136309': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_function-call-5063284682187237706': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}]}

exec(code, env_args)
