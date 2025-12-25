code = """import json
import pandas as pd
import re

# Load data
with open('var_function-call-3565738323903944674.json', 'r') as f:
    businesses = json.load(f)

with open('var_function-call-3806619213573453234.json', 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
df_reviews = pd.DataFrame(reviews)
# Ensure rating is numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

# Helper function to parse time
def parse_time_to_hours(time_str):
    # Returns 24-hour float. 6:30PM -> 18.5. 12AM -> 24.0 (as closing time)
    # Handle "Open 24 hours" before calling this.
    time_str = time_str.strip()
    if not time_str: return 0.0
    
    # Extract AM/PM
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    # Remove AM/PM
    t = time_str.replace('AM', '').replace('PM', '').strip()
    
    if ':' in t:
        h, m = map(int, t.split(':'))
    else:
        h = int(t)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0 # 12 AM is 0:00
        
    # Special handling for closing time:
    # If closing time is 12AM (midnight) or later (1AM, 2AM...), it effectively remains open after 6PM.
    # However, for simple comparison:
    # If 12AM is parsed as 0.0, it is < 18.0. But 12AM closing means open until midnight.
    # If closing time is 1AM (1.0), it means open until 1AM next day.
    # So if h < 12 (AM hours) and it's a closing time, we can treat it as h + 24 for comparison with 18.
    # But 12PM is 12.0.
    
    val = h + m/60.0
    return val

def is_open_after_6pm(hours_data):
    # hours_data is a list of [Day, TimeRange] or just a string "None"
    if not hours_data or hours_data == 'None':
        return False
    
    try:
        if isinstance(hours_data, str):
            # Try parsing JSON
            try:
                schedule = json.loads(hours_data)
            except:
                # If not json, maybe literal eval or just string
                # Given the format in previous turn, it's a JSON string
                return False
        else:
            schedule = hours_data
            
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_entry in schedule:
            day = day_entry[0]
            time_range = day_entry[1]
            
            if day in weekdays:
                if 'Open 24 hours' in time_range:
                    return True
                if 'Closed' in time_range:
                    continue
                
                # Split start and end
                # Separators can be \u2013 (en dash) or -
                # Regex split
                parts = re.split(r'\u2013|-', time_range)
                if len(parts) == 2:
                    end_time_str = parts[1]
                    end_val = parse_time_to_hours(end_time_str)
                    
                    # Logic for "after 6PM" (18.0)
                    # If end_val > 18.0, it's open after 6PM.
                    # Also need to handle late night closings (e.g. 1AM).
                    # My parse function:
                    # 1AM -> 1.0. 1.0 < 18.0. But it IS open after 6PM.
                    # So if closing time is AM (0 to 11.99), it implies next day, so > 18.0.
                    # Unless it's like 11AM closing (morning shift only).
                    # But usually businesses open in AM and close in PM or next AM.
                    # Let's check start time to be sure? 
                    # Assume standard business:
                    # If closes in AM (0-11), likely next day -> Open after 6PM.
                    # If closes in PM: must be > 6PM.
                    # parsing logic adjustments:
                    
                    is_am = 'AM' in end_time_str
                    is_pm = 'PM' in end_time_str
                    
                    # Re-parse to be careful
                    val = parse_time_to_hours(end_time_str)
                    
                    # If PM and val > 18.0: True
                    if is_pm and val > 18.0:
                        return True
                        
                    # If AM (0.0 to 11.99):
                    # If it's 12AM (0.0), it's midnight. It is > 6PM.
                    # If it's 1AM, etc. It is > 6PM.
                    # Is there a case where it closes at 10AM?
                    # "6AM-10AM". 10AM is 10.0. < 18.0.
                    # How to distinguish 1AM (next day) from 10AM (same day)?
                    # Check start time.
                    # Start: "6AM". End "10AM". Duration 4h.
                    # Start "6PM". End "1AM".
                    # If start time is before end time (numerically), it's same day.
                    # If start time is after end time, it crosses midnight.
                    start_time_str = parts[0]
                    start_val = parse_time_to_hours(start_time_str)
                    
                    if start_val > val:
                        # Crosses midnight. e.g. Start 18.0, End 1.0.
                        # It definitely is open at some point after 6PM?
                        # If start is 8AM and end is 2AM.
                        # If start is 5AM and end is 10AM. No.
                        # If start > val:
                        # Example: 8PM to 2AM. Open after 6PM? Yes.
                        # Example: 6AM to 10AM (start < val). Not open after 6PM.
                        # Example: 6AM to 6PM (start < val). val = 18.0. Not AFTER 6PM.
                        # Example: 6AM to 7PM. val = 19.0. Open after 6PM.
                        
                        # So:
                        # Case 1: Start < End. Check if End > 18.0.
                        # Case 2: Start > End. It crosses midnight.
                        # Does it cover post-6PM?
                        # If Start is < 18.0 (e.g. 8AM) and crosses midnight (End 1AM), yes, it covers 6PM.
                        # If Start is > 18.0 (e.g. 8PM). It is open after 6PM (at 8PM).
                        # So if crosses midnight, it generally is open after 6PM, unless start is like 4AM and end is 5AM (next day?? No).
                        # Valid shifts usually don't wrap around 24h multiple times.
                        # Safe assumption: If crosses midnight, it is open late (after 6PM).
                        # Exception: Open 1AM to 5AM. Start 1.0, End 5.0. Start < End. End < 18.0. Not open after 6PM.
                        # Open 11PM to 4AM. Start 23.0, End 4.0. Crosses midnight. Yes.
                        return True
                    else:
                        # Start < End. Same day.
                        if val > 18.0:
                            return True
                            
    except Exception as e:
        # print(f"Error parsing {hours_data}: {e}")
        pass
        
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        b_id = b['gmap_id']
        if b_id in avg_ratings:
            b['average_rating'] = avg_ratings[b_id]
            filtered_businesses.append(b)

# Rank by rating desc
filtered_businesses.sort(key=lambda x: x['average_rating'], reverse=True)

# Take top 5
top_5 = filtered_businesses[:5]

# Format output
result = []
for b in top_5:
    result.append({
        "name": b['name'],
        "hours": b['hours'],
        "average_rating": b['average_rating']
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4970281995441041141': ['business_description'], 'var_function-call-4970281995441039434': ['review'], 'var_function-call-569539876123265185': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-3945752392740038203': [{'count': '79'}], 'var_function-call-2961703696066761256': [{'COUNT(*)': '2000'}], 'var_function-call-3565738323903944674': 'file_storage/function-call-3565738323903944674.json', 'var_function-call-3806619213573453234': 'file_storage/function-call-3806619213573453234.json'}

exec(code, env_args)
