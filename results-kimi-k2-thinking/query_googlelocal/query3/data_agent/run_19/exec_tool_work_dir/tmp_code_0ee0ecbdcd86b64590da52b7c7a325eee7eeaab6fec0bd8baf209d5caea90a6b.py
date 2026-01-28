code = """import json
import pandas as pd
import re
from datetime import datetime

# Load business data
business_file_path = var_functions.query_db:12
with open(business_file_path, 'r') as f:
    businesses = json.load(f)

print('Total businesses with hours:', len(businesses))

# Load review data
review_file_path = var_functions.query_db:16
with open(review_file_path, 'r') as f:
    reviews = json.load(f)

print('Total reviews:', len(reviews))

# Function to parse time and convert to decimal hours
def parse_time(time_str):
    '''Parse time string in formats like "6:30PM" or "6PM" '''
    if not time_str:
        return None
    
    time_str = time_str.strip().replace(' ', '')
    # Extract AM/PM
    is_pm = 'PM' in time_str
    time_str = time_str.replace('PM', '').replace('AM', '')
    
    # Parse hour and minute
    if ':' in time_str:
        hour_str, minute_str = time_str.split(':')
        hour = int(hour_str)
        minute = int(minute_str)
    else:
        hour = int(time_str)
        minute = 0
    
    # Convert to 24-hour format
    if is_pm and hour != 12:
        hour += 12
    if not is_pm and hour == 12:
        hour = 0
    
    return hour + minute/60

# Function to check if business is open after 6PM on any weekday
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}

def check_open_after_6pm(hours_str):
    '''Check if business is open after 6PM on any weekday'''
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string
        hours_list = eval(hours_str)
        
        for day_info in hours_list:
            if len(day_info) != 2:
                continue
            day, hours_range = day_info
            
            if day not in weekdays:
                continue
                
            if hours_range == 'Open 24 hours':
                return True
            if hours_range == 'Closed':
                continue
            
            # Parse time range
            if '–' in hours_range:
                end_str = hours_range.split('–')[1]
                end_time = parse_time(end_str)
                
                if end_time and end_time > 18:  # After 6PM
                    return True
                    
    except Exception as e:
        return False
    
    return False

# Filter businesses that are open after 6PM on at least one weekday
eligible_businesses = []
for business in businesses:
    if check_open_after_6pm(business['hours']):
        eligible_businesses.append(business)

print('Eligible businesses (open after 6PM):', len(eligible_businesses))

# Get gmap_ids of eligible businesses
eligible_gmap_ids = set(biz['gmap_id'] for biz in eligible_businesses)

# Calculate average ratings
review_df = pd.DataFrame(reviews)
review_df['rating'] = pd.to_numeric(review_df['rating'])

avg_ratings = review_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

# Filter for eligible businesses
eligible_ratings = avg_ratings[avg_ratings['gmap_id'].isin(eligible_gmap_ids)]

print('Eligible businesses with ratings:', len(eligible_ratings))

# Create business info dataframe
business_df = pd.DataFrame(eligible_businesses)[['gmap_id', 'name', 'hours']]

# Merge with ratings
result_df = eligible_ratings.merge(business_df, on='gmap_id', how='inner')

# Sort by average rating descending and take top 5
top_5_df = result_df.sort_values('avg_rating', ascending=False).head(5)

print('\nTop 5 businesses:')
for _, row in top_5_df.iterrows():
    print(f"{row['name']}: Rating {row['avg_rating']:.2f}")

# Prepare final result
final_result = []
for _, row in top_5_df.iterrows():
    final_result.append({
        'name': row['name'],
        'avg_rating': round(row['avg_rating'], 2),
        'hours': row['hours']
    })

# Print result in required format
print('\n__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
