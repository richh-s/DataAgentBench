code = """import json
import pandas as pd
import re
from datetime import datetime

# Load business data
business_file_path = var_functions.query_db:12
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses with hours:', len(businesses))
print('First business:', businesses[0])

# Load review data to get ratings
review_file_path = var_functions.query_db:14
with open(review_file_path, 'r') as f:
    reviews = json.load(f)

print('Total reviews:', len(reviews))

# Let's process the hours and filter businesses that are open after 6PM (18:00) on at least one weekday
timezone_aware = False  # Assuming times are not timezone-aware based on the format

# Function to parse time

def parse_time(time_str):
    '''Parse time string in formats like "6:30PM" or "6PM" or "6:30 AM"'''
    time_str = time_str.strip().replace(' ', '')
    if '.' in time_str:
        time_str = time_str.replace('.', '')
    # Extract AM/PM
    if 'PM' in time_str:
        base = time_str.replace('PM', '')
        is_pm = True
    elif 'AM' in time_str:
        base = time_str.replace('AM', '')
        is_pm = False
    else:
        # No AM/PM, assume PM if evening hours
        base = time_str
        is_pm = False
    
    # Parse hour and minute
    if ':' in base:
        hour_str, minute_str = base.split(':')
        hour = int(hour_str)
        minute = int(minute_str)
    else:
        hour = int(base)
        minute = 0
    
    # Convert to 24-hour format
    if is_pm and hour != 12:
        hour += 12
    if not is_pm and hour == 12:
        hour = 0
    
    return hour + minute/60

# Function to check if business is open after 6PM on any weekday
# Weekdays: Monday, Tuesday, Wednesday, Thursday, Friday
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def is_open_after_6pm(hours_str):
    '''Check if business is open after 6PM on any weekday'''
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string into a list
        hours_list = eval(hours_str)
        
        for day, hours_range in hours_list:
            if day not in weekdays:
                continue
                
            if hours_range in ['Closed', 'Open 24 hours']:
                if hours_range == 'Open 24 hours':
                    return True
                continue
            
            # Parse time range like "11AM–9:30PM"
            if '–' in hours_range:
                start_str, end_str = hours_range.split('–')
                end_time = parse_time(end_str)
                
                # Check if end time is after 6PM (18:00)
                if end_time > 18:  # After 6PM
                    return True
                    
    except Exception as e:
        return False
    
    return False

# Create a mapping from gmap_id to business info
business_dict = {biz['gmap_id']: biz for biz in businesses}

# Filter businesses that are open after 6PM
eligible_businesses = []
for business in businesses:
    if is_open_after_6pm(business['hours']):
        eligible_businesses.append(business)

print('Businesses open after 6PM:', len(eligible_businesses))

# Get ratings for eligible businesses
gmap_ids = [biz['gmap_id'] for biz in eligible_businesses]

# Create review DataFrame and calculate average ratings
review_df = pd.DataFrame(reviews)
print('Review columns:', review_df.columns.tolist())
print('Sample review data:', review_df.head())

# Calculate average rating per business
avg_ratings = review_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

# Filter for our eligible businesses
eligible_ratings = avg_ratings[avg_ratings['gmap_id'].isin(gmap_ids)]

print('Eligible businesses with ratings:', len(eligible_ratings))
print('Sample eligible ratings:', eligible_ratings.head())

# Merge with business data to get names and hours
result_df = eligible_ratings.merge(
    pd.DataFrame(eligible_businesses)[['gmap_id', 'name', 'hours']], 
    on='gmap_id', 
    how='left'
)

# Sort by average rating descending and take top 5
top_5 = result_df.sort_values('avg_rating', ascending=False).head(5)

print('Top 5 businesses:')
for idx, row in top_5.iterrows():
    print(f"{row['name']}: Rating {row['avg_rating']:.2f}, Hours: {row['hours'][:100]}...")

# Format final result
final_result = []
for idx, row in top_5.iterrows():
    final_result.append({
        'name': row['name'],
        'avg_rating': round(row['avg_rating'], 2),
        'hours': row['hours']
    })

print('Final result:', json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
