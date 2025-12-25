code = """import json
import ast
import re
from datetime import datetime

# Load the business data
with open(locals()['var_function-call-6337185605064194143'], 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # formats: "6PM", "6:30PM", "12PM", "12AM", "6AM"
    # return minutes from midnight
    if not t_str: return None
    try:
        t = datetime.strptime(t_str, "%I:%M%p")
        return t.hour * 60 + t.minute
    except ValueError:
        try:
            t = datetime.strptime(t_str, "%I%p")
            return t.hour * 60 + t.minute
        except ValueError:
            return None

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    try:
        # The string is like "[['Day', 'Time'], ...]"
        # Use ast.literal_eval for safe parsing
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == "Closed":
                continue
            if time_range == "Open 24 hours":
                return True
            
            # Split time range "Start–End"
            # The separator seems to be \u2013 (en-dash) based on output
            # But let's handle hyphen as well just in case
            parts = re.split(r'[–-]', time_range)
            if len(parts) == 2:
                start_str = parts[0].strip()
                end_str = parts[1].strip()
                
                # We care about end time
                # If end time is e.g. 1AM (next day), it is technically after 6PM.
                # Logic: parse end time.
                # If end time corresponds to > 18:00 (6 PM), then yes.
                # 6 PM is 18 * 60 = 1080 minutes.
                
                end_minutes = parse_time(end_str)
                if end_minutes is not None:
                    # Special handling for "12AM" (0 min) or times in early morning which mean late night closing?
                    # "Open after 6 PM" usually means the shop doesn't close before 6 PM.
                    # e.g. Closes at 5 PM -> No.
                    # Closes at 6 PM -> No (it closes AT 6 PM, not after).
                    # Closes at 6:30 PM -> Yes.
                    # Closes at 1 AM -> Yes.
                    
                    # 6 PM = 18:00 = 1080 min.
                    # If end_minutes > 1080: Yes.
                    # If end_minutes < start_minutes (e.g. 9AM to 2AM): Yes, it spans across midnight, so it is open after 6 PM.
                    
                    start_minutes = parse_time(start_str)
                    
                    if start_minutes is not None:
                        # Case 1: Spans midnight (e.g. 5PM - 2AM) -> end < start
                        # Case 2: Standard day (e.g. 9AM - 9PM) -> end > start
                        
                        if end_minutes < start_minutes:
                            # It closes the next day, so it is definitely open in the evening.
                            # Unless it opens at 4 AM and closes at 5 AM (unlikely for "Open after 6 PM" check logic context usually).
                            # Assuming standard business hours.
                            # If it spans midnight, it covers the evening (unless it opens after 6 PM? but "remains open" implies it's open at 6 PM and continues).
                            # The question: "remains open after 6:00 PM".
                            # This means Closing Time > 6:00 PM.
                            return True
                        else:
                            # Does not span midnight
                            if end_minutes > 1080: # 18:00
                                return True
    return False

filtered_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_businesses.append(b)

# Extract gmap_ids
gmap_ids = [b['gmap_id'] for b in filtered_businesses]

print("__RESULT__:")
print(json.dumps(filtered_businesses))"""

env_args = {'var_function-call-8882120226069178599': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-15047165187426334041': [{'count': '79'}], 'var_function-call-6337185605064194143': 'file_storage/function-call-6337185605064194143.json'}

exec(code, env_args)
