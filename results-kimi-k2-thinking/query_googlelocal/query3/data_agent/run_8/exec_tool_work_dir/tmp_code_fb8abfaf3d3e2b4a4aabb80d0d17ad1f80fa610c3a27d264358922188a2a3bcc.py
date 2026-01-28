code = """import json
import re
from datetime import datetime

# Get business data
businesses = var_functions.query_db:28

# Get review data  
reviews = var_functions.query_db:26

# Calculate average rating per business
rating_sums = {}
rating_counts = {}

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id not in rating_sums:
        rating_sums[gmap_id] = 0
        rating_counts[gmap_id] = 0
    
    rating_sums[gmap_id] += rating
    rating_counts[gmap_id] += 1

# Calculate averages
avg_ratings = {}
for gmap_id in rating_sums:
    avg_ratings[gmap_id] = rating_sums[gmap_id] / rating_counts[gmap_id]

# Helper to parse time string to minutes since midnight
def time_to_minutes(time_str):
    time_str = time_str.strip().lower()
    time_str = time_str.replace('–', '-').replace('—', '-')
    
    # Handle formats like "9:30PM", "10PM", "12AM", "12PM"
    parts = time_str.split('-')
    if len(parts) != 2:
        return None
    
    close_time = parts[1].strip()
    
    # Handle 12-hour format
    if 'am' in close_time or 'pm' in close_time:
        try:
            time_part = close_time.replace('am', '').replace('pm', '').strip()
            if ':' in time_part:
                hours, minutes = map(int, time_part.split(':'))
            else:
                hours = int(time_part)
                minutes = 0
            
            is_pm = 'pm' in close_time
            
            # Convert to 24-hour
            if is_pm and hours != 12:
                hours += 12
            elif not is_pm and hours == 12:
                hours = 0
                
            return hours * 60 + minutes
        except:
            return None
    
    return None

# Helper to check if business is open after 6pm on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the string representation of nested arrays
        hours_list = eval(hours_str)
        
        # Check each day's hours
        for day_info in hours_list:
            if not isinstance(day_info, list) or len(day_info) != 2:
                continue
                
            day = day_info[0]
            hours = day_info[1]
            
            # Skip weekends
            if day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                continue
            
            # Skip if closed
            if hours == 'Closed':
                continue
                
            # Parse the time range
            minutes = time_to_minutes(hours)
            if minutes is None:
                continue
            
            # Check if closing time is after 6:00 PM (18:00 = 1080 minutes)
            if minutes > 18 * 60:
                return True
                
    except:
        return False
    
    return False

# Process businesses and filter
candidate_businesses = []

for business in businesses:
    gmap_id = business['gmap_id']
    name = business['name']
    hours_str = business['hours']
    state = business['state']
    
    # Check if open after 6pm on any weekday
    if not is_open_after_6pm(hours_str):
        continue
    
    # Get average rating
    avg_rating = avg_ratings.get(gmap_id, 0)
    review_count = rating_counts.get(gmap_id, 0)
    
    # Only include businesses with at least 5 reviews for reliability
    if review_count < 5:
        continue
    
    candidate_businesses.append({
        'name': name,
        'gmap_id': gmap_id,
        'hours': hours_str,
        'avg_rating': round(avg_rating, 2),
        'review_count': review_count
    })

# Sort by average rating descending
candidate_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = candidate_businesses[:5]

# Format result
result = []
for business in top_5:
    result.append({
        'name': business['name'],
        'operating_hours': business['hours'],
        'average_rating': business['avg_rating'],
        'review_count': business['review_count']
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'PODS Sacramento Hub', 'gmap_id': 'gmap_19', 'hours': 'None', 'state': 'Open now'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:20': [{'gmap_id': 'gmap_44'}, {'gmap_id': 'gmap_41'}, {'gmap_id': 'gmap_43'}, {'gmap_id': 'gmap_38'}, {'gmap_id': 'gmap_45'}, {'gmap_id': 'gmap_74'}, {'gmap_id': 'gmap_17'}, {'gmap_id': 'gmap_22'}, {'gmap_id': 'gmap_29'}, {'gmap_id': 'gmap_25'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
