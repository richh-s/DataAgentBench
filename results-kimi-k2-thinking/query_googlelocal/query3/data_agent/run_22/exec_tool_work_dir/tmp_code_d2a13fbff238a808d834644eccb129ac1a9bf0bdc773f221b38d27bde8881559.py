code = """import json
import re
from datetime import datetime

# Get business data
business_data = locals()['var_functions.query_db:8']

# Function to parse hours string and check if business is open after 6PM on any weekday
def parse_hours_and_check(hours_str):
    """Parse hours string and check if open after 6PM on any weekday"""
    if not hours_str or hours_str == 'None':
        return False, None
    
    try:
        # Parse the string representation of list
        hours_list = eval(hours_str)
        if not isinstance(hours_list, list):
            return False, None
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_entry in hours_list:
            if len(day_entry) != 2:
                continue
                
            day, hours = day_entry
            if day not in weekdays:
                continue
                
            # Handle cases like "9:30AM–10PM" or "Closed"
            if hours == 'Closed' or hours == 'Open 24 hours':
                if hours == 'Open 24 hours':
                    # Open 24 hours means it's open after 6PM
                    return True, hours_list
                continue
            
            # Extract closing time (part after the dash/en dash)
            dash_match = re.search(r'[\u2013\u2014\u2015-]', hours)
            if dash_match:
                closing_part = hours[dash_match.end():].strip()
                
                # Extract time and AM/PM
                time_match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*(AM|PM)', closing_part, re.IGNORECASE)
                if time_match:
                    hour = int(time_match.group(1))
                    minutes = int(time_match.group(2)) if time_match.group(2) else 0
                    am_pm = time_match.group(3).upper()
                    
                    # Convert to 24-hour format
                    if am_pm == 'PM' and hour != 12:
                        hour += 12
                    elif am_pm == 'AM' and hour == 12:
                        hour = 0
                    
                    # Check if closing time is after 6:00 PM (18:00)
                    if hour > 18 or (hour == 18 and minutes > 0):
                        return True, hours_list
        
        return False, hours_list
    except:
        return False, None

# Process businesses
open_after_6pm = []
for business in business_data:
    if 'hours' in business and business['hours'] != 'None':
        is_open_late, parsed_hours = parse_hours_and_check(business['hours'])
        if is_open_late:
            business['parsed_hours'] = parsed_hours
            open_after_6pm.append(business)

print(f"Total businesses: {len(business_data)}")
print(f"Businesses open after 6PM: {len(open_after_6pm)}")

# Save result for next step
result_data = {
    'open_after_6pm': open_after_6pm,
    'total_count': len(business_data),
    'late_count': len(open_after_6pm)
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'state': 'Open ⋅ Closes 5PM', 'count': '18'}, {'state': 'None', 'count': '9'}, {'state': 'Closed ⋅ Opens 10AM', 'count': '5'}, {'state': 'Open ⋅ Closes 9:30PM', 'count': '4'}, {'state': 'Open now', 'count': '4'}, {'state': 'Open ⋅ Closes 8PM', 'count': '3'}, {'state': 'Permanently closed', 'count': '3'}, {'state': 'Open ⋅ Closes 7PM', 'count': '3'}, {'state': 'Open ⋅ Closes 4PM', 'count': '3'}, {'state': 'Open ⋅ Closes 10PM', 'count': '3'}, {'state': 'Open ⋅ Closes 6PM', 'count': '3'}, {'state': 'Closed ⋅ Opens 9AM', 'count': '3'}, {'state': 'Open 24 hours', 'count': '2'}, {'state': 'Open ⋅ Closes 5:30PM', 'count': '2'}, {'state': 'Open ⋅ Closes 11AM ⋅ Reopens 4PM', 'count': '1'}, {'state': 'Open ⋅ Closes 3:30PM', 'count': '1'}, {'state': 'Open ⋅ Closes 9PM', 'count': '1'}, {'state': 'Closed ⋅ Opens 5PM Fri', 'count': '1'}, {'state': 'Open ⋅ Closes 11:30AM ⋅ Reopens 1PM', 'count': '1'}, {'state': 'Open ⋅ Closes 12PM ⋅ Reopens 1PM', 'count': '1'}], 'var_functions.query_db:6': [{'name': 'City Textile', 'hours': 'None'}, {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'name': 'Elite Massage', 'hours': 'None'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
