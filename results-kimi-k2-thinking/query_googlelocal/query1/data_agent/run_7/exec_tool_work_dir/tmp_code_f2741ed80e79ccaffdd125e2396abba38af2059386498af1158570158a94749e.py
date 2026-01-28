code = """import json

# Get the data from storage
business_data = var_functions.query_db:6  # Los Angeles businesses
review_data = var_functions.query_db:8    # Reviews for those businesses

# Calculate average ratings for each business
from collections import defaultdict

business_dict = {b['gmap_id']: b['name'] for b in business_data}
rating_sums = defaultdict(int)
rating_counts = defaultdict(int)

for review in review_data:
    rating = int(review['rating'])
    gmap_id = review['gmap_id']
    rating_sums[gmap_id] += rating
    rating_counts[gmap_id] += 1

# Calculate averages
avg_ratings = []
for gmap_id, name in business_dict.items():
    if rating_counts[gmap_id] > 0:
        avg = rating_sums[gmap_id] / rating_counts[gmap_id]
        avg_ratings.append({
            'gmap_id': gmap_id,
            'name': name,
            'avg_rating': round(avg, 2),
            'num_reviews': rating_counts[gmap_id]
        })

# Sort by average rating descending
avg_ratings_sorted = sorted(avg_ratings, key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = avg_ratings_sorted[:5]

# Prepare result for printing
result = json.dumps(top_5, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '1'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}, {'gmap_id': 'gmap_43', 'rating': '3'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '1'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_43', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '1'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_38', 'rating': '4'}, {'gmap_id': 'gmap_38', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '3'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '4'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '1'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_39', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_42', 'rating': '1'}, {'gmap_id': 'gmap_42', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '4'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}, {'gmap_id': 'gmap_40', 'rating': '5'}]}

exec(code, env_args)
