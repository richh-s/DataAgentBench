code = """import json
import re
from datetime import datetime

# Load business data from the file
business_data_path = locals()['var_functions.query_db:5']
if isinstance(business_data_path, str) and business_data_path.endswith('.json'):
    with open(business_data_path, 'r') as f:
        businesses = json.load(f)
else:
    businesses = locals()['var_functions.query_db:5']

print(f"Total businesses with hours data: {len(businesses)}")

# Function to parse time and check if it's after 6 PM
def is_after_6pm(time_str):
    """Check if a closing time is after 6:00 PM"""
    if not time_str or time_str == 'Closed' or time_str == 'Open 24 hours':
        return False
    
    # Match patterns like "6:30AM–6PM", "9:30PM", etc.
    # Extract the closing time (after the dash)
    if '–' in time_str:
        closing_time = time_str.split('–')[1].strip()
    else:
        closing_time = time_str.strip()
    
    # Handle 24 hours case
    if closing_time == 'Open 24 hours':
        return True
    
    # Parse time like "6PM", "9:30PM", "12AM"
    try:
        # Remove any extra whitespace
        closing_time = closing_time.strip()
        
        # Parse the time
        if ':' in closing_time:
            # Format: "9:30PM"
            time_part, period = closing_time.split('M')
            time_part = time_part.strip()
            period = period.replace('P', 'PM').replace('A', 'AM')
            if period:
                closing_time = f"{time_part}{period}"
            else:
                closing_time = f"{time_part}"
        else:
            # Format: "6PM"
            if 'PM' in closing_time or 'AM' in closing_time:
                # Already has AM/PM
                pass
            else:
                # Add PM if not present
                if closing_time.endswith('P'):
                    closing_time = closing_time.replace('P', 'PM')
                elif closing_time.endswith('A'):
                    closing_time = closing_time.replace('A', 'AM')
        
        # Standardize the format
        if 'PM' in closing_time:
            time_part = closing_time.replace('PM', '').strip()
            if ':' in time_part:
                hour, minute = map(int, time_part.split(':'))
                hour = hour + 12 if hour != 12 else hour
            else:
                hour = int(time_part)
                if hour != 12:
                    hour += 12
                minute = 0
        elif 'AM' in closing_time:
            time_part = closing_time.replace('AM', '').strip()
            if ':' in time_part:
                hour, minute = map(int, time_part.split(':'))
                hour = 0 if hour == 12 else hour
            else:
                hour = int(time_part)
                hour = 0 if hour == 12 else hour
                minute = 0
        else:
            return False
        
        # Check if after 6 PM (hour >= 18)
        return hour >= 18
        
    except Exception as e:
        print(f"Error parsing time '{time_str}': {e}")
        return False

# Weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Filter businesses that are open after 6 PM on at least one weekday
businesses_open_after_6pm = []
for business in businesses:
    hours_str = business.get('hours', '')
    if hours_str and hours_str != 'None':
        try:
            # Parse the hours list from string
            if isinstance(hours_str, str):
                hours_list = eval(hours_str)
            else:
                hours_list = hours_str
            
            # Check each day's hours
            for day_hours in hours_list:
                if len(day_hours) == 2:
                    day, hours = day_hours
                    if day in weekdays:  # Only check weekdays
                        if is_after_6pm(hours):
                            businesses_open_after_6pm.append({
                                'name': business['name'],
                                'gmap_id': business['gmap_id'],
                                'hours': hours_str,
                                'matching_day': day,
                                'matching_hours': hours
                            })
                            break  # No need to check other days for this business
        except Exception as e:
            print(f"Error processing business {business.get('name', 'Unknown')}: {e}")

print(f"Businesses open after 6 PM on weekdays: {len(businesses_open_after_6pm)}")

# Show a few examples
for i, biz in enumerate(businesses_open_after_6pm[:5]):
    print(f"{i+1}. {biz['name']} - {biz['matching_day']}: {biz['matching_hours']}")

# Save filtered businesses
result = {
    'filtered_businesses': businesses_open_after_6pm,
    'count': len(businesses_open_after_6pm)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
