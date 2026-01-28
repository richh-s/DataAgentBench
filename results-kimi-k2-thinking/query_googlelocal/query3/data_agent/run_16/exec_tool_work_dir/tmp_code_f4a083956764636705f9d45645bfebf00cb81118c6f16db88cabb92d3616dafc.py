code = """import json
import re

# Get the business data from the query result
businesses = var_functions.query_db:10

def parse_hours(hours_str):
    """Parse hours string into a list of [day, time_range] pairs"""
    if not hours_str or hours_str == 'None':
        return []
    try:
        # The hours are stored as string representation of lists
        # Use ast.literal_eval for safe evaluation
        import ast
        return ast.literal_eval(hours_str)
    except:
        return []

def is_open_after_6pm(hours_list):
    """Check if business is open after 6PM on any weekday"""
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    for day, time_range in hours_list:
        if day in weekdays:
            # Handle "Open 24 hours" case
            if time_range == "Open 24 hours":
                return True
            
            # Extract closing time
            # Time ranges are in formats like "9AM–9:30PM" or "9AM–10PM"
            if '–' in time_range:  # en dash
                closing = time_range.split('–')[1]
            elif '-' in time_range:  # regular dash
                closing = time_range.split('-')[1]
            else:
                continue
            
            # Parse closing time
            closing = closing.strip()
            
            # Convert to 24-hour format for comparison
            if 'PM' in closing:
                # Remove PM and parse hour
                closing = closing.replace('PM', '').strip()
                if ':' in closing:
                    hour = int(closing.split(':')[0])
                    if hour != 12:
                        hour += 12
                else:
                    hour = int(closing)
                    if hour != 12:
                        hour += 12
            elif 'AM' in closing:
                closing = closing.replace('AM', '').strip()
                if ':' in closing:
                    hour = int(closing.split(':')[0])
                else:
                    hour = int(closing)
                if hour == 12:  # 12 AM is 0 hours
                    hour = 0
            else:
                # Try to parse numeric time
                try:
                    if ':' in closing:
                        hour = int(closing.split(':')[0])
                    else:
                        hour = int(re.sub(r'[^0-9]', '', closing[:2]))
                except:
                    continue
            
            # Check if open after 6PM (18:00)
            if hour >= 18:
                return True
    
    return False

# Process businesses to find those open after 6PM
open_after_6 = []
for business in businesses:
    hours_list = parse_hours(business['hours'])
    if is_open_after_6pm(hours_list):
        open_after_6.append({
            'gmap_id': business['gmap_id'],
            'name': business['name'],
            'hours': hours_list,
            'hours_raw': business['hours']
        })

# Debug info
print(f"Total businesses: {len(businesses)}")
print(f"Businesses open after 6PM: {len(open_after_6)}")

# Show first few
for b in open_after_6[:10]:
    print(f"{b['name']}: {b['hours']}")

print('__RESULT__:')
print(json.dumps(open_after_6))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:5': ['business_description'], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
