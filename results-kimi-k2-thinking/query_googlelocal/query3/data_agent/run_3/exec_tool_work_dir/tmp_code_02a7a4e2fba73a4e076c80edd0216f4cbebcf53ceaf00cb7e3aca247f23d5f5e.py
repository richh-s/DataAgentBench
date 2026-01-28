code = """import json
import re

with open(var_functions.query_db:10, 'r') as f:
    businesses = json.load(f)

with open(var_functions.query_db:11, 'r') as f:
    reviews = json.load(f)

ratings_sum = {}
ratings_count = {}

for review in reviews:
    gmap_id = review['gmap_id']
    rating = int(review['rating'])
    
    if gmap_id not in ratings_sum:
        ratings_sum[gmap_id] = 0
        ratings_count[gmap_id] = 0
    
    ratings_sum[gmap_id] += rating
    ratings_count[gmap_id] += 1

avg_ratings = {}
for gmap_id in ratings_sum:
    avg_ratings[gmap_id] = ratings_sum[gmap_id] / ratings_count[gmap_id]

def is_after_6pm(time_str):
    if 'Open 24 hours' in time_str:
        return True
    
    if '–' in time_str:
        closing = time_str.split('–')[1]
    elif '-' in time_str:
        closing = time_str.split('-')[1]
    else:
        return False
    
    closing = closing.strip()
    
    try:
        if 'PM' in closing:
            closing = closing.replace('PM', '').strip()
            if ':' in closing:
                hour = int(closing.split(':')[0])
                if hour < 12:
                    hour += 12
                minute = int(closing.split(':')[1]) if ':' in closing else 0
                return hour > 18 or (hour == 18 and minute > 0)
            else:
                hour = int(closing)
                if hour < 12:
                    hour += 12
                return hour >= 19
        elif 'AM' in closing:
            return False
        else:
            return False
    except:
        return False

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
eligible_businesses = []

for business in businesses:
    gmap_id = business['gmap_id']
    hours_str = business['hours']
    
    if hours_str == 'None' or not hours_str:
        continue
    
    try:
        hours_list = eval(hours_str)
        
        open_late = False
        for day_hours in hours_list:
            if len(day_hours) >= 2:
                day = day_hours[0]
                time_range = day_hours[1]
                
                if day in weekdays and is_after_6pm(time_range):
                    open_late = True
                    break
        
        if open_late and gmap_id in avg_ratings:
            eligible_businesses.append({
                'gmap_id': gmap_id,
                'name': business['name'],
                'hours': hours_str,
                'avg_rating': round(avg_ratings[gmap_id], 2)
            })
    except:
        continue

eligible_businesses.sort(key=lambda x: x['avg_rating'], reverse=True)
top_5 = eligible_businesses[:5]

result = json.dumps(top_5, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['business_description'], 'var_functions.query_db:4': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'MISC': '{"Service options": ["In-store pickup"]}', 'state': 'Open ⋅ Closes 5PM'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.', 'num_of_reviews': '6', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"]}', 'state': 'Open ⋅ Closes 5:30PM'}], 'var_functions.query_db:5': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
