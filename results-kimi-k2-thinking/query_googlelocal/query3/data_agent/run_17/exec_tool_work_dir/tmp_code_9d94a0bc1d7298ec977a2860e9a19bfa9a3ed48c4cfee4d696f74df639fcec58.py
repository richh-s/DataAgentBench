code = """import json

# Load review data
review_data_path = locals()['var_functions.query_db:12']
if isinstance(review_data_path, str) and review_data_path.endswith('.json'):
    with open(review_data_path, 'r') as f:
        reviews = json.load(f)
else:
    reviews = locals()['var_functions.query_db:12']

# Load business data
business_data = locals()['var_functions.execute_python:10']
businesses = business_data['businesses']

print(f'Reviews loaded: {len(reviews)}')
print(f'Businesses loaded: {len(businesses)}')

# Group reviews by gmap_id and calculate average rating
from collections import defaultdict

# Create mapping for businesses
business_map = {biz['gmap_id']: biz for biz in businesses}

# Group ratings by business
ratings_by_business = defaultdict(list)
for review in reviews:
    gmap_id = review['gmap_id']
    if gmap_id in business_map:
        try:
            rating = int(review['rating'])
            ratings_by_business[gmap_id].append(rating)
        except:
            continue

# Calculate average ratings
business_with_ratings = []
for gmap_id, ratings in ratings_by_business.items():
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        business = business_map[gmap_id]
        business_with_ratings.append({
            'name': business['name'],
            'gmap_id': gmap_id,
            'hours': business['hours'],
            'avg_rating': round(avg_rating, 2),
            'review_count': len(ratings)
        })

# Sort by average rating (descending)
business_with_ratings.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = business_with_ratings[:5]

print(f'Top 5 businesses with ratings:')
for i, biz in enumerate(top_5, 1):
    print(f"{i}. {biz['name']} - Avg Rating: {biz['avg_rating']} ({biz['review_count']} reviews)")

# Create result
result = {
    'top_businesses': top_5,
    'total_with_ratings': len(business_with_ratings)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'businesses': [{'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'J B Oriental Inc', 'gmap_id': 'gmap_32', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]'}, {'name': 'Hanford Auto Supply', 'gmap_id': 'gmap_16', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'The Beauty Bar', 'gmap_id': 'gmap_30', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53', 'hours': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]'}, {'name': 'Excel Hair & Nails', 'gmap_id': 'gmap_65', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'name': 'Beauty Divine Artistry', 'gmap_id': 'gmap_36', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'name': 'White Barn Candle Co', 'gmap_id': 'gmap_12', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]'}, {'name': "Rossy's Beauty Salon", 'gmap_id': 'gmap_7', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'name': 'TACOS LA CABANA', 'gmap_id': 'gmap_8', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'name': 'Dr. Syverain Skincare Clinic', 'gmap_id': 'gmap_5', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'name': "Ruby's Boutique", 'gmap_id': 'gmap_34', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–5PM"], ["Sunday", "11AM–4PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'name': 'Paradise tattoo', 'gmap_id': 'gmap_11', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]'}, {'name': 'Off The Hoof', 'gmap_id': 'gmap_61', 'hours': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]'}, {'name': 'Laptop Masters', 'gmap_id': 'gmap_47', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'name': 'Advanced Auto Upholstery', 'gmap_id': 'gmap_68', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]'}, {'name': 'LuXe Organic Nails Boutique', 'gmap_id': 'gmap_67', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]'}, {'name': 'St John Knits International Inc', 'gmap_id': 'gmap_64', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–6PM"], ["Sunday", "12:30–6PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40', 'hours': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'name': 'The Dream Junction', 'gmap_id': 'gmap_60', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}], 'count': 28}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
