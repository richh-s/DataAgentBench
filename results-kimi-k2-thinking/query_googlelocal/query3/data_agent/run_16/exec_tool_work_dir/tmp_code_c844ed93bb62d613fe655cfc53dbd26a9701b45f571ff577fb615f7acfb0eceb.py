code = """import json
import re
import ast
from collections import defaultdict

# Load all business data
business_file = locals()['var_functions.query_db:34']
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Load all review data
review_file = locals()['var_functions.query_db:42']
with open(review_file, 'r') as f:
    reviews = json.load(f)

# Step 1: Calculate average rating per business
ratings_by_business = defaultdict(list)
for review in reviews:
    gmap_id = review.get('gmap_id')
    rating = review.get('rating')
    if gmap_id and rating is not None:
        try:
            ratings_by_business[gmap_id].append(int(rating))
        except (ValueError, TypeError):
            pass

# Step 2: Parse hours string to list
def parse_hours_string(hours_str):
    if not hours_str or hours_str == 'None':
        return []
    try:
        return ast.literal_eval(hours_str)
    except:
        return []

# Step 3: Check if open after 6PM on weekdays
def is_open_after_6pm(hours_list):
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Open 24 hours':
                return True
            
            if '–' in time_range:
                times = time_range.split('–')
            elif '-' in time_range:
                times = time_range.split('-')
            else:
                continue
            
            if len(times) < 2:
                continue
            
            closing = times[1].strip()
            closing_hour = 0
            
            if 'PM' in closing:
                closing = closing.replace('PM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    if hour_part.isdigit():
                        hour = int(hour_part)
                        closing_hour = hour + 12 if hour != 12 else 12
                else:
                    hour_part = re.sub(r'[^0-9]', '', closing.strip()[:2])
                    if hour_part.isdigit():
                        hour = int(hour_part)
                        closing_hour = hour + 12 if hour != 12 else 12
            elif 'AM' in closing:
                closing = closing.replace('AM', '').strip()
                if ':' in closing:
                    hour_part = closing.split(':')[0]
                    if hour_part.isdigit():
                        hour = int(hour_part)
                        closing_hour = 0 if hour == 12 else hour
                else:
                    hour_part = re.sub(r'[^0-9]', '', closing.strip()[:2])
                    if hour_part.isdigit():
                        hour = int(hour_part)
                        closing_hour = 0 if hour == 12 else hour
            
            if closing_hour >= 18:
                return True
    
    return False

# Step 4: Find eligible businesses with ratings
eligible_businesses = []
for business in businesses:
    gmap_id = business.get('gmap_id')
    
    if gmap_id not in ratings_by_business:
        continue
    
    hours_str = business.get('hours', '')
    hours_list = parse_hours_string(hours_str)
    
    if is_open_after_6pm(hours_list):
        ratings = ratings_by_business[gmap_id]
        avg_rating = sum(ratings) / len(ratings)
        eligible_businesses.append({
            'name': business.get('name'),
            'hours': hours_str,
            'average_rating': round(avg_rating, 2),
            'review_count': len(ratings)
        })

# Step 5: Sort and get top 5
top_5 = sorted(eligible_businesses, key=lambda x: x['average_rating'], reverse=True)[:5]

print('__RESULT__:')
print(json.dumps(top_5))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:5': ['business_description'], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'count': 39}, 'var_functions.execute_python:24': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': [{'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'average_rating': 5.0, 'review_count': 6, 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'average_rating': 5.0, 'review_count': 18, 'state': 'Open ⋅ Closes 7PM'}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'average_rating': 5.0, 'review_count': 8, 'state': 'Open ⋅ Closes 8PM'}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'average_rating': 5.0, 'review_count': 2, 'state': 'Open ⋅ Closes 9PM'}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'average_rating': 5.0, 'review_count': 2, 'state': 'Closed ⋅ Opens 5PM Fri'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': [{'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'average_rating': 5.0, 'review_count': 2, 'state': 'Open ⋅ Closes 9PM'}, {'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'average_rating': 5.0, 'review_count': 6, 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'average_rating': 5.0, 'review_count': 8, 'state': 'Open ⋅ Closes 8PM'}, {'name': 'Dr. Syverain Skincare Clinic', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'average_rating': 5.0, 'review_count': 5, 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'average_rating': 5.0, 'review_count': 18, 'state': 'Open ⋅ Closes 7PM'}], 'var_functions.list_db:38': ['review'], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:46': {'status': 'success', 'business_count': 62, 'review_count': 2000}}

exec(code, env_args)
