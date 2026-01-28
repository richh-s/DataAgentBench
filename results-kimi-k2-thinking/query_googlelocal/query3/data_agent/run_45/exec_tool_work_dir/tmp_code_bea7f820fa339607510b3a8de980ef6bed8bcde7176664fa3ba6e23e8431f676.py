code = """import json
import ast
from collections import defaultdict

# Read data files
businesses_file = locals()['var_functions.query_db:6']
reviews_file = locals()['var_functions.query_db:14']

with open(businesses_file, 'r') as f:
    businesses = json.load(f)

with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Function to parse time string and get hour
def get_hour(time_str):
    time_str = time_str.strip()
    if time_str in ['Closed', 'Open 24 hours']:
        return None
    
    is_pm = 'PM' in time_str or 'pm' in time_str
    time_str = time_str.replace('PM', '').replace('AM', '').replace('pm', '').replace('am', '').strip()
    
    if ':' in time_str:
        hours = int(time_str.split(':')[0])
    else:
        hours = int(time_str)
    
    if is_pm and hours != 12:
        hours = hours + 12
    elif not is_pm and hours == 12:
        hours = 0
    
    return hours

# Function to check if business is open after 6:00 PM (strictly after) on weekdays
def check_open_after_6pm(hours_str):
    try:
        hours_list = ast.literal_eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for entry in hours_list:
            if len(entry) != 2:
                continue
            
            day = entry[0]
            time_range = entry[1]
            
            if day not in weekdays:
                continue
            
            if time_range == 'Closed':
                continue
            
            if time_range == 'Open 24 hours':
                return True
            
            # Try different separators
            separator = None
            if '-' in time_range:
                separator = '-'
            elif u'\u2013' in time_range:
                separator = u'\u2013'
            elif u'\u2014' in time_range:
                separator = u'\u2014'
            
            if separator:
                times = time_range.split(separator)
                if len(times) == 2:
                    close_time = times[1].strip()
                    close_hour = get_hour(close_time)
                    # Strictly after 6:00 PM (hour > 18)
                    if close_hour is not None and close_hour > 18:
                        return True
        
        return False
    except:
        return False

# Calculate average ratings
business_ratings = defaultdict(list)
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    business_ratings[gmap_id].append(rating)

avg_ratings = {}
for gmap_id, ratings in business_ratings.items():
    if ratings:
        avg_ratings[gmap_id] = sum(ratings) / len(ratings)

# Find eligible businesses (strictly after 6 PM)
eligible = []
for business in businesses:
    gmap_id = business['gmap_id']
    hours = business.get('hours', '')
    
    if not hours or hours == 'None':
        continue
    
    if check_open_after_6pm(hours) and gmap_id in avg_ratings:
        eligible.append({
            'gmap_id': gmap_id,
            'name': business['name'],
            'hours': hours,
            'avg_rating': round(avg_ratings[gmap_id], 2),
            'num_reviews': len(business_ratings[gmap_id])
        })

# Sort by rating and get top 5
eligible.sort(key=lambda x: x['avg_rating'], reverse=True)
top5 = eligible[:5]

# Format hours for better display
def format_hours_display(hours_str):
    try:
        hours_list = ast.literal_eval(hours_str)
        formatted = []
        for day, hours in hours_list:
            formatted.append(f"{day}: {hours}")
        return "; ".join(formatted)
    except:
        return hours_str

# Add formatted hours
for business in top5:
    business['hours_display'] = format_hours_display(business['hours'])

result = {
    'top_5_businesses': top5,
    'total_eligible': len(eligible)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}], 'var_functions.query_db:10': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'businesses_count': 66, 'reviews_count': 2000, 'sample_business': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, 'sample_review': {'gmap_id': 'gmap_44', 'rating': '5'}}, 'var_functions.execute_python:24': {'top_5': [{'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'avg_rating': 5.0, 'num_reviews': 6}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'avg_rating': 5.0, 'num_reviews': 18}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'avg_rating': 5.0, 'num_reviews': 8}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'avg_rating': 5.0, 'num_reviews': 2}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'avg_rating': 5.0, 'num_reviews': 2}], 'total_eligible': 31}}

exec(code, env_args)
