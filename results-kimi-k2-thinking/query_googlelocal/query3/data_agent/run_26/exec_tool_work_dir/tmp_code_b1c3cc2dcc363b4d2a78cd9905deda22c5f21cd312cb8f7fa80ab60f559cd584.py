code = """import json
import re
from collections import defaultdict

# Load business data
business_file = locals()['var_functions.query_db:2']
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Load review data
review_file = locals()['var_functions.query_db:10']
with open(review_file, 'r') as f:
    reviews = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def parse_time(time_str):
    time_str = time_str.replace('\u2013', '-')
    
    if 'AM' in time_str or 'PM' in time_str:
        match = re.match(r'(\d{1,2})(:(\d{2}))?(AM|PM)', time_str, re.IGNORECASE)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(3)) if match.group(3) else 0
            period = match.group(4).upper()
            
            if period == 'PM' and hour != 12:
                hour += 12
            elif period == 'AM' and hour == 12:
                hour = 0
                
            return hour + minute/60.0
    return None

def is_open_after_6pm(hours_list):
    try:
        hours_data = json.loads(hours_list)
        
        for day_entry in hours_data:
            day = day_entry[0]
            hours = day_entry[1]
            
            if day in weekdays and hours != 'Closed':
                if '-' in hours:
                    closing_time = hours.split('-')[1].strip()
                    closing_hour = parse_time(closing_time)
                    
                    if closing_hour is not None and closing_hour >= 18.0:
                        return True
    except:
        pass
    
    return False

# Get business gmap_ids
eligible_business_ids = []
businesses_by_id = {}

for business in businesses:
    if business['hours'] and business['hours'] != 'None' and is_open_after_6pm(business['hours']):
        eligible_business_ids.append(business['gmap_id'])
        businesses_by_id[business['gmap_id']] = {
            'name': business['name'],
            'hours': business['hours']
        }

# Calculate average ratings
ratings_by_business = defaultdict(list)

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id in eligible_business_ids:
        ratings_by_business[gmap_id].append(rating)

# Calculate averages
business_averages = []
for gmap_id, ratings in ratings_by_business.items():
    if len(ratings) >= 1:  # At least one review
        avg_rating = sum(ratings) / len(ratings)
        business_averages.append({
            'gmap_id': gmap_id,
            'name': businesses_by_id[gmap_id]['name'],
            'hours': businesses_by_id[gmap_id]['hours'],
            'avg_rating': round(avg_rating, 2),
            'num_reviews': len(ratings)
        })

# Sort by average rating descending
business_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'eligible_count': len(eligible_business_ids),
    'with_reviews': len(business_averages),
    'top_5': business_averages[:5],
    'all_ranked': business_averages
}))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 66, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}, 'var_functions.execute_python:8': {'total_businesses': 66, 'eligible_businesses': 28, 'sample_eligible': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'business_count': 66, 'review_count': 665, 'review_sample': [{'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}]}}

exec(code, env_args)
