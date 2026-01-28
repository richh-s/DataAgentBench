code = """import json
import re

# Read business data from the file
business_file_path = locals()['var_functions.query_db:5']
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Read review data from the file
review_file_path = locals()['var_functions.query_db:8']
with open(review_file_path, 'r') as f:
    review_data = json.load(f)

# Function to parse time strings and check if after 6 PM
def is_after_6pm(time_str):
    if not time_str or time_str == 'Closed':
        return False
    if 'Open 24 hours' in time_str:
        return True
    
    # Extract closing time (after the dash)
    if '\u2013' in time_str:
        # Use unicode en-dash
        parts = time_str.split('\u2013')
        if len(parts) >= 2:
            closing = parts[1].strip()
        else:
            return False
    elif '-' in time_str:
        parts = time_str.split('-')
        if len(parts) >= 2:
            closing = parts[1].strip()
        else:
            return False
    else:
        return False
    
    # Handle times like "9:30PM", "10PM", "12PM", "6PM"
    closing = closing.strip()
    
    # Check for various patterns
    if 'PM' in closing:
        # Extract hour part
        hour_match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*PM', closing, re.IGNORECASE)
        if hour_match:
            hour = int(hour_match.group(1))
            minute = int(hour_match.group(2)) if hour_match.group(2) else 0
            
            # Convert to 24-hour format
            if hour != 12:
                hour_24 = hour + 12
            else:
                hour_24 = 12
                
            # Check if after 18:00 (6 PM)
            if hour_24 > 18 or (hour_24 == 18 and minute > 0):
                return True
    elif 'AM' in closing:
        # For AM times, only after 6 PM if it's 12 AM (midnight)
        hour_match = re.search(r'(\d{1,2})(?::(\d{2}))?\s*AM', closing, re.IGNORECASE)
        if hour_match:
            hour = int(hour_match.group(1))
            if hour == 12:  # Midnight
                return True
    
    return False

# Filter businesses open after 6 PM on at least one weekday
def check_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # The hours field is a string representation of a list
        hours_list = eval(hours_str)  # Using eval since it's stored as string representation
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if isinstance(day_info, list) and len(day_info) >= 2:
                day = day_info[0]
                hours = day_info[1]
                
                if day in weekdays and is_after_6pm(hours):
                    return True
    except:
        return False
    
    return False

# Filter businesses
eigible_businesses = []
for business in business_data:
    hours = business.get('hours')
    if hours and check_open_after_6pm(hours):
        eigible_businesses.append(business)

print('__RESULT__:')
print(json.dumps({
    'total_businesses': len(business_data),
    'eigible_businesses': len(eigible_businesses),
    'first_eigible': eigible_businesses[0] if eigible_businesses else None
}))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'hours': 'None', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'gmap_id': 'gmap_45'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'businesses_loaded': 66, 'reviews_loaded': 2000, 'first_business': {'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'gmap_id': 'gmap_41'}}}

exec(code, env_args)
