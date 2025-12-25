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

# Create a dictionary for easy lookup
biz_dict = {b['gmap_id']: b['name'] for b in businesses}

top_5 = []
for r in ratings[:5]:
    name = biz_dict.get(r['gmap_id'], "Unknown")
    top_5.append(f"{name} (Rating: {r['avg_rating']:.2f})")

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-1420727427030071195': ['business_description'], 'var_function-call-14801318699149957110': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-11488886057836341714': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_function-call-403084766639082981': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223'}]}

exec(code, env_args)
