code = """import json
import os

# Access variables using the correct key format
businesses_key = "var_functions.query_db:4"
reviews_key = "var_functions.query_db:6"

businesses = locals()[businesses_key]
reviews_data = locals()[reviews_key]

# Check if reviews_data is a file path (string containing .json)
if isinstance(reviews_data, str) and '.json' in reviews_data:
    with open(reviews_data, 'r') as f:
        reviews = json.load(f)
else:
    reviews = reviews_data

from collections import defaultdict

# Calculate average rating for each business
business_ratings = defaultdict(list)
for review in reviews:
    biz_id = review.get('gmap_id')
    rating_str = review.get('rating', '0')
    rating = int(rating_str) if rating_str else 0
    if biz_id and rating > 0:
        business_ratings[biz_id].append(rating)

# Calculate averages and filter for massage businesses with avg >= 4.0
valid_businesses = []
for business in businesses:
    biz_id = business.get('gmap_id')
    name = business.get('name')
    description = business.get('description', '').lower()
    
    # Double-check it's a massage business (contains 'massage')
    if 'massage' in name.lower() or 'massage' in description:
        if biz_id and biz_id in business_ratings:
            ratings = business_ratings[biz_id]
            if len(ratings) > 0:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating >= 4.0:
                    valid_businesses.append({
                        'name': name,
                        'avg_rating': round(avg_rating, 2),
                        'total_reviews': len(ratings)
                    })

# Sort by avg_rating descending
valid_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps(valid_businesses))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['business_description'], 'var_functions.query_db:4': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1', 'hours': 'None', 'MISC': 'None', 'state': 'None'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'MISC': '{"Health & safety": ["Mask required", "Staff wear masks"], "Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 10PM'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.', 'num_of_reviews': '56', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.', 'num_of_reviews': '15', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 8PM'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.', 'num_of_reviews': '8', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
