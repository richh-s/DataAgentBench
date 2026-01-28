code = """import json
import re

# Load business data
businesses_result = locals()['var_functions.query_db:10']
if isinstance(businesses_result, str) and businesses_result.endswith('.json'):
    with open(businesses_result, 'r') as f:
        businesses = json.load(f)
else:
    businesses = businesses_result

# Load review ratings data
ratings_result = locals()['var_functions.query_db:18']
if isinstance(ratings_result, str) and ratings_result.endswith('.json'):
    with open(ratings_result, 'r') as f:
        ratings = json.load(f)
else:
    ratings = ratings_result

print('Total businesses:', len(businesses))
print('Total rating records:', len(ratings))

# Create rating lookup
create_rating_lookup = {}
for r in ratings:
    create_rating_lookup[r['gmap_id']] = {
        'avg_rating': float(r['avg_rating']),
        'num_reviews': int(r['num_reviews'])
    }

# Function to parse time
def parse_closing_time(time_str):
    if not time_str or 'Closed' in time_str:
        return None
    if '24 hours' in time_str:
        return 24
    time_str = str(time_str).replace('\\u2013', '-').replace('\u2013', '-')
    parts = time_str.split('-')
    if len(parts) < 2:
        return None
    closing = parts[1].strip()
    closing = re.sub(r'[^a-zA-Z0-9:]', '', closing)
    match = re.match(r'(\d{1,2})(?::(\d{2}))?(AM|PM|am|pm)?', closing)
    if not match:
        return None
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    ampm = match.group(3)
    if ampm and ampm.upper() == 'PM' and hour != 12:
        hour += 12
    elif ampm and ampm.upper() == 'AM' and hour == 12:
        hour = 0
    return hour + minute / 60

# Filter businesses open after 6pm on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
businesses_after_6pm = []
for business in businesses:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours_str = business.get('hours')
    
    if not gmap_id or not name or not hours_str or hours_str == 'None':
        continue
    
    # Check if has ratings
    if gmap_id not in create_rating_lookup:
        continue
    
    try:
        hours_data = json.loads(hours_str.replace("'", '"'))
        for day_entry in hours_data:
            if len(day_entry) >= 2:
                day = day_entry[0]
                time_range = day_entry[1]
                if day in weekdays:
                    closing_time = parse_closing_time(time_range)
                    if closing_time is not None and closing_time >= 18:
                        businesses_after_6pm.append({
                            'gmap_id': gmap_id,
                            'name': name,
                            'hours': hours_str,
                            'avg_rating': create_rating_lookup[gmap_id]['avg_rating'],
                            'num_reviews': create_rating_lookup[gmap_id]['num_reviews']
                        })
                        break
    except:
        continue

print('Businesses after 6pm with ratings:', len(businesses_after_6pm))

# Sort by rating (highest first)
sorted_businesses = sorted(businesses_after_6pm, key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = sorted_businesses[:5]

# Format nicely
formatted_top_5 = []
for business in top_5:
    formatted_top_5.append({
        'name': business['name'],
        'hours': business['hours'],
        'average_rating': round(business['avg_rating'], 2),
        'number_of_reviews': business['num_reviews']
    })

print('Top 5 businesses:')
for i, b in enumerate(formatted_top_5, 1):
    print(f"{i}. {b['name']} - Rating: {b['average_rating']} ({b['number_of_reviews']} reviews)")

print('__RESULT__:')
print(json.dumps(formatted_top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:16': {'count': 31}, 'var_functions.query_db:18': [{'gmap_id': 'gmap_0', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_1', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_10', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605', 'num_reviews': '378'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_13', 'avg_rating': '4.625', 'num_reviews': '8'}, {'gmap_id': 'gmap_14', 'avg_rating': '4.375', 'num_reviews': '8'}, {'gmap_id': 'gmap_15', 'avg_rating': '4.911111111111111', 'num_reviews': '45'}, {'gmap_id': 'gmap_16', 'avg_rating': '5.0', 'num_reviews': '6'}, {'gmap_id': 'gmap_17', 'avg_rating': '4.970588235294118', 'num_reviews': '34'}, {'gmap_id': 'gmap_18', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_19', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_2', 'avg_rating': '4.705882352941177', 'num_reviews': '17'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429', 'num_reviews': '56'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333', 'num_reviews': '15'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333', 'num_reviews': '6'}, {'gmap_id': 'gmap_23', 'avg_rating': '1.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_25', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_26', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_27', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_29', 'avg_rating': '4.6923076923076925', 'num_reviews': '26'}, {'gmap_id': 'gmap_3', 'avg_rating': '4.666666666666667', 'num_reviews': '27'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857', 'num_reviews': '21'}, {'gmap_id': 'gmap_31', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667', 'num_reviews': '6'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125', 'num_reviews': '8'}, {'gmap_id': 'gmap_34', 'avg_rating': '4.5', 'num_reviews': '8'}, {'gmap_id': 'gmap_35', 'avg_rating': '4.142857142857143', 'num_reviews': '84'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_37', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'num_reviews': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'num_reviews': '18'}, {'gmap_id': 'gmap_4', 'avg_rating': '4.25', 'num_reviews': '4'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'num_reviews': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'num_reviews': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'num_reviews': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'num_reviews': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_45', 'avg_rating': '3.5', 'num_reviews': '6'}, {'gmap_id': 'gmap_46', 'avg_rating': '4.130952380952381', 'num_reviews': '168'}, {'gmap_id': 'gmap_47', 'avg_rating': '4.879310344827586', 'num_reviews': '58'}, {'gmap_id': 'gmap_48', 'avg_rating': '4.4', 'num_reviews': '5'}, {'gmap_id': 'gmap_49', 'avg_rating': '4.0', 'num_reviews': '8'}, {'gmap_id': 'gmap_5', 'avg_rating': '5.0', 'num_reviews': '5'}, {'gmap_id': 'gmap_50', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0', 'num_reviews': '18'}, {'gmap_id': 'gmap_52', 'avg_rating': '4.9655172413793105', 'num_reviews': '58'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263', 'num_reviews': '38'}, {'gmap_id': 'gmap_54', 'avg_rating': '3.875', 'num_reviews': '8'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_56', 'avg_rating': '5.0', 'num_reviews': '28'}, {'gmap_id': 'gmap_57', 'avg_rating': '4.184210526315789', 'num_reviews': '38'}, {'gmap_id': 'gmap_58', 'avg_rating': '4.75', 'num_reviews': '8'}, {'gmap_id': 'gmap_59', 'avg_rating': '4.631578947368421', 'num_reviews': '38'}, {'gmap_id': 'gmap_6', 'avg_rating': '4.75', 'num_reviews': '4'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058', 'num_reviews': '17'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_62', 'avg_rating': '4.411764705882353', 'num_reviews': '68'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375', 'num_reviews': '16'}, {'gmap_id': 'gmap_64', 'avg_rating': '4.25', 'num_reviews': '8'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615', 'num_reviews': '52'}, {'gmap_id': 'gmap_66', 'avg_rating': '4.5', 'num_reviews': '2'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806', 'num_reviews': '31'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0', 'num_reviews': '4'}, {'gmap_id': 'gmap_69', 'avg_rating': '4.395833333333333', 'num_reviews': '48'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838', 'num_reviews': '37'}, {'gmap_id': 'gmap_70', 'avg_rating': '4.888888888888889', 'num_reviews': '18'}, {'gmap_id': 'gmap_71', 'avg_rating': '2.0625', 'num_reviews': '16'}, {'gmap_id': 'gmap_72', 'avg_rating': '4.842105263157895', 'num_reviews': '38'}, {'gmap_id': 'gmap_73', 'avg_rating': '5.0', 'num_reviews': '1'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667', 'num_reviews': '18'}, {'gmap_id': 'gmap_75', 'avg_rating': '4.944055944055944', 'num_reviews': '143'}, {'gmap_id': 'gmap_76', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_77', 'avg_rating': '5.0', 'num_reviews': '3'}, {'gmap_id': 'gmap_78', 'avg_rating': '4.222222222222222', 'num_reviews': '18'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0', 'num_reviews': '2'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0', 'num_reviews': '3'}]}

exec(code, env_args)
