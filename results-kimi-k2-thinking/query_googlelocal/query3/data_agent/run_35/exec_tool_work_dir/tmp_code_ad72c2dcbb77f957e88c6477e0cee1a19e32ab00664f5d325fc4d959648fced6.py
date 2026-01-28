code = """import json
import re

# Load the business hours data
result = var_functions.query_db:10
if isinstance(result, str) and result.endswith('.json'):
    with open(result, 'r') as f:
        businesses = json.load(f)
else:
    businesses = result

print('Total businesses with hours:', len(businesses))

# Function to convert time to 24-hour format
def convert_to_24hour(time_str):
    if not time_str or 'Closed' in time_str:
        return None
    if '24 hours' in time_str:
        return 24
    
    # Clean the string
    time_str = str(time_str).replace('\\u2013', '-').replace('\u2013', '-')
    parts = time_str.split('-')
    if len(parts) < 2:
        return None
    
    closing = parts[1].strip()
    # Remove non-alphanumeric except colon
    closing = re.sub(r'[^a-zA-Z0-9:]', '', closing)
    
    # Match patterns: 6PM, 6:30PM, 9PM etc
    match = re.match(r'(\d{1,2})(?::(\d{2}))?(AM|PM|am|pm)?', closing)
    if not match:
        return None
    
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    ampm = match.group(3)
    
    if ampm and ampm.upper() == 'PM' and hour != 12:
        hour += 12
    elif ampm and ampm.upper() == 'AM' and hour == 12:
        hour = 0
    
    return hour + (minute / 60)

# Check which businesses are open after 6pm on weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
businesses_after_6pm = []

for business in businesses:
    gmap_id = business.get('gmap_id')
    name = business.get('name')
    hours_str = business.get('hours')
    
    if not gmap_id or not name or not hours_str or hours_str == 'None':
        continue
    
    try:
        # Parse hours JSON
        hours_data = json.loads(hours_str.replace("'", '"'))
        
        for day_entry in hours_data:
            if len(day_entry) >= 2:
                day = day_entry[0]
                time_range = day_entry[1]
                
                if day in weekdays:
                    closing_time = convert_to_24hour(time_range)
                    if closing_time is not None and closing_time >= 18:
                        businesses_after_6pm.append({
                            'gmap_id': gmap_id,
                            'name': name,
                            'hours': hours_str
                        })
                        break
    except:
        continue

print('Businesses open after 6 PM:', len(businesses_after_6pm))

# Save to file
with open('businesses_after_6pm.json', 'w') as f:
    json.dump(businesses_after_6pm, f)

result = {'count': len(businesses_after_6pm)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['review'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
