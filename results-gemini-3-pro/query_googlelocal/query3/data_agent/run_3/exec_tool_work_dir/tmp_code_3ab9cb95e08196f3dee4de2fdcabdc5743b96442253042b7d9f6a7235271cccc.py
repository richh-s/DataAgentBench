code = """import json
import ast
import pandas as pd
from datetime import datetime

# Load data
with open('var_function-call-7871304986794142237.json', 'r') as f:
    businesses = json.load(f)

with open('var_function-call-7871304986794139884.json', 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

# Helper to parse time
def parse_time(t_str):
    # Returns 24-hour hour and minute
    # t_str like "6PM", "9:30PM", "12AM", "12PM", "12:30PM"
    t_str = t_str.strip()
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    # Remove AM/PM
    time_part = t_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in time_part:
        h, m = map(int, time_part.split(':'))
    else:
        h = int(time_part)
        m = 0
        
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h, m

def is_later_than_6pm(closing_time_str):
    # Parses closing time and checks if > 18:00
    # Returns True if closing time is later than 18:00 (6 PM)
    # Handles "Open 24 hours" logic outside this or treats specially? 
    # This function expects "6PM", "9:30PM" etc.
    try:
        h, m = parse_time(closing_time_str)
        
        # If closing time is early AM (e.g., 1AM, 2AM), it means it stays open past midnight, so definitely past 6PM.
        # "After 6PM" means covering the range 6PM+.
        # If it closes at 00:00 (12AM), it is > 18:00.
        # If it closes at 01:00, etc. it is > 18:00.
        # If it closes at 12:00 (Noon), No.
        # If it closes at 17:00 (5PM), No.
        # If it closes at 18:00 (6PM), No (assumed "after" means >).
        
        # Logic:
        # 0 <= h < 12 (AM times except 12AM is 0) -> Open past midnight -> True
        # h == 12 (12 PM / Noon) -> False
        # 12 < h <= 18 (1 PM to 6 PM) -> False
        # h > 18 (6:01 PM to 11 PM) -> True
        
        if 0 <= h < 10: # Early morning hours (12AM - 9AM) usually mean open late. 
                        # Assuming businesses don't close at 9AM unless they are breakfast only (closing after 6PM previous day? No, hours list represents the day's hours).
                        # Hours usually: "9AM-5PM".
                        # If "5PM-2AM", closing is 2AM.
                        # If "6PM-6AM", closing is 6AM.
            return True
        if h > 18:
            return True
        if h == 18 and m > 0:
            return True
            
        return False
    except:
        return False

filtered_businesses = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for b in businesses:
    hours_raw = b.get('hours')
    gmap_id = b.get('gmap_id')
    name = b.get('name')
    
    if not hours_raw or hours_raw == 'None':
        continue
        
    try:
        # Try JSON load first
        hours_list = json.loads(hours_raw)
    except:
        try:
            hours_list = ast.literal_eval(hours_raw)
        except:
            continue
            
    # Check if open after 6PM on a weekday
    open_late = False
    
    for day_hours in hours_list:
        day_name = day_hours[0]
        time_range = day_hours[1]
        
        if day_name in weekdays:
            if time_range == "Open 24 hours":
                open_late = True
                break
            if time_range == "Closed":
                continue
                
            # Split range
            # Separators can be – (\u2013) or -
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) == 2:
                closing_time = parts[1]
                if is_later_than_6pm(closing_time):
                    open_late = True
                    break
    
    if open_late:
        avg_rating = avg_ratings.get(gmap_id, 0) # Default 0 if no rating, but we should probably ignore? Or keep? Prompt says rank by highest avg rating.
        # If no reviews, avg is usually undefined. The prompt implies businesses *have* ratings.
        if gmap_id in avg_ratings:
            filtered_businesses.append({
                "name": name,
                "hours": hours_raw,
                "average_rating": avg_rating
            })

# Sort
filtered_businesses.sort(key=lambda x: x['average_rating'], reverse=True)

# Top 5
top_5 = filtered_businesses[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16436364067953727415': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-8801674003676599702': [{'count': '79'}], 'var_function-call-8801674003676598901': [{'COUNT(*)': '2000'}], 'var_function-call-7871304986794142237': 'file_storage/function-call-7871304986794142237.json', 'var_function-call-7871304986794139884': 'file_storage/function-call-7871304986794139884.json'}

exec(code, env_args)
