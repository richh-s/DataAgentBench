code = """import json

# Read the eligible businesses data
eligible_file = locals()['var_functions.execute_python:22']
with open(eligible_file, 'r') as f:
    eligible_data = json.load(f)

eligible_businesses = eligible_data['eligible_businesses']
business_info_map = {b['gmap_id']: b for b in eligible_businesses}

# Read the reviews data
reviews_file = locals()['var_functions.query_db:26']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

print(f"Total reviews to process: {len(reviews_data)}")
print(f"Sample review: {reviews_data[0] if reviews_data else 'None'}")

# Calculate average rating per business
from collections import defaultdict
import numpy as np

business_ratings = defaultdict(list)
for review in reviews_data:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    business_ratings[gmap_id].append(rating)

# Calculate averages and stats
business_averages = {}
for gmap_id, ratings in business_ratings.items():
    avg_rating = np.mean(ratings)
    business_averages[gmap_id] = {
        'average_rating': round(avg_rating, 2),
        'review_count': len(ratings),
        'business_info': business_info_map.get(gmap_id, {})
    }

print(f"Businesses with reviews: {len(business_averages)}")

# Sort by average rating descending
sorted_businesses = sorted(business_averages.items(), key=lambda x: x[1]['average_rating'], reverse=True)

print(f"Top rated business: {sorted_businesses[0] if sorted_businesses else 'None'}")

# Get top 5
top_5 = sorted_businesses[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5': top_5,
    'total_with_ratings': len(sorted_businesses)
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.', 'num_of_reviews': '18', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.', 'num_of_reviews': '34', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.', 'num_of_reviews': '26', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'hours': 'None', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1', 'state': 'None'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:16': {'total_businesses': 38, 'sample_entries': 'fil', 'data_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'total_businesses': 66, 'sample_entries': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}], 'first_entry_hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': {'gmap_ids': ['gmap_41', 'gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_16', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_5', 'gmap_34', 'gmap_11', 'gmap_61', 'gmap_47', 'gmap_68', 'gmap_67', 'gmap_64', 'gmap_40', 'gmap_60'], 'business_info_map_keys': ['gmap_41', 'gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_16', 'gmap_28']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
