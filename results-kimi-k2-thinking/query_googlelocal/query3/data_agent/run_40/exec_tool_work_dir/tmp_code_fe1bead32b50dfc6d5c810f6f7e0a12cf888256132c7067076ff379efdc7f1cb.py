code = """import json
import re

# Load the data from files
businesses_data_file = var_functions.query_db:12
with open(businesses_data_file, 'r') as f:
    businesses = json.load(f)

ratings_data_file = var_functions.query_db:13
with open(ratings_data_file, 'r') as f:
    ratings = json.load(f)

# Filter businesses that are open after 6:00 PM on at least one weekday
def is_after_6pm(time_str):
    """Check if a closing time is after 6:00 PM"""
    time_str = time_str.strip()
    
    # If "Open 24 hours", it's definitely after 6 PM
    if time_str == "Open 24 hours":
        return True
    
    # If contains "AM", it's before noon (excluded)
    if "AM" in time_str:
        return False
    
    # Check for PM times
    if "PM" in time_str:
        # Remove "PM" and any non-digit/non-colon characters
        clean_time = time_str.replace("PM", "").strip()
        
        # Extract hour and minute
        if ":" in clean_time:
            hour, minute = clean_time.split(":")
            hour = int(hour)
            minute = int(minute)
        else:
            hour = int(clean_time)
            minute = 0
        
        # Convert to 24-hour format (12 PM = 12, 1 PM = 13, etc.)
        if hour != 12:
            hour += 12
            
        # Check if after 6:00 PM (18:00)
        if hour > 18 or (hour == 18 and minute > 0):
            return True
    
    return False

# Filter businesses
def closes_after_6pm(hours_str):
    """Check if a business closes after 6 PM on any weekday"""
    try:
        # Parse the hours JSON string
        if hours_str is None:
            return False
        
        hours_list = json.loads(hours_str.replace("'", '"'))
        
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        for day_info in hours_list:
            day = day_info[0]
            hours_range = day_info[1]
            
            # Skip weekends (Saturday, Sunday) and Closed days
            if day not in weekdays or hours_range in ["Closed", "Closed ", ""]:
                continue
            
            # Extract closing time (after the dash)
            if "–" in hours_range or "-" in hours_range:
                # Use unicode dash or regular dash
                if "–" in hours_range:
                    closing = hours_range.split("–")[1]
                else:
                    closing = hours_range.split("-")[1]
                
                if is_after_6pm(closing):
                    return True
        
        return False
    except Exception as e:
        return False

# Filter businesses that are open after 6 PM
filtered_businesses = []
for business in businesses:
    hours_str = business['hours']
    if hours_str and closes_after_6pm(hours_str):
        filtered_businesses.append(business)

print(f"Number of businesses that close after 6 PM on weekdays: {len(filtered_businesses)}")
print("Sample businesses:")
for i, b in enumerate(filtered_businesses[:5]):
    print(f"- {b['name']}: {b['hours']}")"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.list_db:1': ['review'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_19', 'name': 'PODS Sacramento Hub', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_48', 'name': 'State Street/7th Street', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_57', 'name': "Ely's Beauty Salon", 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_13', 'name': 'United Methodist Church', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_4', 'name': 'Lafayette Entrance 1', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_6', 'name': 'ATSI', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_10', 'name': 'Jjironwork', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_77', 'name': 'Climate Control', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_66', 'name': 'HIGHPOINTE', 'hours': 'None', 'state': 'None'}, {'gmap_id': 'gmap_73', 'name': 'CYD Works Electric', 'hours': 'None', 'state': 'Open now'}, {'gmap_id': 'gmap_54', 'name': 'Wildomar Campground', 'hours': 'None', 'state': 'None'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
