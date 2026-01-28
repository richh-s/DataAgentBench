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

def parse_closing_time(hours_str):
    # Clean up unicode issues
    hours_str = hours_str.replace('\u2013', '-').replace('\u20132', '2').replace('\u20139', '9')
    
    # Extract closing time (after dash)
    if '-' in hours_str:
        closing_part = hours_str.split('-')[1].strip()
        
        # Parse time like "9:30PM"
        match = re.match(r'(\d{1,2})(:(\d{2}))?(AM|PM)', closing_part, re.IGNORECASE)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(3)) if match.group(3) else 0
            period = match.group(4).upper()
            
            # Convert to 24-hour format
            if period == 'PM' and hour != 12:
                hour += 12
            elif period == 'AM' and hour == 12:
                hour = 0
                
            return hour + minute/60.0
    return None

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # The hours field is JSON string, parse it
        hours_data = json.loads(hours_str)
        
        for day_entry in hours_data:
            day = day_entry[0]
            hours = day_entry[1]
            
            # Check weekdays only
            if day in weekdays and hours != 'Closed':
                closing_time = parse_closing_time(hours)
                if closing_time is not None and closing_time >= 18.0:  # 6 PM or later
                    return True
    except Exception as e:
        pass
    
    return False

# Test on specific businesses that should qualify
test_businesses = [
    '["Thursday", "11AM\u20139:30PM"]',
    '["Thursday", "9:30AM\u20139:30PM"]'
]

print('Testing parse_closing_time:')
for test in test_businesses:
    result = parse_closing_time(test)
    print(f"  {test} -> {result}")

print('Testing is_open_after_6pm on a specific business hours:')
test_hours = '[["Thursday", "11AM\u20139:30PM"], ["Friday", "11AM\u20139:30PM"]]'
print(f"  Result: {is_open_after_6pm(test_hours)}")

# Now process all businesses
eligible_businesses = []
businesses_by_id = {}

for business in businesses:
    if business['hours'] and business['hours'] != 'None':
        if is_open_after_6pm(business['hours']):
            eligible_businesses.append(business['gmap_id'])
            businesses_by_id[business['gmap_id']] = {
                'name': business['name'],
                'hours': business['hours']
            }

# Calculate average ratings
ratings_by_business = defaultdict(list)

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id in eligible_businesses:
        ratings_by_business[gmap_id].append(rating)

# Calculate averages and sort
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
    'eligible_businesses': len(business_averages),
    'top_5': business_averages[:5]
}))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 66, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}, 'var_functions.execute_python:8': {'total_businesses': 66, 'eligible_businesses': 28, 'sample_eligible': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'business_count': 66, 'review_count': 665, 'review_sample': [{'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}]}, 'var_functions.execute_python:14': {'eligible_count': 0, 'with_reviews': 0, 'top_5': [], 'all_ranked': []}, 'var_functions.execute_python:16': {'total_businesses': 66, 'eligible_count': 0, 'eligible_sample': []}, 'var_functions.execute_python:18': {'status': 'debug complete'}, 'var_functions.execute_python:24': [{'name': 'Vons Chicken', 'hours_raw': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'name': 'Angel-A Massage', 'hours_raw': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}

exec(code, env_args)
