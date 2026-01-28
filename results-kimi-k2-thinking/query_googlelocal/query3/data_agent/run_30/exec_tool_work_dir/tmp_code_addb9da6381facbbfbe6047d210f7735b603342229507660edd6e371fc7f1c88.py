code = """import json
import re
from collections import defaultdict

# Load business data
business_result = locals()['var_functions.query_db:5']
businesses = []
if isinstance(business_result, str) and business_result.endswith('.json'):
    with open(business_result, 'r') as f:
        businesses = json.load(f)
else:
    businesses = business_result

# Load review data
review_result = locals()['var_functions.query_db:6']
reviews = []
if isinstance(review_result, str) and review_result.endswith('.json'):
    with open(review_result, 'r') as f:
        reviews = json.load(f)
else:
    reviews = review_result

# Calculate average rating per business
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

# Function to parse closing time and check if business is open after 6 PM on weekdays
def is_open_after_6pm(hours_field):
    if hours_field == "None" or hours_field == None or not hours_field:
        return False
    
    if "Open 24 hours" in str(hours_field):
        return True
    
    try:
        # Parse the hours list (it's stored as a string representation)
        hours_list = json.loads(hours_field.replace("'", '"'))
        if not isinstance(hours_list, list):
            return False
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if not isinstance(day_info, list) or len(day_info) < 2:
                continue
                
            day_name = day_info[0]
            hours = day_info[1]
            
            # Check if a weekday
            if day_name in weekdays:
                # Extract closing time
                time_str = str(hours)
                # Look for closing time pattern like "6:30AM–6PM" or "9AM–10PM"
                parts = time_str.split('–')  # Use en-dash
                if len(parts) >= 2:
                    close_time = parts[1].strip()
                    
                    # Parse closing time
                    if 'PM' in close_time:
                        # Extract hour
                        hour_match = re.search(r'(\d{1,2})(?::(\d{2}))?PM', close_time)
                        if hour_match:
                            hour = int(hour_match.group(1))
                            if hour != 12:
                                hour += 12
                            # Check if after 6 PM (18:00)
                            if hour > 18:
                                return True
                            elif hour == 18:
                                # Check minutes
                                minutes = hour_match.group(2)
                                if minutes and int(minutes) > 0:
                                    return True
                    elif 'AM' in close_time:
                        # AM times are before 6 PM, skip
                        continue
    except:
        return False
    
    return False

# Find businesses open after 6 PM on weekdays
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

# Prepare result
result = []
for business in top_5_businesses:
    result.append({
        'name': business['name'],
        'hours': business['hours'],
        'average_rating': business['avg_rating']
    })

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
