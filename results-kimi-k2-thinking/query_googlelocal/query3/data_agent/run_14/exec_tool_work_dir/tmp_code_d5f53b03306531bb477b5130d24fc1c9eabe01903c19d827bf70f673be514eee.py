code = """import json
import re
from datetime import datetime

# Read the full result from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    businesses = json.load(f)

# Function to parse time from string like "9:30PM" or "9PM"
def parse_time(time_str):
    time_str = time_str.strip().upper()
    
    # Handle "Open 24 hours" case
    if "24 hours" in time_str:
        return datetime.strptime("11:59PM", "%I:%M%p").time()
    
    # Extract hour and minute
    if ':' in time_str:
        # Format: "9:30PM"
        return datetime.strptime(time_str, "%I:%M%p").time()
    else:
        # Format: "9PM"
        return datetime.strptime(time_str, "%I%p").time()

# Function to check if closing time is after 6:00 PM
def is_open_after_6pm(hours_range):
    if not hours_range or hours_range == "Closed":
        return False
    
    # Split the range, e.g., "9:30AM–9:30PM"
    if "–" in hours_range:
        times = hours_range.split("–")
    elif "-" in hours_range:
        times = hours_range.split("-")
    else:
        return False
    
    if len(times) < 2:
        return False
    
    closing_time_str = times[1].strip()
    
    try:
        closing_time = parse_time(closing_time_str)
        # Check if closing time is after 6:00 PM (18:00)
        six_pm = datetime.strptime("6:00PM", "%I:%M%p").time()
        return closing_time > six_pm
    except:
        return False

# Filter businesses that are open after 6:00 PM on at least one weekday
filtered_businesses = []
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for business in businesses:
    gmap_id = business.get("gmap_id")
    name = business.get("name")
    hours = business.get("hours")
    
    if not hours or hours == "None":
        continue
    
    try:
        hours_list = json.loads(hours.replace("'", '"'))
    except:
        hours_list = hours
    
    # Check if any weekday is open after 6 PM
    open_after_6pm = False
    for day_hours in hours_list:
        if isinstance(day_hours, list) and len(day_hours) >= 2:
            day = day_hours[0]
            hours_range = day_hours[1]
            
            if day in weekdays and is_open_after_6pm(hours_range):
                open_after_6pm = True
                break
    
    if open_after_6pm:
        filtered_businesses.append({
            "gmap_id": gmap_id,
            "name": name,
            "hours": hours
        })

print("__RESULT__:")
print(json.dumps(filtered_businesses[:10]))  # Print first 10 for preview"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74', 'description': ' This inviting eatery in La Mirada, CA 90638 serves a diverse menu of delicious dishes, perfect for casual dining and family gatherings.', 'num_of_reviews': '18', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'MISC': '{"Service options": ["Outdoor seating", "Curbside pickup", "No-contact delivery", "Delivery", "Takeout", "Dine-in"], "Health & safety": ["Mask required", "Staff wear masks", "Staff required to disinfect surfaces between visits"], "Popular for": ["Lunch", "Dinner", "Solo dining"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food", "Quick bite", "Small plates"], "Dining options": ["Lunch", "Dinner"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"], "Crowd": ["College students"]}', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.', 'num_of_reviews': '34', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'MISC': 'None', 'state': 'Open ⋅ Closes 9:30PM'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29', 'description': 'Chain selling interior & exterior paints, primers & finishes, plus supplies. This vibrant shop in Roseville, CA 95661 offers a wide variety of high-quality coatings and supplies for all your home improvement and artistic needs.', 'num_of_reviews': '26', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]', 'MISC': '{"Service options": ["Curbside pickup", "In-store pickup", "In-store shopping", "Same-day delivery"], "Accessibility": ["Wheelchair accessible entrance", "Wheelchair accessible parking lot"], "Offerings": ["Service guarantee"], "Planning": ["Quick visit"], "Payments": ["Checks", "Debit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.', 'num_of_reviews': '1', 'hours': 'None', 'MISC': 'None', 'state': 'None'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
