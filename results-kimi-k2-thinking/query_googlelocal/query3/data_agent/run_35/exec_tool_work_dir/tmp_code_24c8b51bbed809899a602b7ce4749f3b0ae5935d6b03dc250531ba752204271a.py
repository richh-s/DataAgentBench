code = """import json
import re
from datetime import datetime

# Load the business hours data
result_key = 'var_functions.query_db:5'
if result_key in locals():
    result = locals()[result_key]
    if isinstance(result, str) and result.endswith('.json'):
        # Load from file
        with open(result, 'r') as f:
            businesses = json.load(f)
    else:
        businesses = result
else:
    businesses = []

print(f"Total businesses with hours: {len(businesses)}")

# Function to parse closing time and check if it's after 6 PM
def parse_closing_time(time_str):
    """Parse time string and return hour in 24-hour format"""
    if not time_str or time_str.strip() == '':
        return None
    
    # Handle various formats like "6PM", "6:30PM", "6:30 PM", "18:30", "18:30PM"
    time_str = time_str.strip().replace('\u2013', '-').replace('\u2019', '')
    
    # Check for "Open 24 hours"
    if '24 hours' in time_str:
        return 24  # Consider 24 hours as after 6 PM
    
    # Check for "Closed"
    if 'Closed' in time_str:
        return None
    
    # Extract time range (format: "9AM-6PM" or "9AM–6PM")
    if '-' in time_str:
        parts = time_str.split('-')
        if len(parts) >= 2:
            # Get closing time
            closing = parts[1].strip()
        else:
            return None
    else:
        closing = time_str.strip()
    
    # Remove non-alphanumeric except colon and AM/PM
    closing = re.sub(r'[^a-zA-Z0-9:]', '', closing)
    
    # Parse the closing time
    pattern = r'(\d{1,2})(?::(\d{2}))?\s*(AM|PM|am|pm)?'
    match = re.match(pattern, closing)
    
    if not match:
        return None
    
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    ampm = match.group(3).upper() if match.group(3) else None
    
    # Convert to 24-hour format
    if ampm == 'PM' and hour != 12:
        hour += 12
    elif ampm == 'AM' and hour == 12:
        hour = 0
    
    return hour + minute / 60

# Function to check if business is open after 6 PM on weekdays
def is_open_after_6pm(hours_list):
    """Check if business is open after 6 PM on any weekday (Mon-Fri)"""
    if not hours_list or hours_list == 'None':
        return False
    
    try:
        # Parse hours string into list
        if isinstance(hours_list, str):
            hours_data = json.loads(hours_list.replace("'", '"'))
        else:
            hours_data = hours_list
        
        # Weekdays to check
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_hours in hours_data:
            if len(day_hours) >= 2:
                day = day_hours[0]
                time_range = day_hours[1]
                
                # Check if it's a weekday
                if day in weekdays:
                    # Parse closing time
                    closing_hour = parse_closing_time(time_range)
                    
                    # Check if closing is after 6 PM (18:00)
                    if closing_hour is not None and closing_hour >= 18:
                        return True
        
        return False
    except:
        return False

# Find businesses open after 6 PM
businesses_after_6pm = []
for business in businesses:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours = business.get('hours')
    
    if gmap_id and name and is_open_after_6pm(hours):
        businesses_after_6pm.append({
            'gmap_id': gmap_id,
            'name': name,
            'hours': hours
        })

print(f"Businesses open after 6 PM on weekdays: {len(businesses_after_6pm)}")

# Save the list to a file for later use
with open('businesses_after_6pm.json', 'w') as f:
    json.dump(businesses_after_6pm, f)

print('__RESULT__:')
print(json.dumps(businesses_after_6pm[:5]))  # Print first 5 as preview"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review']}

exec(code, env_args)
