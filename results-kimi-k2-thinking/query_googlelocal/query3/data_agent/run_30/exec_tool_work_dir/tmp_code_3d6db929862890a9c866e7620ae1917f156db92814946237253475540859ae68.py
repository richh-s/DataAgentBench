code = """import json
import re
from datetime import datetime

# Load business data
business_file = var_functions.query_db:5
if isinstance(business_file, str):
    with open(business_file, 'r') as f:
        businesses = json.load(f)
else:
    businesses = business_file

# Load review data
review_file = var_functions.query_db:6
if isinstance(review_file, str):
    with open(review_file, 'r') as f:
        reviews = json.load(f)
else:
    reviews = review_file

# Calculate average rating per business
from collections import defaultdict

ratings_sum = defaultdict(float)
ratings_count = defaultdict(int)

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    ratings_sum[gmap_id] += rating
    ratings_count[gmap_id] += 1

avg_ratings = {}
for gmap_id in ratings_sum:
    avg_ratings[gmap_id] = round(ratings_sum[gmap_id] / ratings_count[gmap_id], 2)

# Function to parse closing time and check if business is open after 6 PM
def is_open_after_6pm(hours_field):
    if hours_field == "None" or hours_field == None:
        return False
    
    if "Open 24 hours" in str(hours_field):
        return True
    
    # Parse the hours list
    try:
        hours_list = eval(hours_field)  # Convert string representation of list to actual list
        if not isinstance(hours_list, list):
            return False
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if not isinstance(day_info, list) or len(day_info) < 2:
                continue
                
            day_name = day_info[0]
            hours = day_info[1]
            
            # Check if it's a weekday
            if day_name in weekdays:
                # Parse closing time (format: "9:30PM" or "9PM")
                time_match = re.search(r'(\d{1,2})(?::(\d{2}))?\u2013(\d{1,2})(?::(\d{2}))?(AM|PM)', str(hours))
                if time_match:
                    close_hour = int(time_match.group(3))
                    close_minute = int(time_match.group(4)) if time_match.group(4) else 0
                    close_ampm = time_match.group(5)
                    
                    # Convert to 24-hour format
                    if close_ampm == 'PM' and close_hour != 12:
                        close_hour += 12
                    elif close_ampm == 'AM' and close_hour == 12:
                        close_hour = 0
                    
                    # Check if closing time is after 6 PM (18:00)
                    if close_hour > 18 or (close_hour == 18 and close_minute > 0):
                        return True
    except:
        return False
    
    return False

# Find businesses that are open after 6 PM on at least one weekday
eligible_businesses = []
for business in businesses:
    gmap_id = business['gmap_id']
    name = business['name']
    hours = business['hours']
    
    if is_open_after_6pm(hours):
        avg_rating = avg_ratings.get(gmap_id, 0)
        eligible_businesses.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours,
            'avg_rating': avg_rating
        })

# Sort by average rating (descending) and get top 5
top_5_businesses = sorted(eligible_businesses, key=lambda x: x['avg_rating'], reverse=True)[:5]

# Format the output
result = []
for business in top_5_businesses:
    result.append({
        'name': business['name'],
        'hours': business['hours'],
        'average_rating': business['avg_rating']
    })

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
