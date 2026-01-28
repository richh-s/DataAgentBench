code = """import json
import re

# Read the data files
business_file_path = locals()['var_functions.query_db:10']
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

review_file_path = locals()['var_functions.query_db:12']
with open(review_file_path, 'r') as j:
    reviews = json.load(j)

# Function to check if a business is open after 6 PM on any weekday
def is_open_after_6pm(business):
    hours_str = business.get('hours', '')
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = eval(hours_str)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if len(day_info) != 2:
                continue
                
            day, hours = day_info
            if day not in weekdays:
                continue
                
            # Check if closed
            if hours.lower() == 'closed':
                continue
            
            # If open 24 hours, it's open after 6pm
            if '24 hours' in hours:
                return True
            
            # Parse time range
            # Split on the en-dash character
            time_parts = hours.split('\u2013')
            if len(time_parts) != 2:
                continue
            
            start_time, end_time = time_parts
            end_time = end_time.strip()
            
            # Check if PM and not 6PM exactly
            if 'PM' in end_time:
                # Extract hour part
                match = re.match(r'(\d{1,2}):?(\d{2})?\s*PM', end_time, re.IGNORECASE)
                if match:
                    hour = int(match.group(1))
                    minute_part = match.group(2)
                    minutes = int(minute_part) if minute_part else 0
                    
                    # Convert to 24-hour format for comparison
                    hour_24 = hour if hour == 12 else hour + 12
                    
                    # Check if after 6:00 PM (18:00)
                    if hour_24 > 18 or (hour_24 == 18 and minutes > 0):
                        return True
        
        return False
    except:
        return False

# Filter businesses that are open after 6 PM
evening_businesses = [b for b in businesses if is_open_after_6pm(b)]

# Calculate average ratings for each business
business_avg_ratings = {}
for business in evening_businesses:
    gmap_id = business['gmap_id']
    business_ratings = [int(r['rating']) for r in reviews if r['gmap_id'] == gmap_id]
    
    if business_ratings:
        avg_rating = sum(business_ratings) / len(business_ratings)
        business_avg_ratings[gmap_id] = {
            'name': business['name'],
            'hours': business['hours'],
            'avg_rating': round(avg_rating, 2),
            'review_count': len(business_ratings)
        }

# Sort by average rating descending and get top 5
sorted_businesses = sorted(business_avg_ratings.values(), 
                          key=lambda x: x['avg_rating'], 
                          reverse=True)

top_5 = sorted_businesses[:5]

# Convert to JSON for output
result_json = json.dumps(top_5, indent=2)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'num_of_reviews': '6'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'num_of_reviews': '18'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'num_of_reviews': '6'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:18': '66 businesses with hours, 2000 total reviews'}

exec(code, env_args)
