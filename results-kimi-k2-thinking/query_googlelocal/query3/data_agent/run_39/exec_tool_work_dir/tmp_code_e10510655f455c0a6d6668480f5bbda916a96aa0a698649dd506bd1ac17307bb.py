code = """import json
import re
from datetime import datetime

# Get the business data file path
business_file_path = locals()['var_functions.query_db:24']

# Read the business data
with open(business_file_path, 'r') as f:
    business_data = json.load(f)

# Function to parse time string to minutes since midnight
def time_to_minutes(time_str):
    # Handle various formats like "6:30PM", "12PM", "10:30AM", etc.
    time_str = time_str.strip()
    
    # Handle "Open 24 hours" case
    if time_str == "Open 24 hours":
        return 24 * 60  # 1440 minutes
    
    # Remove any unicode dash and other characters
    time_str = time_str.replace('\u2013', '').replace('\u2014', '').replace('–', '').replace('—', '')
    
    # Extract AM/PM if present
    is_pm = 'PM' in time_str.upper()
    is_am = 'AM' in time_str.upper()
    
    # Remove AM/PM indicators and any extra text
    time_str = time_str.replace('AM', '').replace('PM', '').replace('am', '').replace('pm', '')
    time_str = time_str.strip()
    
    # Parse the time
    if ':' in time_str:
        hours, minutes = map(int, time_str.split(':'))
    else:
        hours = int(time_str)
        minutes = 0
    
    # Convert to 24-hour format
    if is_pm and hours != 12:
        hours += 12
    elif is_am and hours == 12:
        hours = 0
    
    return hours * 60 + minutes

# Function to check if a business is open after 6 PM on any weekday
def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string which is formatted as a string representation of a list
        hours_list = eval(hours_str)  # Using eval since it's a string representation of a list
        
        # Weekdays to check (Monday through Friday)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        six_pm_minutes = 18 * 60  # 6:00 PM in minutes
        
        for day_hours in hours_list:
            if len(day_hours) >= 2:
                day = day_hours[0]
                hours_range = day_hours[1]
                
                # Skip if day is not a weekday or if closed
                if day not in weekdays or hours_range == 'Closed':
                    continue
                
                # Extract closing time (part after the dash/en dash)
                if '\u2013' in hours_range or '–' in hours_range:
                    # Handle en dash
                    if '\u2013' in hours_range:
                        _, closing_time = hours_range.split('\u2013')
                    else:
                        _, closing_time = hours_range.split('–')
                elif '-' in hours_range:
                    _, closing_time = hours_range.split('-')
                else:
                    continue
                
                closing_time = closing_time.strip()
                
                # Skip if closing time indicates closed
                if closing_time in ['Closed', 'None', '']:
                    continue
                
                # Convert closing time to minutes
                try:
                    closing_minutes = time_to_minutes(closing_time)
                    
                    # Check if closing time is after 6:00 PM (or open 24 hours)
                    if closing_minutes > six_pm_minutes or 'Open 24 hours' in hours_range:
                        return True
                except:
                    continue
        
        return False
    except:
        return False

# Filter businesses that are open after 6 PM on weekdays
businesses_open_late = []
for business in business_data:
    if is_open_after_6pm(business.get('hours', '')):
        businesses_open_late.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print('__RESULT__:')
print(json.dumps({
    'total_businesses_open_late': len(businesses_open_late),
    'sample_businesses': businesses_open_late[:5]
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:22': {'data_directory_contents': [], 'available_vars': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.query_db:12', 'var_functions.query_db:14']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_businesses': 63, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}}

exec(code, env_args)
