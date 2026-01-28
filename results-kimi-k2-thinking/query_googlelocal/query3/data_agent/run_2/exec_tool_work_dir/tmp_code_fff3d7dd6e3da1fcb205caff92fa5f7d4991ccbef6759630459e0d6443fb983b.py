code = """import json
import pandas as pd
import re

# Load the business data
business_file = var_functions.query_db:8
with open(business_file, 'r') as f:
    business_data = json.load(f)

# Convert to DataFrame
df_business = pd.DataFrame(business_data)

# Filter out None hours
business_with_hours = df_business[df_business['hours'].notna() & (df_business['hours'] != 'None')]

print('Total businesses: ' + str(len(df_business)))
print('Businesses with hours: ' + str(len(business_with_hours)))

# Function to check if a business is open after 6PM on any weekday
def check_open_after_6pm(hours_str):
    try:
        # Parse the hours string which looks like: [["Thursday", "6:30AM–6PM"], ...]
        hours_list = eval(hours_str)
        
        # Weekdays: Monday through Friday
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day_info in hours_list:
            if len(day_info) != 2:
                continue
                
            day, hours = day_info
            # Check if it's a weekday
            if day not in weekdays:
                continue
            
            # If open 24 hours, it's after 6PM
            if hours == 'Open 24 hours':
                return True
                
            # Skip closed days
            if hours == 'Closed':
                continue
            
            # Parse hours like '6:30AM–6PM', '11AM–9:30PM', etc.
            # Look for closing time (after the dash)
            if '–' in hours:
                closing_time = hours.split('–')[1].strip()
            elif '-' in hours:
                closing_time = hours.split('-')[1].strip()
            else:
                continue
            
            # Check if closing time is after 6PM
            if 'PM' in closing_time:
                # Extract hour (before the colon if present, or the whole number)
                closing_hour_str = closing_time.replace('PM', '').strip()
                if ':' in closing_hour_str:
                    hour = int(closing_hour_str.split(':')[0])
                else:
                    hour = int(closing_hour_str) if closing_hour_str.isdigit() else 12
                
                # PM times: if hour >= 6 and hour != 12, it's after 6PM (or if it's exactly 6PM)
                if hour > 6 or (hour == 6 and ':' in closing_hour_str):
                    return True
            
    except Exception as e:
        return False
    
    return False

# Apply the function to filter businesses
business_open_late = business_with_hours[business_with_hours['hours'].apply(check_open_after_6pm)]

print('Businesses open after 6PM on weekdays: ' + str(len(business_open_late)))
print('First few businesses open after 6PM:')
for _, row in business_open_late.head().iterrows():
    print('- ' + row['name'] + ': ' + str(row['hours']))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.list_db:5': ['business_description'], 'var_functions.query_db:7': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
