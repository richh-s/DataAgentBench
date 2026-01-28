code = """import json
import re
from datetime import datetime

# Load business data
business_file_path = locals()['var_functions.query_db:18']
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

# Load review data
review_file_path = locals()['var_functions.query_db:10']
with open(review_file_path, 'r') as f:
    reviews = json.load(f)

print("Loaded data successfully")
print("Businesses count:", len(businesses))
print("Reviews count:", len(reviews))

# Function to parse closing time
def parse_closing_time(time_range):
    if not time_range or time_range == 'Closed':
        return None
    
    # Split on the en dash or hyphen
    parts = re.split('[\u2013\u2014-]', time_range)
    if len(parts) < 2:
        return None
    
    closing_part = parts[1].strip()
    
    # Handle 24-hour businesses
    if '24 hours' in time_range:
        return 24
    
    # Parse the closing time
    closing_part = closing_part.replace(' ', '').upper()
    
    try:
        if ':' in closing_part:
            time_str = closing_part
        else:
            time_str = closing_part
            
        # Standardize format
        if ':' not in time_str and ('AM' in time_str or 'PM' in time_str):
            time_str = time_str.replace('AM', ':00AM').replace('PM', ':00PM')
            
        # Parse time
        if ':' in time_str:
            time_obj = datetime.strptime(time_str, '%I:%M%p')
            return time_obj.hour
        else:
            return None
            
    except (ValueError, IndexError):
        return None

# Extract businesses open after 6 PM on weekdays
businesses_open_late = []

for business in businesses:
    gmap_id = business['gmap_id']
    name = business['name']
    hours_str = business['hours']
    state = business['state']
    
    # Skip businesses with 24 hours
    if '24 hours' in str(state):
        continue
    
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        # Parse the hours string
        hours_list = json.loads(hours_str)
        
        # Check each weekday
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        is_open_late = False
        
        for day, time_range in hours_list:
            if day in weekday_names:
                closing_hour = parse_closing_time(time_range)
                if closing_hour and closing_hour > 18:
                    is_open_late = True
                    break
        
        if is_open_late:
            businesses_open_late.append(business)
            
    except (json.JSONDecodeError, ValueError):
        continue

print("Businesses open late:", len(businesses_open_late))

# Calculate average ratings
from collections import defaultdict
ratings_by_business = defaultdict(list)

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    ratings_by_business[gmap_id].append(rating)

# Calculate averages
gmap_id_to_avg_rating = {}
for gmap_id, ratings in ratings_by_business.items():
    avg_rating = sum(ratings) / len(ratings)
    gmap_id_to_avg_rating[gmap_id] = avg_rating

# Filter businesses with reviews
businesses_with_ratings = []
for business in businesses_open_late:
    gmap_id = business['gmap_id']
    if gmap_id in gmap_id_to_avg_rating:
        business['avg_rating'] = gmap_id_to_avg_rating[gmap_id]
        business['num_reviews'] = len(ratings_by_business[gmap_id])
        businesses_with_ratings.append(business)

print("Businesses with ratings:", len(businesses_with_ratings))

# Sort and get top 5
top_5 = sorted(businesses_with_ratings, key=lambda x: x['avg_rating'], reverse=True)[:5]

# Prepare result
result = []
for business in top_5:
    result.append({
        'name': business['name'],
        'hours': business['hours'],
        'avg_rating': round(business['avg_rating'], 2),
        'num_reviews': business['num_reviews']
    })

# Print in required format
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
