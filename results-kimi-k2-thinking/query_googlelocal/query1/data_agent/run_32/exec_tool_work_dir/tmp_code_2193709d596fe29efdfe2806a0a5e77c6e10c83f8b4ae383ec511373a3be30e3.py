code = """import json

# Load the data from storage
businesses = locals()['var_functions.query_db:10']
reviews = locals()['var_functions.query_db:12']

# Print for debugging
print('__DEBUG__:', f'Found {len(businesses)} businesses and {len(reviews)} reviews')

# Calculate average rating for each business
business_ratings = {}
business_names = {}
for biz in businesses:
    gmap_id = biz['gmap_id']
    business_names[gmap_id] = biz['name']
    business_ratings[gmap_id] = []

# Collect all ratings for each business
for review in reviews:
    gmap_id = review['gmap_id']
    if gmap_id in business_ratings:
        business_ratings[gmap_id].append(int(review['rating']))

# Calculate average ratings
results = []
for gmap_id, name in business_names.items():
    ratings = business_ratings[gmap_id]
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        results.append({
            'name': name,
            'gmap_id': gmap_id,
            'average_rating': round(avg_rating, 2),
            'num_reviews': len(ratings)
        })

# Sort by average rating descending
results_sorted = sorted(results, key=lambda x: x['average_rating'], reverse=True)

# Get top 5
top_5 = results_sorted[:5]

# Format output
output = top_5

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}], 'var_functions.query_db:12': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '3'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}], 'var_functions.list_db:14': ['review']}

exec(code, env_args)
