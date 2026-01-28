code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the business data from file
with open('/tmp/20250320-091853-json-gbjq.json', 'r') as f:
    business_data = json.load(f)

# Read the review data from file
with open('/tmp/20250320-091920-json-5y9y.json', 'r') as f:
    review_data = json.load(f)

# Create DataFrames
df_business = pd.DataFrame(business_data)
df_reviews = pd.DataFrame(review_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating']

# Merge business with average ratings
df_business_with_ratings = df_business.merge(avg_ratings, on='gmap_id', how='left')

# Filter businesses with hours information
df_valid_hours = df_business_with_ratings[df_business_with_ratings['hours'].notna() & 
                                           (df_business_with_ratings['hours'] != 'None')].copy()

print(f"Total businesses with valid hours: {len(df_valid_hours)}")
print(f"Sample hours entry: {df_valid_hours['hours'].iloc[0]}")

# Define function to parse hours and check if open after 6 PM on any weekday
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def is_open_after_6pm(hours_str):
    """Check if business is open after 6 PM on at least one weekday"""
    try:
        if not hours_str or hours_str == 'None':
            return False
        
        # Parse the hour string (it's stored as a string representation of a list)
        hours_list = eval(hours_str.replace('\u2013', '-'))
        
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed' and 'Closed' not in str(hours):
                # Extract closing time
                # Handle formats like "11AM-9:30PM", "9:30AM-10PM", "Open 24 hours"
                if 'Open 24 hours' in str(hours):
                    return True
                
                # Split by dash or endash
                time_parts = re.split(r'[-\u2013]', hours)
                if len(time_parts) >= 2:
                    closing_time = time_parts[1].strip()
                    
                    # Parse closing time to 24-hour format
                    closing_hour = None
                    closing_time = closing_time.upper()
                    
                    if 'PM' in closing_time:
                        if ':' in closing_time:
                            hour_part = closing_time.replace('PM', '').strip()
                            hour, minute = map(int, hour_part.split(':'))
                            closing_hour = hour + 12 if hour != 12 else 12
                        else:
                            hour = int(closing_time.replace('PM', '').strip())
                            closing_hour = hour + 12 if hour != 12 else 12
                    elif 'AM' in closing_time:
                        if ':' in closing_time:
                            hour_part = closing_time.replace('AM', '').strip()
                            hour, minute = map(int, hour_part.split(':'))
                            closing_hour = hour if hour != 12 else 0
                        else:
                            hour = int(closing_time.replace('AM', '').strip())
                            closing_hour = hour if hour != 12 else 0
                    
                    if closing_hour is not None and closing_hour >= 18:
                        return True
        
        return False
    except Exception as e:
        print(f"Error parsing hours: {hours_str}, Error: {e}")
        return False

# Apply the function to check which businesses are open after 6 PM
df_valid_hours['open_after_6pm'] = df_valid_hours['hours'].apply(is_open_after_6pm)

# Filter businesses open after 6 PM
open_after_6pm = df_valid_hours[df_valid_hours['open_after_6pm'] == True]

print(f"Businesses open after 6 PM on weekdays: {len(open_after_6pm)}")
print("\nSample open businesses:")
print(open_after_6pm[['name', 'hours', 'avg_rating']].head())

# Sort by average rating (descending) and get top 5
top_5_businesses = open_after_6pm.sort_values('avg_rating', ascending=False).head(5)

print(f"\nTop 5 businesses:")
print(top_5_businesses[['name', 'hours', 'avg_rating']])

# Format the result
result = []
for _, row in top_5_businesses.iterrows():
    result.append({
        'name': row['name'],
        'operating_hours': row['hours'],
        'average_rating': round(row['avg_rating'], 2) if pd.notna(row['avg_rating']) else 'N/A'
    })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:8': [{'gmap_id': 'gmap_44', 'name': 'City Textile'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage'}, {'gmap_id': 'gmap_19', 'name': 'PODS Sacramento Hub'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage'}, {'gmap_id': 'gmap_48', 'name': 'State Street/7th Street'}, {'gmap_id': 'gmap_50', 'name': 'HDR'}, {'gmap_id': 'gmap_18', 'name': 'Porvene Doors'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
