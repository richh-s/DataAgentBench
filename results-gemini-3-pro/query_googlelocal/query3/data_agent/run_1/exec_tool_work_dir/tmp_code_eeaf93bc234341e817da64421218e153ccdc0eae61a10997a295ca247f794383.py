code = """import json
import re

# Load businesses
with open(locals()['var_function-call-7844734147639526508'], 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # Returns minutes from midnight
    # t_str example: 6:30AM, 6PM, 12PM (noon), 12AM (midnight)
    # 12PM is 12*60 = 720
    # 12AM is 0
    # 1AM is 60
    # 1PM is 13*60 = 780
    t_str = t_str.strip()
    if not t_str: return None
    
    match = re.match(r'(\d+)(?::(\d+))?\s*(AM|PM)', t_str, re.IGNORECASE)
    if not match:
        # Maybe 24 hour format? Unlikely given examples.
        # Just return None
        return None
    
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    period = match.group(3).upper()
    
    if period == 'PM' and h != 12:
        h += 12
    elif period == 'AM' and h == 12:
        h = 0
    
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # The hours string is a string repr of a python list, e.g. "[['Day', 'Range'], ...]"
        # However, it might be safer to use json.loads if it's valid JSON, but the example showed single quotes?
        # Example: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]" - This looks like JSON.
        # But let's check if there are single quotes. 
        # The output from query_db showed double quotes inside the string.
        # Let's try json.loads. If fail, use ast.literal_eval
        import ast
        try:
            schedule = json.loads(hours_str)
        except:
            schedule = ast.literal_eval(hours_str)
            
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        target_time = 18 * 60 # 6:00 PM
        
        for day, time_range in schedule:
            if day in weekdays:
                if time_range == 'Open 24 hours':
                    return True
                if time_range == 'Closed':
                    continue
                
                # Split range. Separators can be \u2013 (en dash) or -
                # Regex split
                parts = re.split(r'\u2013|-', time_range)
                if len(parts) == 2:
                    start_str, end_str = parts
                    end_minutes = parse_time(end_str)
                    start_minutes = parse_time(start_str)
                    
                    if end_minutes is not None:
                        # Handle overnight cases, e.g. 5PM-2AM. 2AM is 120, which is < target_time.
                        # But it means it stays open past midnight, so definitely past 6PM.
                        # If end < start, it crosses midnight.
                        # If end > start: check if end > target_time
                        
                        if start_minutes is not None and end_minutes < start_minutes:
                             # Crosses midnight, so it is open at 11:59PM, which is > 6PM
                             # Unless it opens after 6PM? e.g. 10PM-2AM. Yes, open after 6PM.
                             # What if it opens at 3AM closes at 5AM? (Crosses midnight is usually PM to AM)
                             # Assuming standard business hours.
                             return True
                        elif end_minutes > target_time:
                            return True
                            
        return False
    except Exception as e:
        # print(f"Error parsing {hours_str}: {e}")
        return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b.get('hours')):
        filtered_businesses.append(b)

# Extract gmap_ids
gmap_ids = [b['gmap_id'] for b in filtered_businesses]

print("__RESULT__:")
print(json.dumps({
    "filtered_count": len(filtered_businesses),
    "gmap_ids": gmap_ids,
    "businesses": filtered_businesses
}))"""

env_args = {'var_function-call-14154199791297009731': ['business_description'], 'var_function-call-484761039144150750': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-1005033066681998170': [{'count': '79'}], 'var_function-call-4672188591761786021': ['review'], 'var_function-call-6754515918236083387': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}], 'var_function-call-7844734147639526508': 'file_storage/function-call-7844734147639526508.json'}

exec(code, env_args)
