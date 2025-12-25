code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-7208437766801302728'], 'r') as f:
    businesses = json.load(f)

with open(locals()['var_function-call-12495174720899739046'], 'r') as f:
    reviews = json.load(f)

# Calculate average ratings
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

def parse_time_to_minutes(t_str):
    # t_str like "6PM", "6:30PM", "12AM", "12:30AM", "Open 24 hours"
    if not t_str: return -1
    t_str = t_str.strip().upper()
    if "24 HOURS" in t_str:
        return 24 * 60 + 1 # Treated as effectively infinite/always open
    
    # Check for AM/PM
    is_pm = "PM" in t_str
    is_am = "AM" in t_str
    
    if not (is_pm or is_am):
        return -1 # Unknown format
    
    # Remove AM/PM
    t_clean = t_str.replace("PM", "").replace("AM", "").strip()
    
    parts = t_clean.split(":")
    hour = int(parts[0])
    minute = int(parts[1]) if len(parts) > 1 else 0
    
    if is_pm and hour != 12:
        hour += 12
    if is_am and hour == 12:
        hour = 0
        
    return hour * 60 + minute

def is_open_after_6pm(hours_json):
    if not hours_json or hours_json == "None":
        return False
    try:
        hours_list = json.loads(hours_json)
    except:
        return False
        
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for day_info in hours_list:
        day_name = day_info[0]
        time_range = day_info[1]
        
        if day_name in weekdays:
            if "Closed" in time_range:
                continue
            if "24 hours" in time_range:
                return True
                
            # Split time range. Separator is \u2013 (en dash) or -
            # In the sample: "6:30AM\u20136PM"
            # It seems the separator is \u2013 based on previous output
            parts = re.split(r'\u2013|-', time_range)
            if len(parts) >= 2:
                closing_str = parts[-1]
                closing_minutes = parse_time_to_minutes(closing_str)
                
                # 6:00 PM is 18 * 60 = 1080 minutes
                # If closing time is exactly 6PM (1080), it's not AFTER 6PM.
                # If closing time is e.g. 1AM, it is 1*60 = 60 minutes.
                # But physically 1AM is after 6PM of the previous day. 
                # Usually closing times like 1AM, 2AM imply late night operation.
                # So if closing_minutes < opening_minutes (crossing midnight) OR closing_minutes > 1080
                
                # Simplified logic:
                # If parsed hour is between 0 and 5 (00:00 to 05:00), it's late night -> Open after 6PM.
                # If parsed minutes > 1080 (18:00), it's open after 6PM.
                
                if closing_minutes > 1080:
                    return True
                if closing_minutes < 6 * 60: # Closings in early morning (e.g. 1 AM)
                     # Note: 12AM is 0 min. 12:01AM is 1 min.
                     # We assume early morning hours mean open past midnight.
                     return True
                     
    return False

eligible_businesses = []

for b in businesses:
    g_id = b['gmap_id']
    if is_open_after_6pm(b['hours']):
        rating = avg_ratings.get(g_id, 0)
        # Store needed info
        eligible_businesses.append({
            "name": b['name'],
            "hours": b['hours'], # Keep raw string or parsed? Requirement says "Include their... operating hours"
            "rating": rating,
            "gmap_id": g_id
        })

# Sort by rating desc
eligible_businesses.sort(key=lambda x: x['rating'], reverse=True)

# Top 5
top_5 = eligible_businesses[:5]

# Format operating hours for display? The user asked to "Include their names, operating hours, and average ratings."
# The raw JSON string is a bit ugly. I'll pass it as is or clean it up slightly if needed.
# Since the tool output should be JSON, passing the list structure is fine.

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-2951264646156852967': ['business_description'], 'var_function-call-13804032949895521975': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-10421031522172776481': [{'count': '79'}], 'var_function-call-7938855942288438444': [{'COUNT(*)': '2000'}], 'var_function-call-7208437766801302728': 'file_storage/function-call-7208437766801302728.json', 'var_function-call-12495174720899739046': 'file_storage/function-call-12495174720899739046.json'}

exec(code, env_args)
