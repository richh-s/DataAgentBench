code = """import json
import re

# Load business data from the file
business_data_path = locals()['var_functions.query_db:5']
if isinstance(business_data_path, str) and business_data_path.endswith('.json'):
    with open(business_data_path, 'r') as f:
        businesses = json.load(f)
else:
    businesses = locals()['var_functions.query_db:5']

print(f"Total businesses with hours data: {len(businesses)}")

# Function to check if a closing time is after 6 PM
def is_after_6pm(time_range):
    """Check if closing time is after 6:00 PM"""
    if not time_range or time_range == 'Closed' or time_range == 'Open 24 hours':
        return False
    
    if '–' not in time_range:
        return False
    
    # Extract closing time (after the dash)
    closing_time = time_range.split('–')[1].strip()
    
    # Handle 24 hours
    if closing_time == 'Open 24 hours':
        return True
    
    # Check for PM times
    if 'PM' in closing_time:
        # Extract hour part
        time_part = closing_time.replace('PM', '').strip()
        if ':' in time_part:
            hour = int(time_part.split(':')[0])
        else:
            hour = int(time_part)
        
        # Convert to 24-hour format
        if hour != 12:
            hour += 12
        
        return hour >= 18  # 6 PM or later
    
    return False

# Filter businesses open after 6 PM on weekdays
weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
filtered_businesses = []

for business in businesses:
    hours_str = business.get('hours', '')
    if hours_str and hours_str != 'None':
        try:
            # Parse hours list
            if isinstance(hours_str, str):
                hours_list = eval(hours_str)
            else:
                hours_list = hours_str
            
            # Check if open after 6 PM on any weekday
            for day_info in hours_list:
                if len(day_info) == 2:
                    day, hours = day_info
                    if day in weekdays and is_after_6pm(hours):
                        filtered_businesses.append({
                            'name': business['name'],
                            'gmap_id': business['gmap_id'],
                            'hours': hours_str
                        })
                        break
        except:
            continue

print(f"Businesses open after 6 PM on weekdays: {len(filtered_businesses)}")

# Show sample businesses
for i, biz in enumerate(filtered_businesses[:10]):
    print(f"{i+1}. {biz['name']}")

# Save results
result = {
    'businesses': filtered_businesses,
    'count': len(filtered_businesses)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
