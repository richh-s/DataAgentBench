code = """import json
import re
import ast
from collections import defaultdict

# Load data
business_data_path = locals()['var_functions.query_db:20']
review_data_path = locals()['var_functions.query_db:11']

with open(business_data_path, 'r') as f:
    businesses = json.load(f)

with open(review_data_path, 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
ratings_by_business = defaultdict(list)
for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    ratings_by_business[gmap_id].append(rating)

avg_ratings = {}
for gmap_id, ratings in ratings_by_business.items():
    avg_ratings[gmap_id] = sum(ratings) / len(ratings)

# Parse closing time

def get_closing_time(time_str):
    if not time_str or time_str == "None":
        return None
    
    # Pattern to match times like "6:30PM", "10PM", "9:30PM"
    pattern = r'(\d{1,2})(?::(\d{2}))?\s*([AP]M)'
    matches = re.findall(pattern, time_str, re.IGNORECASE)
    
    if matches:
        hour, minute, period = matches[0]
        hour = int(hour)
        minute = int(minute) if minute else 0
        
        if period.upper() == 'PM' and hour != 12:
            hour += 12
        elif period.upper() == 'AM' and hour == 12:
            hour = 0
            
        return hour + minute/60.0
    
    return None

# Check if open after 6 PM on any weekday

def check_open_after_6pm(hours_str, state_str):
    if not hours_str or hours_str == "None":
        return False
    
    # Parse hours list string
    if hours_str.startswith('[['):
        try:
            hours_list = ast.literal_eval(hours_str)
            for day_entry in hours_list:
                if len(day_entry) >= 2:
                    day = day_entry[0]
                    hours_range = day_entry[1]
                    
                    # Skip weekends
                    if day in ['Saturday', 'Sunday']:
                        continue
                    
                    # Get closing time
                    closing = get_closing_time(hours_range)
                    if closing is not None and closing > 18.0:  # After 6 PM
                        return True
        except:
            pass
    
    # Check state field for closing times
    if state_str and isinstance(state_str, str):
        if 'Closes' in state_str:
            closing = get_closing_time(state_str)
            if closing is not None and closing > 18.0:
                return True
        elif 'Open 24 hours' in state_str:
            return True
    
    return False

# Find eligible businesses
eligible = []
for business in businesses:
    gmap_id = business['gmap_id']
    name = business['name']
    hours = business.get('hours', 'None')
    state = business.get('state', '')
    
    if gmap_id in avg_ratings and check_open_after_6pm(hours, state):
        eligible.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours,
            'avg_rating': round(avg_ratings[gmap_id], 2),
            'review_count': len(ratings_by_business[gmap_id])
        })

# Sort by avg_rating (highest first), then by review_count
top_5 = sorted(eligible, key=lambda x: (x['avg_rating'], x['review_count']), reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['business_description'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.query_db:10': [], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'state': 'Open ⋅ Closes 9:30PM'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None', 'state': 'None'}], 'var_functions.execute_python:18': {'businesses_count': 10, 'reviews_count': 2000, 'sample_business': {'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:24': {'businesses_loaded': 79, 'reviews_loaded': 2000}, 'var_functions.execute_python:26': [{'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM', 'avg_rating': 5.0, 'review_count': 6}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'state': 'Open ⋅ Closes 7PM', 'avg_rating': 5.0, 'review_count': 18}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'state': 'Open ⋅ Closes 8PM', 'avg_rating': 5.0, 'review_count': 8}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'state': 'Open ⋅ Closes 9PM', 'avg_rating': 5.0, 'review_count': 2}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'state': 'Closed ⋅ Opens 5PM Fri', 'avg_rating': 5.0, 'review_count': 2}], 'var_functions.execute_python:28': {'businesses_total': 79, 'reviews_total': 2000}}

exec(code, env_args)
