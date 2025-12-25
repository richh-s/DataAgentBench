code = """import json
import ast
import pandas as pd

# Access file paths from local variables
businesses_path = locals()['var_function-call-7871304986794142237']
reviews_path = locals()['var_function-call-7871304986794139884']

# Load data
with open(businesses_path, 'r') as f:
    businesses = json.load(f)

with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

# Helper to parse time
def parse_time(t_str):
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
    try:
        h, m = parse_time(closing_time_str)
        # 0-3 AM is definitely after 6PM (next day)
        # 4-11 AM - could be breakfast/lunch place closing. Not "open after 6PM" usually.
        # But if a place closes at 7AM, it was open all night.
        # Let's assume if h < 12 (AM) it's likely late night closing (except maybe 10AM/11AM).
        # But for safety, standard late hours are PM or very early AM.
        # 12AM = 0.
        
        # If h < 12, it's AM.
        # If closing is 1AM, 2AM... it's > 18:00 (conceptually).
        # If closing is 11AM, it's < 18:00 (conceptually for that day).
        # Let's say if h < 9 (9AM), it's late night.
        if 0 <= h < 9:
            return True
        
        # PM times
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
        hours_list = json.loads(hours_raw)
    except:
        try:
            hours_list = ast.literal_eval(hours_raw)
        except:
            continue
            
    open_late = False
    
    for day_hours in hours_list:
        if not isinstance(day_hours, list) or len(day_hours) < 2:
            continue
            
        day_name = day_hours[0]
        time_range = day_hours[1]
        
        if day_name in weekdays:
            if "Open 24 hours" in time_range:
                open_late = True
                break
            if "Closed" in time_range:
                continue
                
            # Split range
            # Separators can be – (\u2013) or -
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
                
            if len(parts) >= 2:
                # Some ranges might be complex like "11AM-2PM, 5PM-9PM"
                # If comma exists, take the last part? 
                # Or check any part.
                # Usually Google Maps format is one range per day entry in this list structure or multiple?
                # The sample shows "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
                # If split, parts[1] is "6PM".
                closing_time = parts[-1].strip() # Take the end time
                if is_later_than_6pm(closing_time):
                    open_late = True
                    break
    
    if open_late:
        avg_rating = avg_ratings.get(gmap_id)
        if avg_rating is not None:
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
