code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3639795649981648571'], 'r') as f:
    businesses = json.load(f)

with open(locals()['var_function-call-1810228243877111124'], 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# Calculate average rating per gmap_id
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Merge ratings into businesses
df = pd.merge(df_biz, avg_ratings, on='gmap_id', how='left')

# Helper to parse time string
def parse_time_to_minutes(time_str):
    # time_str examples: "6:30AM", "6PM", "12PM", "12:30AM"
    if not time_str:
        return None
    
    match = re.match(r"(\d+)(?::(\d+))?\s*([AP]M)", time_str.upper())
    if not match:
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    ampm = match.group(3)
    
    if ampm == "PM" and h != 12:
        h += 12
    if ampm == "AM" and h == 12:
        h = 0
        
    return h * 60 + m

# Helper to check if open after 6 PM (18:00 -> 1080 minutes)
def is_open_after_6pm(hours_json):
    if not hours_json or hours_json == "None":
        return False
    
    try:
        # The string might be double serialized or just a string rep of a list
        # It looks like a string: "[[\"Day\", \"Time\"]]"
        hours_list = json.loads(hours_json)
    except Exception as e:
        # Fallback if it's not valid json
        return False
        
    if not isinstance(hours_list, list):
        return False
        
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    target_time = 18 * 60 # 18:00 -> 1080 minutes
    
    for day_info in hours_list:
        if not isinstance(day_info, list) or len(day_info) != 2:
            continue
            
        day_name = day_info[0]
        time_range = day_info[1]
        
        if day_name not in weekdays:
            continue
            
        if "Open 24 hours" in time_range:
            return True
            
        if "Closed" in time_range:
            continue
            
        # Split by unicode en-dash or hyphen
        # \u2013 is en-dash
        parts = re.split(r'[\u2013-]', time_range)
        if len(parts) != 2:
            # Maybe handled weirdly like "3PM-..."
            continue
            
        close_time_str = parts[1].strip()
        close_minutes = parse_time_to_minutes(close_time_str)
        
        if close_minutes is not None:
            # Special case: closing at "12AM" or "1AM" (next day) is > 18:00
            # My parser returns 0 for 12AM, 60 for 1AM.
            # If closing time is early morning, it means it's open past midnight, so definitely past 6PM.
            # So if close_minutes < open_minutes (say 9AM -> 540), it's next day.
            # But simpler check: if close_minutes > 1080 (18:00) OR close_minutes < some early hour (meaning next day).
            # "After 6:00 PM" means the closing time is later than 18:00.
            # If it closes at 00:00 (12AM), is that after 6PM? Yes.
            # If it closes at 17:00 (5PM), no.
            # If it closes at 18:00 (6PM), strictly after? No.
            
            # Logic:
            # If close_minutes > 1080: True
            # If close_minutes < 1080: 
            #   Could be next day (e.g. 1 AM). How to distinguish 1AM (late night) from 1AM (start)?
            #   Hours usually "Open-Close".
            #   If Open > Close, it spans midnight.
            #   Let's check "Open" time too.
            open_time_str = parts[0].strip()
            open_minutes = parse_time_to_minutes(open_time_str)
            
            if open_minutes is not None:
                if close_minutes < open_minutes:
                    # Spans midnight
                    # If it spans midnight, it is open at 23:59, which is after 18:00.
                    # Unless it opens at 4AM and closes at 5AM? Unlikely.
                    # Generally if spans midnight, it covers the evening.
                    return True
                else:
                    # Same day
                    if close_minutes > 1080:
                        return True
                        
    return False

# Filter
filtered_rows = []
for index, row in df.iterrows():
    if is_open_after_6pm(row['hours']):
        filtered_rows.append(row)

result_df = pd.DataFrame(filtered_rows)

# Rank
if not result_df.empty:
    result_df = result_df.sort_values(by='average_rating', ascending=False)
    top_5 = result_df.head(5)
    
    # Select columns
    final_output = top_5[['name', 'hours', 'average_rating']].to_dict(orient='records')
else:
    final_output = []

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-9775449009850635239': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-16950006905405969498': [{'count': '79'}], 'var_function-call-4415990974099584409': [{'count(*)': '2000'}], 'var_function-call-3639795649981648571': 'file_storage/function-call-3639795649981648571.json', 'var_function-call-1810228243877111124': 'file_storage/function-call-1810228243877111124.json'}

exec(code, env_args)
