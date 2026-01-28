code = """import json
import re
from datetime import datetime

# Load the business data
business_file = locals()['var_functions.query_db:2']
with open(business_file, 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
open_after_6 = []

def parse_time(time_str):
    # Handle formats like "6:30AM", "12PM", "9:30AM", etc.
    time_str = time_str.replace('\u2013', '-').replace('\u20132', '-').replace('\u20139', '-')
    
    if 'AM' in time_str or 'PM' in time_str:
        match = re.match(r'(\d{1,2})(:(\d{2}))?(AM|PM)', time_str, re.IGNORECASE)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(3)) if match.group(3) else 0
            period = match.group(4).upper()
            
            if period == 'PM' and hour != 12:
                hour += 12
            elif period == 'AM' and hour == 12:
                hour = 0
                
            return hour + minute/60.0
    return None

def is_open_after_6pm(hours_list):
    # hours_list is a string representation of nested arrays
    try:
        # Parse the string as JSON
        hours_data = json.loads(hours_list.replace('\u2013', '-'))
        
        for day_entry in hours_data:
            day = day_entry[0]
            hours = day_entry[1]
            
            # Only check weekdays
            if day in weekdays and hours != 'Closed':
                if '-' in hours:
                    # Parse closing time
                    closing_time = hours.split('-')[1].strip()
                    closing_hour = parse_time(closing_time)
                    
                    if closing_hour is not None and closing_hour >= 18.0:  # 6 PM or later
                        return True
    except:
        pass
    
    return False

# Find businesses open after 6 PM
eligible_businesses = []
for business in businesses:
    hours_list = business['hours']
    if hours_list and hours_list != 'None':
        if is_open_after_6pm(hours_list):
            eligible_businesses.append({
                'gmap_id': business['gmap_id'],
                'name': business['name'],
                'hours': hours_list
            })

print('__RESULT__:')
print(json.dumps({
    'total_businesses': len(businesses),
    'eligible_businesses': len(eligible_businesses),
    'sample_eligible': eligible_businesses[:3] if eligible_businesses else []
}))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 66, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}}

exec(code, env_args)
