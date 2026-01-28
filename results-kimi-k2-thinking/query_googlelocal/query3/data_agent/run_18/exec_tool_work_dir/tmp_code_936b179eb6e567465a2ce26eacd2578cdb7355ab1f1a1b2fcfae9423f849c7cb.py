code = """import json
import re

# Access stored data using locals() with the correct key format
business_data = locals()['var_functions.query_db:22']
review_data = locals()['var_functions.query_db:8']

# Check if these are file paths or data
if isinstance(business_data, str):
    with open(business_data, 'r') as f:
        business_data = json.load(f)

if isinstance(review_data, str):
    with open(review_data, 'r') as f:
        review_data = json.load(f)

# Function to check if business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the string representation of list
        hours_list = eval(hours_str)
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            day = day_info[0]
            hours_range = day_info[1]
            
            # Only check weekdays
            if day in weekdays:
                # Extract closing time (after dash)
                if '–' in hours_range:
                    closing = hours_range.split('–')[1].strip()
                elif '-' in hours_range:
                    closing = hours_range.split('-')[1].strip()
                else:
                    continue
                
                closing = closing.upper()
                
                # Parse time like "9:30PM" or "10PM" or "12AM"
                match = re.match(r'^(\d+):?(\d*)(AM|PM)$', closing)
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(2)) if match.group(2) else 0
                    period = match.group(3)
                    
                    # Convert to 24-hour format
                    if period == 'PM' and hour != 12:
                        hour += 12
                    elif period == 'AM' and hour == 12:
                        hour = 0
                    
                    # Check if after 6:00 PM (hour >= 18)
                    if hour > 18 or (hour == 18 and minute > 0):
                        return True
        
        return False
    except Exception as e:
        return False

# Filter businesses open after 6 PM on weekdays
eligible_businesses = []
for biz in business_data:
    if is_open_after_6pm(biz.get('hours')):
        eligible_businesses.append({
            'gmap_id': biz['gmap_id'],
            'name': biz['name'],
            'hours': biz['hours'],
            'description': biz.get('description', '')
        })

print('Found', len(eligible_businesses), 'businesses open after 6 PM on weekdays')

# Calculate average ratings for eligible businesses
from collections import defaultdict

# Group ratings by gmap_id
ratings_by_business = defaultdict(list)
for review in review_data:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    ratings_by_business[gmap_id].append(rating)

# Calculate average ratings for eligible businesses
business_ratings = []
for biz in eligible_businesses:
    gmap_id = biz['gmap_id']
    if gmap_id in ratings_by_business:
        ratings = ratings_by_business[gmap_id]
        avg_rating = sum(ratings) / len(ratings)
        business_ratings.append({
            'name': biz['name'],
            'hours': biz['hours'],
            'description': biz['description'],
            'avg_rating': avg_rating,
            'review_count': len(ratings)
        })

# Sort by average rating descending
business_ratings.sort(key=lambda x: x['avg_rating'], reverse=True)

top_5 = business_ratings[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
