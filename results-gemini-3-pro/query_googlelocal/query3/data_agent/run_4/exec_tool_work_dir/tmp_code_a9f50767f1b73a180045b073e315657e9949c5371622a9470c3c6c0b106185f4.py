code = """import json
import pandas as pd

# Load the file from previous step
file_path = locals()['var_function-call-1379940745010134886']
with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def parse_time(t_str):
    # Returns minutes from midnight
    # 12AM -> 0, 1AM -> 60 ... 12PM -> 720, 1PM -> 780 ...
    t_str = t_str.strip()
    if t_str == "Open 24 hours":
        return "24h"
    if t_str == "Closed":
        return None
        
    # Standardize
    t_str = t_str.upper()
    is_pm = "PM" in t_str
    is_am = "AM" in t_str
    
    # Remove suffix
    t_clean = t_str.replace("PM", "").replace("AM", "").strip()
    
    if ":" in t_clean:
        parts = t_clean.split(":")
        h = int(parts[0])
        m = int(parts[1])
    else:
        h = int(t_clean)
        m = 0
        
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

qualifying_gmap_ids = []
qualifying_info = {} # gmap_id -> {name, hours}

for b in businesses:
    hours_str = b['hours']
    gmap_id = b['gmap_id']
    name = b['name']
    
    if not hours_str or hours_str == 'None':
        continue
        
    try:
        # hours_str is a string representation of list, e.g. "[['Day', 'Time']...]"
        # It's valid JSON if we replace single quotes with double quotes? 
        # But the sample shows double quotes. So json.loads might work.
        # However, the sample output was python repr? "hours": "[[\"Thursday\", \"6:30AM\u20136PM\"]...]"
        # It looks like a JSON string.
        hours_list = json.loads(hours_str)
    except:
        continue
        
    is_open_late = False
    for day, time_range in hours_list:
        if day in weekdays:
            if "Open 24 hours" in time_range:
                is_open_late = True
                break
            if "Closed" in time_range:
                continue
                
            # Split by en-dash or hyphen
            # \u2013 is en-dash
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) != 2:
                continue
                
            start_str = parts[0]
            end_str = parts[1]
            
            start_min = parse_time(start_str)
            end_min = parse_time(end_str)
            
            if start_min is None or end_min is None:
                continue
                
            # Check for wrapping
            if end_min < start_min:
                # Wraps to next day (e.g. 5PM to 2AM -> 1020 to 120)
                # Effectively end_min is next day.
                # It is open during the evening.
                # Definitely open after 6PM (18:00 = 1080 min)
                # If start is before 18:00 (e.g. 5PM) and ends next day, it covers 6PM.
                # If start is after 18:00 (e.g. 8PM), it covers post-6PM.
                is_open_late = True
            else:
                # Same day
                # Check if end_min > 18:00 (1080 min)
                if end_min > 1080:
                    is_open_late = True
            
            if is_open_late:
                break
    
    if is_open_late:
        qualifying_gmap_ids.append(gmap_id)
        qualifying_info[gmap_id] = {'name': name, 'hours': hours_list}

print("__RESULT__:")
print(json.dumps({'ids': qualifying_gmap_ids, 'info': qualifying_info}))"""

env_args = {'var_function-call-9531013917415431501': ['business_description'], 'var_function-call-8008252862987401497': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-18334988602388791362': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}], 'var_function-call-14172591937905352552': [{'count': '79'}], 'var_function-call-1379940745010134886': 'file_storage/function-call-1379940745010134886.json'}

exec(code, env_args)
