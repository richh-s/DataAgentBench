code = """import json
import ast
import re
from collections import defaultdict

# Read the full data
businesses_file = locals()['var_functions.query_db:6']
reviews_file = locals()['var_functions.query_db:14']

with open(businesses_file, 'r') as f:
    businesses = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Function to parse time and check if after 6 PM
def parse_time(time_str):
    """Parse a time string like '6:30PM', '9PM', '12AM' and return hour in 24h format"""
    time_str = time_str.strip()
    
    # Handle special cases
    if time_str in ['Closed', 'Open 24 hours']:
        return None
    
    # Extract AM/PM
    is_pm = 'PM' in time_str or 'pm' in time_str
    time_str = time_str.replace('PM', '').replace('AM', '').replace('pm', '').replace('am', '').strip()
    
    # Parse hours and minutes
    if ':' in time_str:
        hours, minutes = map(int, time_str.split(':'))
    else:
        hours = int(time_str)
        minutes = 0
    
    # Convert to 24-hour format
    if is_pm and hours != 12:
        hours += 12
    elif not is_pm and hours == 12:
        hours = 0
    
    return hours

# Function to check if business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    """Check if business is open after 6 PM on any weekday"""
    try:
        # Parse the hours string which is a Python literal
        hours_list = ast.literal_eval(hours_str)
        
        for day_hours in hours_list:
            if len(day_hours) != 2:
                continue
                
            day, time_range = day_hours
            
            # Only check weekdays (Monday-Friday)
            weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            if day not in weekday_list:
                continue
            
            # Check if closed
            if time_range == 'Closed':
                continue
            
            # Handle 24 hours
            if time_range == 'Open 24 hours':
                return True
            
            # Split time range - look for dash or unicode dash
            if '-' in time_range:
                times = time_range.split('-')
            elif '\u2013' in time_range:
                times = time_range.split('\u2013')
            elif '\u2014' in time_range:
                times = time_range.split('\u2014')
            else:
                continue
                
            if len(times) == 2:
                close_time = times[1].strip()
                close_hour = parse_time(close_time)
                if close_hour is not None and close_hour >= 18:  # 6 PM or later
                    return True
        
        return False
    except Exception as e:
        return False

# Calculate average ratings for each business
business_ratings = defaultdict(list)
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    business_ratings[gmap_id].append(rating)

# Calculate average ratings
avg_ratings = {}
for gmap_id, ratings in business_ratings.items():
    avg_ratings[gmap_id] = sum(ratings) / len(ratings)

# Filter businesses that are open after 6 PM on weekdays
eligible_businesses = []
for business in businesses:
    gmap_id = business['gmap_id']
    hours = business.get('hours')
    
    if not hours or hours == 'None' or hours == '':
        continue
    
    if is_open_after_6pm(hours) and gmap_id in avg_ratings:
        eligible_businesses.append({
            'gmap_id': gmap_id,
            'name': business['name'],
            'hours': hours,
            'avg_rating': round(avg_ratings[gmap_id], 2),
            'num_reviews': len(business_ratings[gmap_id])
        })

# Sort by average rating (descending)
eligible_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = eligible_businesses[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5_businesses': top_5,
    'total_eligible': len(eligible_businesses)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}], 'var_functions.query_db:10': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'businesses_count': 66, 'reviews_count': 2000, 'sample_business': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, 'sample_review': {'gmap_id': 'gmap_44', 'rating': '5'}}}

exec(code, env_args)
