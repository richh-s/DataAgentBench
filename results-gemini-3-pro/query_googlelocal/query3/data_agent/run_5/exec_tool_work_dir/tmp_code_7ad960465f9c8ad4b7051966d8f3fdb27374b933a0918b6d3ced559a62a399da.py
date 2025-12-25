code = """import json
import re

# Load data
with open(locals()['var_function-call-17831508441437352482'], 'r') as f:
    businesses = json.load(f)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def parse_time(t_str):
    # Returns 24h float or int, e.g., 18.0 or 18.5
    # t_str like "6PM", "6:30PM", "12AM"
    if t_str == "Open 24 hours":
        return 24.0 # Special case
    
    t_str = t_str.strip()
    match = re.match(r"(\d+)(?::(\d+))?\s*(AM|PM)", t_str, re.IGNORECASE)
    if not match:
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    ampm = match.group(3).upper()
    
    if ampm == "PM" and h != 12:
        h += 12
    if ampm == "AM" and h == 12:
        h = 0
        
    return h + m/60.0

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    try:
        hours_list = json.loads(hours_str.replace("'", '"')) # Sometimes it might be single quotes
    except:
        # If standard json fail, try eval or manual parse if simple
        # The preview showed double quotes, so json.loads might work if string is valid JSON
        # But looking at preview: "[[\"Thursday\", \"6:30AM\u20136PM\"]...]" which is valid JSON.
        try:
             hours_list = json.loads(hours_str)
        except:
            return False
            
    if not isinstance(hours_list, list):
        return False

    for day_info in hours_list:
        if len(day_info) != 2:
            continue
        day, time_range = day_info
        
        if day in weekdays:
            if "Open 24 hours" in time_range:
                return True
            if "Closed" in time_range:
                continue
            
            # Split by en-dash or hyphen
            # The preview shows \u2013 (en-dash)
            # "6:30AM\u20136PM"
            parts = re.split(r'\u2013|-', time_range)
            if len(parts) == 2:
                end_time_str = parts[1]
                end_time = parse_time(end_time_str)
                
                if end_time is not None:
                    # check if end_time > 18.0
                    # Special handling for late night (e.g. closes at 1AM)
                    # 1AM is 1.0. 18.0 is 6PM.
                    # If a business closes at 1AM, it definitely stays open after 6PM (assumed open during day).
                    # But if it opens at 8PM and closes at 10PM, it is open after 6PM.
                    # The condition is "remains open after 6:00 PM".
                    # Usually this means the closing time is > 18:00.
                    # If closing time is early morning (0, 1, 2...), it is > 18:00 in terms of "staying open".
                    # So if end_time > 18.0 or end_time < start_time?
                    # Let's assume standard day hours. If end_time < 12 (noon) and it's a closing time, it's likely next day => open after 6PM.
                    # If end_time > 18.0, it's open after 6PM.
                    
                    if end_time > 18.0:
                        return True
                    if end_time < 8.0: # Arbitrary cutoff: if closes between midnight and 8AM, it was open past 6PM.
                         return True
                         
    return False

filtered_businesses = []
target_gmap_ids = []

for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)
        target_gmap_ids.append(b['gmap_id'])

print("__RESULT__:")
print(json.dumps({
    "count": len(filtered_businesses),
    "gmap_ids": target_gmap_ids,
    "filtered_businesses": filtered_businesses
}))"""

env_args = {'var_function-call-12936472494111131858': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-7597134774412487797': [{'count': '79'}], 'var_function-call-17831508441437352482': 'file_storage/function-call-17831508441437352482.json'}

exec(code, env_args)
