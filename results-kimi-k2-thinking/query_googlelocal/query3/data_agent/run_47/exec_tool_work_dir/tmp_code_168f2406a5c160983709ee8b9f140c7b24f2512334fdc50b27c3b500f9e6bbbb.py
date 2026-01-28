code = """import json
import pandas as pd
import re
from datetime import datetime

# Load the full result from the file
hours_data = []
filepath = var_functions.query_db:4

if isinstance(filepath, str) and filepath.endswith('.json'):
    with open(filepath, 'r') as f:
        hours_data = json.load(f)
else:
    # If it's not a filepath, it's the direct data
    hours_data = var_functions.query_db:4

print(f"Loaded {len(hours_data)} business records with hours data")

# Function to check if a business is open after 6:00 PM on any weekday
def is_open_after_6pm(hours_str):
    """
    Check if business is open after 6:00 PM on at least one weekday.
    Weekdays: Monday, Tuesday, Wednesday, Thursday, Friday
    """
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        # Parse the hours string (it's stored as a string representation of a list)
        hours_list = eval(hours_str)
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                # Check for "Open 24 hours"
                if hours == 'Open 24 hours':
                    return True
                
                # Parse closing time
                # Handle formats like "9:30AM–9:30PM", "11AM–9:30PM", "3–9PM"
                if '–' in hours:  # en dash
                    parts = hours.split('–')
                elif '-' in hours:  # regular dash
                    parts = hours.split('-')
                else:
                    continue
                
                if len(parts) >= 2:
                    open_time = parts[0].strip()
                    close_time = parts[1].strip()
                    
                    # Parse closing time
                    close_time_clean = close_time.replace(' ', '')
                    
                    # Check if PM and hour >= 6
                    if 'PM' in close_time_clean:
                        # Extract hour part
                        hour_part = close_time_clean.replace('PM', '')
                        if ':' in hour_part:
                            hour = int(hour_part.split(':')[0])
                        else:
                            hour = int(hour_part)
                        
                        # Convert 12 PM to 12 (noon), otherwise add 12
                        if hour != 12:
                            hour += 12
                        
                        if hour >= 18:  # 6 PM or later
                            return True
    except:
        # If parsing fails, skip this business
        pass
    
    return False

# Filter businesses open after 6 PM
businesses_open_late = []
for business in hours_data:
    if is_open_after_6pm(business['hours']):
        businesses_open_late.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': business['hours']
        })

print(f"Found {len(businesses_open_late)} businesses open after 6 PM on weekdays")

# Get the gmap_ids for these businesses
gmap_ids = [b['gmap_id'] for b in businesses_open_late]

# Convert to JSON-serializable format
result = {
    'businesses': businesses_open_late,
    'gmap_ids': gmap_ids
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
