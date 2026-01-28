code = """import json
import ast
import re
from datetime import datetime

# Access the data from storage using locals()
businesses_key = 'var_functions.query_db:7'
reviews_key = 'var_functions.query_db:8'

businesses_data = locals().get(businesses_key, [])
reviews_data = locals().get(reviews_key, [])

# If they're strings (file paths), load them
if isinstance(businesses_data, str) and '.json' in businesses_data:
    with open(businesses_data, 'r') as f:
        businesses_data = json.load(f)

if isinstance(reviews_data, str) and '.json' in reviews_data:
    with open(reviews_data, 'r') as f:
        reviews_data = json.load(f)

# Function to parse time strings and check if closing time is after 6 PM
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string - it's stored as a string representation of a list
        hours_list = ast.literal_eval(hours_str)
        
        for day_schedule in hours_list:
            if len(day_schedule) != 2:
                continue
                
            day, hours = day_schedule
            
            # Skip closed days
            if hours == 'Closed':
                continue
                
            # Handle "Open 24 hours"
            if hours == 'Open 24 hours':
                return True
            
            # Parse time range (e.g., "6:30AM–6PM" or "11AM–9:30PM")
            # Handle the unicode dash
            time_parts = hours.replace('–', '-').replace('—', '-').split('-')
            if len(time_parts) != 2:
                continue
            
            open_time, close_time = time_parts
            
            # Parse closing time
            close_time = close_time.strip()
            
            # Handle various time formats
            if ':' in close_time:
                if 'PM' in close_time:
                    hour = int(close_time.split(':')[0])
                    if hour == 12:
                        hour = 12
                    else:
                        hour += 12
                    minute = int(close_time.split(':')[1].replace('PM', '').replace('AM', ''))
                elif 'AM' in close_time:
                    hour = int(close_time.split(':')[0])
                    minute = int(close_time.split(':')[1].replace('PM', '').replace('AM', ''))
                else:
                    continue
            else:
                # No colon, e.g., "6PM"
                if 'PM' in close_time:
                    hour_part = close_time.replace('PM', '')
                    if hour_part:
                        hour = int(hour_part)
                        if hour == 12:
                            hour = 12
                        else:
                            hour += 12
                        minute = 0
                    else:
                        continue
                elif 'AM' in close_time:
                    hour_part = close_time.replace('AM', '')
                    if hour_part:
                        hour = int(hour_part)
                        minute = 0
                    else:
                        continue
                else:
                    continue
            
            # Check if closing time is after 6:00 PM (18:00)
            if hour > 18 or (hour == 18 and minute > 0):
                return True
                
    except Exception as e:
        # If parsing fails, return False
        return False
    
    return False

# Filter businesses that are open after 6 PM on at least one weekday
businesses_open_after_6 = []

for business in businesses_data:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours_str = business.get('hours')
    
    # Check if this business is open after 6 PM on any weekday
    if is_open_after_6pm(hours_str):
        businesses_open_after_6.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours_str
        })

# Calculate average ratings for these businesses
# First, group reviews by gmap_id
business_ratings = {}
for review in reviews_data:
    gmap_id = review.get('gmap_id')
    rating = review.get('rating')
    
    if gmap_id and rating is not None:
        if gmap_id not in business_ratings:
            business_ratings[gmap_id] = []
        business_ratings[gmap_id].append(int(rating))

# Calculate average rating for businesses that are open after 6 PM
businesses_with_ratings = []
for business in businesses_open_after_6:
    gmap_id = business['gmap_id']
    if gmap_id in business_ratings:
        ratings = business_ratings[gmap_id]
        avg_rating = sum(ratings) / len(ratings)
        review_count = len(ratings)
        
        businesses_with_ratings.append({
            'name': business['name'],
            'hours': business['hours'],
            'average_rating': round(avg_rating, 2),
            'review_count': review_count
        })

# Sort by average rating (descending) and get top 5
top_5_businesses = sorted(businesses_with_ratings, key=lambda x: x['average_rating'], reverse=True)[:5]

# Prepare result
result = {
    'top_5_businesses': top_5_businesses,
    'total_filtered': len(businesses_open_after_6),
    'total_with_reviews': len(businesses_with_ratings)
}

result_json = json.dumps(result)
print(result_json)"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:3': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
