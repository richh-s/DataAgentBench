code = """import json
import re
from datetime import datetime

# Load the business data with hours
business_file = var_functions.query_db_6
with open(business_file, 'r') as f:
    businesses = json.load(f)

print('Total businesses with hours:', len(businesses))

def parse_closing_time(time_str):
    time_str = time_str.replace('\u2013', '-').replace('\u2014', '-')
    if '-' in time_str:
        parts = time_str.split('-')
        if len(parts) >= 2:
            closing_str = parts[1].strip()
            if closing_str == "Open 24 hours":
                return datetime.strptime("23:59", "%H:%M")
            if closing_str == "Closed":
                return None
            closing_str = closing_str.upper().strip()
            for fmt in ["%I%p", "%I:%M%p"]:
                try:
                    dt = datetime.strptime(closing_str, fmt)
                    return dt
                except:
                    continue
    return None

def is_open_after_6pm_on_weekday(hours_str):
    try:
        hours_str_clean = hours_str.replace("'", '"')
        hours_list = json.loads(hours_str_clean)
        weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day_info in hours_list:
            if isinstance(day_info, list) and len(day_info) >= 2:
                day_name = day_info[0]
                hours_range = day_info[1]
                if day_name in weekday_names:
                    if hours_range and hours_range != "Closed":
                        closing_time = parse_closing_time(day_name + "-" + hours_range)
                        if closing_time:
                            if closing_time.hour > 18 or (closing_time.hour == 18 and closing_time.minute > 0):
                                return True
        return False
    except Exception as e:
        return False

open_after_6pm = []
for business in businesses:
    if is_open_after_6pm_on_weekday(business['hours']):
        open_after_6pm.append(business)

print('Businesses open after 6 PM on weekdays:', len(open_after_6pm))

for biz in open_after_6pm[:3]:
    print('-', biz['name'] + ':', biz['hours'])

result = json.dumps(open_after_6pm)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:5': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
