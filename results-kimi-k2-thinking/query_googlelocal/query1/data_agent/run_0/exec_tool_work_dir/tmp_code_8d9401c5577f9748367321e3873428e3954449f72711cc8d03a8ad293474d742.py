code = """import json

# Ratings data from review database
ratings_data = [
    {"gmap_id": "gmap_40", "avg_rating": "4.857142857142857", "review_count": "35"},
    {"gmap_id": "gmap_44", "avg_rating": "4.5", "review_count": "6"},
    {"gmap_id": "gmap_38", "avg_rating": "4.285714285714286", "review_count": "7"},
    {"gmap_id": "gmap_41", "avg_rating": "4.277777777777778", "review_count": "18"},
    {"gmap_id": "gmap_43", "avg_rating": "3.3333333333333335", "review_count": "6"},
    {"gmap_id": "gmap_42", "avg_rating": "3.2857142857142856", "review_count": "7"},
    {"gmap_id": "gmap_39", "avg_rating": "3.2222222222222223", "review_count": "18"}
]

# Business names data
business_names = [
    {"gmap_id": "gmap_42", "name": "Ace Jewelry & Loan"},
    {"gmap_id": "gmap_39", "name": "Beads and More"},
    {"gmap_id": "gmap_44", "name": "City Textile"},
    {"gmap_id": "gmap_38", "name": "Nobel Textile Co"},
    {"gmap_id": "gmap_43", "name": "Nova Fabrics"},
    {"gmap_id": "gmap_41", "name": "San Soo Dang"},
    {"gmap_id": "gmap_40", "name": "Widows Peak Salon"}
]

# Map gmap_id to business name
name_map = {b['gmap_id']: b['name'] for b in business_names}

# Create top 5 list (already sorted by rating DESC)
top_5 = []
for i, item in enumerate(ratings_data[:5]):
    gmap_id = item['gmap_id']
    top_5.append({
        'rank': i + 1,
        'business_name': name_map[gmap_id],
        'average_rating': round(float(item['avg_rating']), 2),
        'review_count': int(item['review_count'])
    })

# Format answer as string
result_str = "Top 5 Businesses in Los Angeles, California by Average Rating (Descending):\n\n"
for biz in top_5:
    result_str += f"{biz['rank']}. {biz['business_name']}\n"
    result_str += f"   Average Rating: {biz['average_rating']}/5\n"
    result_str += f"   Number of Reviews: {biz['review_count']}\n\n"

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'MISC': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'MISC': '{"Service options": ["In-store pickup"]}'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'MISC': '{"Service options": ["In-store shopping"], "Accessibility": ["Wheelchair accessible entrance"], "Planning": ["Quick visit"]}'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'MISC': '{"Service options": ["In-store shopping"], "Accessibility": ["Wheelchair accessible entrance"], "Planning": ["Quick visit"]}'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"], "Amenities": ["Wi-Fi"], "Planning": ["Appointments recommended"], "Payments": ["Debit cards", "NFC mobile payments", "Credit cards"]}'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}], 'var_functions.query_db:12': [{'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
