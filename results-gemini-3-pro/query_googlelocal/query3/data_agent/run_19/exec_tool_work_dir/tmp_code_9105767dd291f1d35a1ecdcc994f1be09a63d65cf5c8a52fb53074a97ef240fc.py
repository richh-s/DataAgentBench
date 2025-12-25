code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10152310203624475919'], 'r') as f:
    businesses = json.load(f)
    
with open(locals()['var_function-call-16403635681702118191'], 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'])

# Calculate average rating per gmap_id
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)

# Merge ratings into businesses
df_biz = pd.merge(df_biz, avg_ratings, on='gmap_id', how='left')

# Function to parse time
def parse_time(t_str):
    # Returns float 0-23.99
    # t_str example: "6:30AM", "6PM", "12AM", "12PM", "12:30PM"
    if not t_str: return 0.0
    t_str = t_str.strip()
    is_pm = 'PM' in t_str
    is_am = 'AM' in t_str
    
    # Remove AM/PM
    t_numeric = t_str.replace('PM', '').replace('AM', '').strip()
    
    if ':' in t_numeric:
        parts = t_numeric.split(':')
        h = int(parts[0])
        m = int(parts[1])
    else:
        h = int(t_numeric)
        m = 0
        
    # Adjust for 12h clock
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h + m/60.0

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # Evaluate string representation of list
        # It comes as a string like "[[\"Day\", \"Time\"]]"
        # We can use json.loads if it's valid JSON, or simple eval if not (but eval is risky).
        # The sample showed double quotes escaped inside the string? 
        # Actually the sample output was: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # This looks like a JSON string.
        hours_list = json.loads(hours_str)
    except:
        # Fallback or return False
        return False
        
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day_item in hours_list:
        if len(day_item) != 2: continue
        day = day_item[0]
        time_range = day_item[1]
        
        if day in weekdays:
            if time_range == 'Closed':
                continue
            if time_range == 'Open 24 hours':
                return True
                
            # Split range
            # Range chars seen: \u2013 (en dash). Could be hyphen too.
            # Regex split
            parts = re.split(r'[\u2013\-\u2014]', time_range)
            if len(parts) == 2:
                start_str = parts[0]
                end_str = parts[1]
                
                try:
                    start_h = parse_time(start_str)
                    end_h = parse_time(end_str)
                    
                    # Logic: 
                    # If End < Start, it crosses midnight (e.g. 5PM to 1AM). -> Open after 6PM (18.0)
                    # If End > 18.0 -> Open after 6PM.
                    
                    if end_h < start_h:
                        return True
                    if end_h > 18.0:
                        return True
                except:
                    continue
                    
    return False

# Filter businesses
eligible_biz = []
for index, row in df_biz.iterrows():
    if is_open_after_6pm(row['hours']):
        eligible_biz.append(row)

df_eligible = pd.DataFrame(eligible_biz)

# Sort by avg_rating desc
if not df_eligible.empty:
    df_sorted = df_eligible.sort_values(by='avg_rating', ascending=False)
    top_5 = df_sorted.head(5)
    
    # Prepare result
    result_list = []
    for idx, row in top_5.iterrows():
        result_list.append({
            "name": row['name'],
            "hours": row['hours'],
            "average_rating": row['avg_rating']
        })
else:
    result_list = []

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-1227827140834025280': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-10858273279927582185': [{'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_38'}], 'var_function-call-11412053873557210717': [{'count': '66'}], 'var_function-call-6980382487236268712': [{'count': '79'}], 'var_function-call-12176905152175675848': [{'COUNT(*)': '2000'}], 'var_function-call-10152310203624475919': 'file_storage/function-call-10152310203624475919.json', 'var_function-call-16403635681702118191': 'file_storage/function-call-16403635681702118191.json'}

exec(code, env_args)
