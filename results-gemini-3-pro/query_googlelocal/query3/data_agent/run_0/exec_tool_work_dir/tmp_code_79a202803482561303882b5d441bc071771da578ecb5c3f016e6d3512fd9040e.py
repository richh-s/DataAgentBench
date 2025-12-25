code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-11402182038532519728.json', 'r') as f:
    businesses = json.load(f)

with open('var_function-call-14327882022513570432.json', 'r') as f:
    reviews = json.load(f)

# Create DataFrame for reviews and calculate average rating
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Helper function to parse time
def parse_time_to_minutes(time_str):
    # time_str formats: "6PM", "6:30AM", "12AM", "12:30PM"
    if not time_str:
        return None
    match = re.match(r"(\d+):?(\d+)?(AM|PM)", time_str)
    if not match:
        return None
    
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3)
    
    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0
        
    return hour * 60 + minute

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    
    try:
        hours_list = json.loads(hours_str)
    except:
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    target_time = 18 * 60 # 6:00 PM in minutes
    
    for day_info in hours_list:
        if len(day_info) != 2:
            continue
            
        day = day_info[0]
        time_range = day_info[1]
        
        if day in weekdays:
            if "Open 24 hours" in time_range:
                return True
            if "Closed" in time_range:
                continue
            
            # Split time range. En-dash or hyphen
            parts = re.split(r'\u2013|-', time_range)
            if len(parts) == 2:
                open_time = parts[0].strip()
                close_time = parts[1].strip()
                
                close_minutes = parse_time_to_minutes(close_time)
                
                if close_minutes is not None:
                    # Handle crossing midnight (e.g. 9PM-2AM)
                    # Ideally, if close_minutes < open_minutes, it's next day.
                    # But simpler check: if close_minutes > 18:00 (1080) OR close_minutes < open_minutes (assuming late night)
                    # Actually, we just need to know if it's open AFTER 6pm.
                    # If it closes at 7PM (19:00), 19*60 > 18*60. True.
                    # If it closes at 2AM (2:00), 2*60 = 120. 
                    # If open 5PM-2AM. Is it open after 6PM? Yes.
                    # If open 11AM-5PM. Closes 17:00. No.
                    
                    # Logic: 
                    # If close_minutes > target_time: Open after 6pm.
                    # If close_minutes < open_minutes (crosses midnight): Open after 6pm (since it stays open past midnight).
                    # Special case: 12AM (0 minutes). If treated as 0, 0 < 1080, but 0 < open (say 10AM), so it crosses midnight.
                    
                    # We need open_minutes to check crossing midnight properly?
                    # Or just:
                    # If period is PM and hour >= 6? No, 5:30PM is PM.
                    # If hour_24 > 18? Yes.
                    # If hour_24 < 12 (AM) (meaning it ends in the morning next day)? Yes.
                    
                    # Let's refine parse_time_to_minutes to return 0-1439.
                    
                    # Valid "after 6PM" conditions:
                    # 1. Close time is > 18:00 (1080 mins) and < 24:00.
                    # 2. Close time is in AM (0:00 to 11:59). This implies it went past midnight, so definitely past 6PM.
                    
                    if close_minutes > target_time:
                        return True
                    
                    # Check for AM closing times (next day)
                    # If original string had "AM" and it wasn't morning business only?
                    # E.g. 6AM-11AM. Close 11AM (660). Not > 1080.
                    # E.g. 6PM-2AM. Close 2AM (120). Not > 1080. But it IS open after 6PM.
                    # We need to distinguish 2AM (night) from 11AM (morning).
                    # Usually businesses open in morning. If close < open, it crosses midnight.
                    # Let's parse open time too.
                    
                    open_minutes = parse_time_to_minutes(open_time)
                    if open_minutes is not None:
                        if close_minutes < open_minutes:
                            # Crosses midnight
                            return True
                        
    return False

# Filter businesses
valid_businesses = []
for item in businesses:
    if is_open_after_6pm(item.get('hours')):
        valid_businesses.append(item)

df_valid_biz = pd.DataFrame(valid_businesses)

# Merge
if not df_valid_biz.empty:
    merged = pd.merge(df_valid_biz, avg_ratings, on='gmap_id', how='inner')
    # Sort
    merged.sort_values(by='avg_rating', ascending=False, inplace=True)
    top_5 = merged.head(5)
    result = top_5[['name', 'hours', 'avg_rating']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2037192531929361992': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-6515103259913690058': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_function-call-3505425497574083711': [{'count': '79'}], 'var_function-call-10316088510373851265': [{'COUNT(*)': '2000'}], 'var_function-call-11402182038532519728': 'file_storage/function-call-11402182038532519728.json', 'var_function-call-14327882022513570432': 'file_storage/function-call-14327882022513570432.json'}

exec(code, env_args)
