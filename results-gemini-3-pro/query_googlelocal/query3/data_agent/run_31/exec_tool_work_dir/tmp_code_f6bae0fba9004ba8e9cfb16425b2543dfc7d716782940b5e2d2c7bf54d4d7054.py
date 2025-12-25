code = """import json
import ast
import pandas as pd

# Load data
with open('var_function-call-1762609296451302444.json', 'r') as f:
    businesses = json.load(f)

with open('var_function-call-1762609296451304817.json', 'r') as f:
    reviews = json.load(f)

# Create DataFrame for reviews
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].mean().to_dict()

# Helper function to parse time
def to_24hr(time_str):
    # time_str examples: "6PM", "6:30PM", "12AM", "12:30AM", "11AM"
    if not time_str:
        return None
    time_str = time_str.strip()
    is_pm = 'PM' in time_str
    is_am = 'AM' in time_str
    
    # Remove AM/PM
    t = time_str.replace('PM', '').replace('AM', '').strip()
    
    parts = t.split(':')
    h = int(parts[0])
    m = int(parts[1]) if len(parts) > 1 else 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == 'None':
        return False
    
    try:
        hours_list = ast.literal_eval(hours_str)
    except:
        return False
        
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    
    for day_info in hours_list:
        if len(day_info) != 2:
            continue
        day, time_range = day_info
        
        if day in weekdays:
            if time_range == "Open 24 hours":
                return True
            if time_range == "Closed":
                continue
            
            # Split range
            # Range usually contains en-dash \u2013
            if '\u2013' in time_range:
                parts = time_range.split('\u2013')
            elif '-' in time_range:
                parts = time_range.split('-')
            else:
                continue
            
            if len(parts) != 2:
                continue
            
            end_time = parts[1] # e.g. "6PM", "9:30PM"
            
            # Parse end time
            minutes_from_midnight = to_24hr(end_time)
            
            if minutes_from_midnight is None:
                continue
                
            # 6:00 PM is 18:00 = 18 * 60 = 1080 minutes
            # We want AFTER 6:00 PM, so > 1080
            # Special case: Closing at 12AM, 1AM, 2AM etc. (next day)
            # If minutes < 1080, it might be next day (morning) or early afternoon.
            # But usually "9AM-5PM" -> 17:00 (1020). Not open after 6PM.
            # "11AM-2AM" -> 2AM is 2*60 = 120. 
            # Logic: If closing time is AM (and not 12PM/noon) or closing time > 6PM (18:00).
            # Wait, 12AM is 0. 1AM is 60.
            # If closing time is early morning (0 to say 11AM?), it means it stayed open past midnight.
            # If closing time is between 6:01 PM and 11:59 PM, it's open after 6PM.
            
            # Let's simplify:
            # If closing time is PM and > 6PM?
            # 6PM = 1080 min.
            # 5PM = 1020 min.
            # 7PM = 1140 min.
            # If time > 1080 (18:00), it's after 6PM.
            # If time < 1080:
            #   Could be AM (next day). e.g. 2AM.
            #   Could be PM (afternoon). e.g. 5PM.
            #   How to distinguish?
            #   Usually opening hours like "5PM-2AM".
            #   If closing time is AM (0-11:59), it's generally effectively "late" (next day), so certainly open after 6PM of the previous day.
            #   Unless it's a breakfast place "6AM-11AM". Closing at 11AM is not after 6PM.
            #   We need to compare with opening time? 
            #   But looking at samples: "11AM-9:30PM", "9:30AM-10PM".
            #   Closing times are explicit.
            #   If closing time is "AM" (00:00 to 11:59), we need to be careful.
            #   However, most businesses open during the day. If they close in AM, it's late night.
            #   If they close in PM, check if > 6PM.
            
            is_am = 'AM' in end_time
            is_pm = 'PM' in end_time
            
            val = minutes_from_midnight
            
            if is_pm:
                # If PM, must be > 6:00 PM (18:00) => > 1080 minutes
                # 12 PM is noon (720). 1 PM is 13:00.
                if val > 1080:
                    return True
                # If 12PM (noon) <= val <= 6PM, then No.
            elif is_am:
                # If AM, it's either morning or late night.
                # If it's 12AM (0), 1AM, 2AM... it's late night => Open after 6PM.
                # If it's 11AM, it's morning.
                # How to distinguish?
                # Usually standard businesses don't operate 5PM to 11AM (next day) without being 24h.
                # But let's look at start time?
                # Start: "6AM-11AM" -> Closes 11AM. No.
                # Start: "5PM-2AM" -> Closes 2AM. Yes.
                # Assume if closing time is between 00:00 and 05:00 (5AM), it is late night.
                # If closing time is 6AM - 11AM, it's morning shift.
                # This is a heuristic.
                # Alternatively, check opening time.
                start_time = parts[0]
                start_val = to_24hr(start_time)
                
                # If close time < start time (crossing midnight), then yes, open past 6PM (unless start time is also past 6PM? No, if it crosses midnight it covers 6PM to midnight usually? No. "3AM - 5AM" crosses nothing. "11PM - 4AM" -> open after 6PM? Yes, 11PM is > 6PM.)
                
                # Case: "11AM - 2AM". Start=660, End=120. End < Start. Crosses midnight. 
                # Does it cover "after 6PM"?
                # If Start < 18:00 (6PM), and it crosses midnight, it definitely is open at 6PM and after.
                # If Start > 18:00 (e.g. 8PM), it is open after 6PM.
                
                if val < start_val:
                    # Crosses midnight
                    return True
                else:
                    # Same day. e.g. "6AM - 11AM".
                    # Is End > 18:00?
                    # 11AM is 660. 18:00 is 1080. No.
                    if val > 1080:
                        return True
            
    return False

filtered_businesses = []
for b in businesses:
    if b['gmap_id'] in avg_ratings:
        if is_open_after_6pm(b['hours']):
            b['avg_rating'] = avg_ratings[b['gmap_id']]
            filtered_businesses.append(b)

# Sort by avg_rating desc
# If tie, maybe sort by name or review count? Prompt says "ranked by highest average rating". 
# Let's sort by rating desc.
filtered_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)

top_5 = filtered_businesses[:5]

# Format output
result = []
for b in top_5:
    result.append({
        "name": b['name'],
        "hours": b['hours'],
        "average_rating": round(b['avg_rating'], 2) # rounding for display
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3497092084826213214': ['business_description'], 'var_function-call-3497092084826212987': ['review'], 'var_function-call-11064619406107204210': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_function-call-11064619406107202835': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-17921115159587230610': [{'count': '79'}], 'var_function-call-17921115159587232363': [{'COUNT(*)': '2000'}], 'var_function-call-1762609296451302444': 'file_storage/function-call-1762609296451302444.json', 'var_function-call-1762609296451304817': 'file_storage/function-call-1762609296451304817.json'}

exec(code, env_args)
