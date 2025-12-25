code = """import json
import ast
from datetime import datetime

# Load business data
with open('var_function-call-4041812981108132417.json', 'r') as f:
    businesses = json.load(f)

def parse_time(t_str):
    # formats: "6:30AM", "6PM", "12PM", "12AM", "9:30PM"
    return datetime.strptime(t_str, "%I:%M%p" if ":" in t_str else "%I%p")

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day, time_range in hours_list:
        if day in weekdays:
            if time_range == 'Closed':
                continue
            if time_range == 'Open 24 hours':
                return True
            
            # Format usually "Start–End" (using en-dash or hyphen?)
            # The sample shows "\u2013" which is en-dash.
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) == 2:
                end_time_str = parts[1].strip()
                # Handle special cases? "12AM" is midnight (next day usually).
                # "6PM" is 18:00.
                try:
                    end_dt = parse_time(end_time_str)
                    # 6:00 PM is 18:00
                    # If end_dt is 12:00 AM (midnight), it's effectively 24:00 or next day, so > 6PM
                    # Check hour.
                    # 6PM is hour 18.
                    # If time is 6:01PM or 7PM etc.
                    # Comparing datetime objects requires a reference date, but we can use time()
                    
                    target = datetime.strptime("6:00PM", "%I:%M%p").time()
                    check = end_dt.time()
                    
                    # Special handling for AM times that are early morning vs late night?
                    # Usually closing times like 1AM, 2AM are technically "next day" but represent being open late.
                    # If closing time is AM (00:00 to 11:59), and it's small (like 1 AM), it implies open past 6PM.
                    # If closing time is PM, it must be > 6PM.
                    
                    is_am = end_time_str.endswith('AM')
                    is_pm = end_time_str.endswith('PM')
                    
                    # Logic:
                    # If PM: must be > 6:00 PM. (18:00)
                    # If AM: usually means past midnight, so yes (unless it closes at like 11AM which is morning).
                    # Let's assume standard operating hours.
                    # 11AM-9:30PM -> 9:30PM > 6PM.
                    # 9AM-5PM -> 5PM < 6PM.
                    # 9AM-1AM -> 1AM is next day, so yes.
                    
                    if is_pm:
                         if check > target:
                             return True
                    elif is_am:
                        # If it closes in AM, need to check if it's "early morning" (like closes at 11am) or "late night" (closes at 2am).
                        # Usually start time helps, but here simplistic:
                        # If closing is 12AM, 1AM, 2AM, 3AM, 4AM, 5AM... it's definitely after 6PM of the previous day.
                        # If closing is 10AM, 11AM... it might be a morning shift?
                        # However, typical stores open ~9AM. If it closes at 11AM, it's not open after 6PM.
                        # If it closes at 2AM, it is.
                        # Let's assume if hour < 12 (since it's AM), if hour < 6 (e.g. 1,2,3,4,5), it's late night.
                        # If hour is 12 (midnight), it is > 6PM.
                        if check.hour < 10 or check.hour == 12 or check.hour == 0: # 12AM is 0
                            return True
                        # What if closes at 11AM? No.
                        
                except Exception as e:
                    pass
    return False

valid_businesses = []
for b in businesses:
    if is_open_after_6pm(b['hours']):
        valid_businesses.append(b)

print("__RESULT__:")
print(json.dumps(valid_businesses))"""

env_args = {'var_function-call-11274278717337983726': ['business_description'], 'var_function-call-5679228863261529158': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_function-call-10625289044817991517': [{'count': '79'}], 'var_function-call-4041812981108132417': 'file_storage/function-call-4041812981108132417.json'}

exec(code, env_args)
