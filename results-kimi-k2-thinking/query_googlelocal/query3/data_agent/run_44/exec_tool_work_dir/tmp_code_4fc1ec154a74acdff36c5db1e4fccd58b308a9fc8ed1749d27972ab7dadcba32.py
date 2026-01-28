code = """import json
import pandas as pd
from datetime import datetime

# Load business data
business_data_file = locals()['var_functions.query_db:10']
if isinstance(business_data_file, str) and business_data_file.endswith('.json'):
    with open(business_data_file, 'r') as f:
        business_data = json.load(f)
else:
    business_data = locals()['var_functions.query_db:10']

# Load review data
review_data_file = locals()['var_functions.query_db:12']
if isinstance(review_data_file, str) and review_data_file.endswith('.json'):
    with open(review_data_file, 'r') as f:
        review_data = json.load(f)
else:
    review_data = locals()['var_functions.query_db:12']

print('Businesses loaded:', len(business_data))
print('Reviews loaded:', len(review_data))

# Function to parse closing time
def parse_closing_time(time_str):
    if not time_str or time_str == 'Closed':
        return None
    if '24 hours' in time_str:
        return 24 * 60  # 24:00 in minutes
    
    # Handle formats like "6:30AM–6PM" or "6PM"
    try:
        time_part = time_str.split('–')[-1] if '–' in time_str else time_str
        time_part = time_part.strip()
        
        # Handle midnight
        if time_part == '12AM':
            return 0
        
        if ':' in time_part:
            if 'PM' in time_part:
                hour = int(time_part.split(':')[0])
                minute = int(time_part.split(':')[1].replace('PM', ''))
                if hour != 12:
                    hour += 12
                return hour * 60 + minute
            else:  # AM
                hour = int(time_part.split(':')[0])
                minute = int(time_part.split(':')[1].replace('AM', ''))
                return hour * 60 + minute
        else:
            if 'PM' in time_part:
                hour = int(time_part.replace('PM', ''))
                if hour != 12:
                    hour += 12
                return hour * 60
            else:  # AM
                hour = int(time_part.replace('AM', ''))
                return hour * 60
    except:
        return None

# Function to check if business is open after 6PM on weekdays
def check_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = json.loads(hours_str) if isinstance(hours_str, str) else hours_str
        
        for day_info in hours_list:
            if len(day_info) >= 2:
                day, hours = day_info[0], day_info[1]
                
                # Only check weekdays (Monday-Friday)
                if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
                    closing_minutes = parse_closing_time(str(hours))
                    # 6:00 PM = 18:00 = 1080 minutes
                    if closing_minutes is not None and closing_minutes > 1080:
                        return True
        return False
    except:
        return False

# Check which businesses meet criteria
open_businesses = []
for business in business_data:
    if check_open_after_6pm(business['hours']):
        open_businesses.append(business)

print(f'Businesses open after 6PM on weekdays: {len(open_businesses)}')

# Show sample businesses
for i, business in enumerate(open_businesses[:5]):
    print(f"{i+1}. {business['name']}: {business['hours']}")

# Calculate average ratings
rating_df = pd.DataFrame(review_data)
rating_df['rating'] = pd.to_numeric(rating_df['rating'])
average_ratings = rating_df.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
average_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

print(f'\nBusinesses with average ratings: {len(average_ratings)}')

# Join with businesses
business_df = pd.DataFrame(business_data)
merged = pd.merge(business_df, average_ratings, on='gmap_id')

# Filter businesses open after 6PM
filtered = merged[merged['hours'].apply(check_open_after_6pm)]

print(f'Businesses meeting all criteria: {len(filtered)}')

# Sort by average rating and get top 5
top_5 = filtered.sort_values('avg_rating', ascending=False).head(5)

print('\nTop 5 businesses:')
for idx, row in top_5.iterrows():
    print(f"{row['name']}: {row['avg_rating']:.2f}, reviews: {row['review_count']}, hours: {row['hours']}")

# Format results for output
result = []
for idx, row in top_5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(float(row['avg_rating']), 2),
        'review_count': int(row['review_count'])
    })

result_json = json.dumps(result, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': ['Total businesses: 79', '', 'First business hours field: None', "Type: <class 'str'>", '', 'Second business:', 'Name: San Soo Dang', 'Hours: [["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', '', "Type of second business hours: <class 'str'>", 'Successfully parsed JSON', "Parsed type: <class 'list'>", "First 2 days: [['Thursday', '6:30AM–6PM'], ['Friday', '6:30AM–6PM']]"], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
