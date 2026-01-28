code = """import json
import re
import os

# Load data from the files
review_file = '/tmp/tmptzz9e_0k.json'
business_file = '/tmp/tmph4_28y_m.json'

# Load the data
with open(review_file, 'r') as f:
    review_data = json.load(f)

with open(business_file, 'r') as f:
    business_data = json.load(f)

def parse_time_to_minutes(time_str):
    """Parse time string to total minutes since midnight"""
    try:
        # Handle formats like "6:30AM", "9:30PM", "Open 24 hours", etc.
        time_str = time_str.strip().upper()
        
        if 'OPEN 24 HOURS' in time_str or '24 HOURS' in time_str:
            return 0, 1440  # Open all day
        if time_str == 'CLOSED':
            return None, None
        
        # Handle various formats like "9:30PM", "9PM", "12AM", etc.
        if ':' in time_str:
            # Format: "9:30PM" or "9:30 PM"
            time_part = time_str.replace(' ', '')
            match = re.match(r'(\d{1,2}):(\d{2})(AM|PM)', time_part)
            if match:
                hour = int(match.group(1))
                minute = int(match.group(2))
                period = match.group(3)
            else:
                return None, None
        else:
            # Format: "9PM" or "9 PM"
            time_part = time_str.replace(' ', '')
            match = re.match(r'(\d{1,2})(AM|PM)', time_part)
            if match:
                hour = int(match.group(1))
                minute = 0
                period = match.group(2)
            else:
                return None, None
        
        # Convert to 24-hour format
        if period == 'PM' and hour != 12:
            hour += 12
        elif period == 'AM' and hour == 12:
            hour = 0
            
        return hour * 60 + minute
    except:
        return None

def is_open_after_6pm(hours_array):
    """Check if business is open after 6PM (18:00) on any weekday"""
    if not hours_array or hours_array == 'None':
        return False
    
    try:
        # Parse the hours array string into Python list
        if isinstance(hours_array, str):
            hours_list = ast.literal_eval(hours_array)
        else:
            hours_list = hours_array
        
        six_pm_minutes = 18 * 60  # 6PM in minutes
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_hours in hours_list:
            if len(day_hours) >= 2:
                day = day_hours[0]
                hours_str = day_hours[1]
                
                # Only check weekdays
                if day in weekdays:
                    # Parse the time range (e.g., "6:30AM–6PM" or "9AM–5PM")
                    if '–' in hours_str or '-' in hours_str:
                        # Handle both en dash and regular dash
                        if '–' in hours_str:
                            time_range = hours_str.split('–')
                        else:
                            time_range = hours_str.split('-')
                        
                        if len(time_range) == 2:
                            close_time = parse_time_to_minutes(time_range[1])
                            if close_time and close_time > six_pm_minutes:
                                return True
                    elif 'OPEN 24 HOURS' in hours_str.upper():
                        return True
        
        return False
    except:
        return False

# Calculate average rating per business
business_ratings = {}
for review in review_data:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id not in business_ratings:
        business_ratings[gmap_id] = []
    business_ratings[gmap_id].append(rating)

# Calculate averages
business_avg_ratings = {}
for gmap_id, ratings in business_ratings.items():
    if len(ratings) >= 1:  # At least one review
        avg_rating = sum(ratings) / len(ratings)
        business_avg_ratings[gmap_id] = {
            'avg_rating': round(avg_rating, 2),
            'review_count': len(ratings)
        }

# Find businesses open after 6PM and combine with ratings
results = []
for business in business_data:
    gmap_id = business['gmap_id']
    hours = business.get('hours', 'None')
    
    if is_open_after_6pm(hours):
        if gmap_id in business_avg_ratings:
            results.append({
                'name': business['name'],
                'gmap_id': gmap_id,
                'hours': hours,
                'avg_rating': business_avg_ratings[gmap_id]['avg_rating'],
                'review_count': business_avg_ratings[gmap_id]['review_count']
            })

# Sort by average rating (descending) and get top 5
top_5 = sorted(results, key=lambda x: x['avg_rating'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.query_db:0': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.list_db:6': ['review'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
