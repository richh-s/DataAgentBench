code = """import json
import re
from collections import defaultdict
import datetime

# Load business data
business_data_path = locals()['var_functions.query_db:20']
with open(business_data_path, 'r') as f:
    businesses = json.load(f)

# Load review data
review_data_path = locals()['var_functions.query_db:11']
with open(review_data_path, 'r') as f:
    reviews = json.load(f)

# Calculate average ratings per business
ratings_by_business = defaultdict(list)
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    ratings_by_business[gmap_id].append(rating)

avg_ratings = {}
for gmap_id, ratings in ratings_by_business.items():
    avg_ratings[gmap_id] = sum(ratings) / len(ratings)

# Function to parse closing time from hours string
def parse_closing_time(time_str):
    if not time_str or time_str == "None":
        return None
    
    # Look for patterns like "6PM", "9:30PM", "10PM", etc.
    patterns = [
        r'(\d{1,2}):?(\d{2})?\s*([APMapm]{2})',
        r'Closes\s+(\d{1,2}):?(\d{2})?\s*([APMapm]{2})'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, time_str)
        if matches:
            hour, minute, period = matches[0]
            hour = int(hour)
            minute = int(minute) if minute else 0
            
            if period.lower() == 'pm' and hour != 12:
                hour += 12
            elif period.lower() == 'am' and hour == 12:
                hour = 0
                
            return hour + minute/60
    
    return None

# Function to check if business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    
    # Check if hours is a string representation of a list
    if hours_str.startswith('[['):
        try:
            hours_list = eval(hours_str)
            for day_hours in hours_list:
                if len(day_hours) >= 2:
                    day = day_hours[0]
                    hours = day_hours[1]
                    
                    # Skip weekend days
                    if day in ['Saturday', 'Sunday']:
                        continue
                    
                    # Parse closing time
                    closing_time = parse_closing_time(hours)
                    if closing_time and closing_time >= 18:  # 6 PM = 18:00
                        return True
        except:
            pass
    
    # Also check state field for closing times
    return False

# Find businesses open after 6 PM
eligible_businesses = []
for business in businesses:
    gmap_id = business['gmap_id']
    hours = business.get('hours', 'None')
    state = business.get('state', '')
    
    # Check from hours field
    if is_open_after_6pm(hours):
        eligible_businesses.append(business)
    # Check from state field as backup
    elif state and any(x in state for x in ['Closes 6', 'Closes 7', 'Closes 8', 'Closes 9', 'Closes 10', 'Closes 11', 'Open 24']):
        eligible_businesses.append(business)

# Filter businesses that have ratings
rated_businesses = []
for business in eligible_businesses:
    gmap_id = business['gmap_id']
    if gmap_id in avg_ratings:
        rated_businesses.append({
            'gmap_id': gmap_id,
            'name': business['name'],
            'hours': business['hours'],
            'state': business.get('state', ''),
            'avg_rating': avg_ratings[gmap_id],
            'review_count': len(ratings_by_business[gmap_id])
        })

# Sort by average rating (descending) and get top 5
top_5 = sorted(rated_businesses, key=lambda x: x['avg_rating'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['business_description'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.query_db:10': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None', 'state': 'None'}], 'var_functions.execute_python:18': {'businesses_count': 10, 'reviews_count': 2000, 'sample_business': {'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'businesses_loaded': 79, 'reviews_loaded': 2000}}

exec(code, env_args)
