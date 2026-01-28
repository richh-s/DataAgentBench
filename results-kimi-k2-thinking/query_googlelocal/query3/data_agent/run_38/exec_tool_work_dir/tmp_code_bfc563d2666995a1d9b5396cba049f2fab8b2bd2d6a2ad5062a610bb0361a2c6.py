code = """import json
import pandas as pd
from pathlib import Path

# Read the file path from storage using locals()
file_path_key = 'var_functions.query_db:4'
if file_path_key in locals():
    file_path = locals()[file_path_key]
else:
    print("__RESULT__:")
    print(json.dumps("Error: File path not found"))
    exit()

# Read the actual data from the JSON file
with open(file_path, 'r') as f:
    business_data = json.load(f)

# Initialize a list to track businesses with extended hours
extended_hours_businesses = []

# Process each business
for business in business_data:
    try:
        gmap_id = business.get('gmap_id')
        name = business.get('name')
        hours_str = business.get('hours')
        
        if not hours_str or hours_str == 'None':
            continue
            
        # Parse the hours string which looks like: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        hours_list = eval(hours_str)
        
        # Check each day's hours
        weekday_extended = False
        weekend_extended = False
        
        for day_info in hours_list:
            if len(day_info) < 2:
                continue
                
            day = day_info[0]
            time_range = day_info[1]
            
            # Skip if closed
            if time_range == "Closed":
                continue
                
            # Check if "Open 24 hours"
            if "Open 24 hours" in time_range:
                extended_hours = True
                if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                    weekday_extended = True
                elif day in ["Saturday", "Sunday"]:
                    weekend_extended = True
                continue
            
            # Parse normal time ranges like "9AM–9:30PM" or "10AM-6PM"
            # Replace the unicode dash with a hyphen for consistent parsing
            time_range_clean = time_range.replace('\u2013', '-')
            
            # Check if there's a closing time after splitting
            try:
                if '-' in time_range_clean:
                    times = time_range_clean.split('-')
                    if len(times) >= 2:
                        close_time = times[1].strip()
                        
                        # Check if PM time > 6:00 PM
                        if 'PM' in close_time:
                            # Parse the hour part
                            close_time_no_spaces = close_time.replace(' ', '')
                            
                            if ':' in close_time_no_spaces:
                                hour_part = close_time_no_spaces.split(':')[0]
                                close_hour = int(hour_part)
                            else:
                                hour_part = close_time_no_spaces.replace('PM', '')
                                close_hour = int(hour_part)
                            
                            # Convert to 24-hour format (12 PM stays 12, 1-11 PM -> 13-23)
                            if close_hour == 12:
                                close_hour_24 = 12
                            elif close_hour < 12:
                                close_hour_24 = close_hour + 12
                            else:
                                close_hour_24 = close_hour
                            
                            # Check if closed after 6:00 PM (18:00)
                            if close_hour_24 > 18:
                                if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                                    weekday_extended = True
                                elif day in ["Saturday", "Sunday"]:
                                    weekend_extended = True
                                        
            except Exception as e:
                # Skip parsing errors
                continue
        
        # If the business has weekday extended hours (open after 6PM), add it
        if weekday_extended:
            extended_hours_businesses.append({
                'gmap_id': gmap_id,
                'name': name,
                'hours': hours_str
            })
            
    except Exception as e:
        # Skip any businesses that cause parse errors
        continue

result_preview = {
    'count': len(extended_hours_businesses),
    'sample': extended_hours_businesses[:3]
}

print("__RESULT__:")
print(json.dumps(result_preview))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
