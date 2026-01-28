code = """import json
import pandas as pd

# Get business data
business_file_key = 'var_functions.query_db:4'
if business_file_key in locals():
    business_file_path = locals()[business_file_key]
    with open(business_file_path, 'r') as f:
        business_data = json.load(f)
else:
    print("__RESULT__:")
    print(json.dumps("Error: Business file not found"))
    exit()

# Get review data
review_file_key = 'var_functions.query_db:14'
if review_file_key in locals():
    review_file_path = locals()[review_file_key]
    with open(review_file_path, 'r') as f:
        review_data = json.load(f)
else:
    print("__RESULT__:")
    print(json.dumps("Error: Review file not found"))
    exit()

# First, identify businesses open after 6PM on weekdays
extended_hours_businesses = {}

for business in business_data:
    try:
        gmap_id = business.get('gmap_id')
        name = business.get('name')
        hours_str = business.get('hours')
        
        if not hours_str or hours_str == 'None':
            continue
            
        hours_list = eval(hours_str)
        weekday_extended = False
        
        for day_info in hours_list:
            if len(day_info) < 2:
                continue
                
            day, time_range = day_info[0], day_info[1]
            
            if time_range == "Closed":
                continue
                
            if "Open 24 hours" in time_range:
                if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                    weekday_extended = True
                    break
                continue
            
            # Parse close time
            time_range_clean = time_range.replace('\u2013', '-')
            
            try:
                if '-' in time_range_clean:
                    close_time = time_range_clean.split('-')[1].strip()
                    
                    if 'PM' in close_time:
                        close_time_clean = close_time.replace(' ', '')
                        
                        # Extract hour part
                        if ':' in close_time_clean:
                            hour_part = close_time_clean.split(':')[0]
                            close_hour = int(hour_part)
                        else:
                            hour_part = close_time_clean.replace('PM', '')
                            close_hour = int(hour_part)
                        
                        # Convert to 24-hour format
                        if close_hour == 12:
                            close_hour_24 = 12
                        elif close_hour < 12:
                            close_hour_24 = close_hour + 12
                        else:
                            close_hour_24 = close_hour
                        
                        if close_hour_24 > 18:  # After 6 PM
                            if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                                weekday_extended = True
                                break
                                
            except:
                continue
        
        if weekday_extended:
            extended_hours_businesses[gmap_id] = {
                'name': name,
                'hours_str': hours_str
            }
            
    except:
        continue

# Calculate average ratings for these businesses
from collections import defaultdict

business_ratings = defaultdict(list)

for review in review_data:
    gmap_id = review.get('gmap_id')
    rating = review.get('rating')
    
    if gmap_id in extended_hours_businesses:
        try:
            rating_int = int(rating)
            business_ratings[gmap_id].append(rating_int)
        except:
            continue

# Calculate average ratings
business_averages = []

for gmap_id, ratings in business_ratings.items():
    if len(ratings) >= 1:  # At least one review
        avg_rating = sum(ratings) / len(ratings)
        business_averages.append({
            'gmap_id': gmap_id,
            'name': extended_hours_businesses[gmap_id]['name'],
            'hours': extended_hours_businesses[gmap_id]['hours_str'],
            'avg_rating': round(avg_rating, 2),
            'review_count': len(ratings)
        })

# Sort by average rating (descending)
business_averages.sort(key=lambda x: x['avg_rating'], reverse=True)

# Get top 5
top_5 = business_averages[:5]

print("__RESULT__:")
print(json.dumps(top_5, indent=2))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 25, 'sample': [{'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}]}, 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}], 'var_functions.execute_python:12': {'businesses': [{'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours_str': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours_str': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours_str': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours_str': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours_str': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'hours_str': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'hours_str': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'hours_str': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar', 'hours_str': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'hours_str': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'hours_str': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails', 'hours_str': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours_str': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours_str': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours_str': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]'}, {'gmap_id': 'gmap_7', 'name': "Rossy's Beauty Salon", 'hours_str': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours_str': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano', 'hours_str': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]'}, {'gmap_id': 'gmap_11', 'name': 'Paradise tattoo', 'hours_str': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]'}, {'gmap_id': 'gmap_61', 'name': 'Off The Hoof', 'hours_str': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]'}, {'gmap_id': 'gmap_55', 'name': 'Mobile Moreno Valley Dispensary', 'hours_str': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_68', 'name': 'Advanced Auto Upholstery', 'hours_str': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]'}, {'gmap_id': 'gmap_67', 'name': 'LuXe Organic Nails Boutique', 'hours_str': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'hours_str': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_60', 'name': 'The Dream Junction', 'hours_str': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}], 'gmap_ids': ['gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_11', 'gmap_61', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60'], 'count': 25}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
