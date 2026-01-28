code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
business_file = locals()['var_functions.query_db:6']
review_file = locals()['var_functions.query_db:8']

with open(business_file, 'r') as f:
    businesses = json.load(f)

with open(review_file, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_business = pd.DataFrame(businesses)
df_reviews = pd.DataFrame(reviews)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
df_avg_rating = df_reviews.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
df_avg_rating.columns = ['gmap_id', 'avg_rating', 'review_count']

# Function to parse time string and check if after 6 PM
def is_after_6pm(time_str):
    """Check if a closing time is after 6:00 PM"""
    if time_str in ['Closed', 'Open 24 hours']:
        return False
    
    # Handle formats like "9:30PM", "10PM", "12AM", etc.
    time_str = time_str.strip()
    
    # Remove any non-ASCII characters and replace with ASCII equivalent
    time_str = time_str.replace('\u2013', '-').replace('\u2014', '-').replace('\u2212', '-')
    
    # Extract the time part (after hyphen if exists)
    if '-' in time_str:
        time_str = time_str.split('-')[1].strip()
    
    # Parse time
    try:
        if ':' in time_str:
            # Format: "9:30PM"
            time_obj = datetime.strptime(time_str, '%I:%M%p')
        else:
            # Format: "10PM"
            time_obj = datetime.strptime(time_str, '%I%p')
        
        # Check if hour >= 18 (6 PM) or if it's PM and hour != 12
        if time_obj.hour >= 18:
            return True
        elif time_obj.hour < 12 and 'PM' in time_str.upper():
            return True
        return False
    except:
        return False

# Function to check if business is open after 6 PM on any weekday
def check_open_after_6pm(hours_str):
    """Check if business is open after 6 PM on any weekday"""
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the string representation of list
        hours_list = eval(hours_str)
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day, hours in hours_list:
            if day in weekdays:
                if is_after_6pm(hours):
                    return True
        return False
    except:
        return False

# Apply the function to filter businesses
df_business['open_after_6pm'] = df_business['hours'].apply(check_open_after_6pm)

# Filter businesses that are open after 6 PM
open_businesses = df_business[df_business['open_after_6pm'] == True]

# Merge with average ratings
df_merged = open_businesses.merge(df_avg_rating, on='gmap_id', how='inner')

# Sort by average rating (descending) and get top 5
top_5 = df_merged.sort_values('avg_rating', ascending=False).head(5)

# Prepare result
result = []
for _, row in top_5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(row['avg_rating'], 2),
        'review_count': row['review_count']
    })

result_json = json.dumps(result, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': 'Total businesses: 66, Total reviews: 2000'}

exec(code, env_args)
