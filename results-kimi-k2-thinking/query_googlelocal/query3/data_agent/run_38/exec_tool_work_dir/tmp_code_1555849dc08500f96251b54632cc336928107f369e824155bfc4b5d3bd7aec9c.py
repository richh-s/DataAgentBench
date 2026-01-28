code = """import json
import pandas as pd

# Get the extended hours businesses data
file_path_key = 'var_functions.query_db:4'
if file_path_key in locals():
    file_path = locals()[file_path_key]
    with open(file_path, 'r') as f:
        business_data = json.load(f)
else:
    print("__RESULT__:")
    print(json.dumps("Error: File not found"))
    exit()

# Find all businesses open after 6PM on weekdays
extended_hours_businesses = []

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
            
            time_range_clean = time_range.replace('\u2013', '-')
            
            try:
                if '-' in time_range_clean:
                    times = time_range_clean.split('-')
                    if len(times) >= 2:
                        close_time = times[1].strip()
                        
                        if 'PM' in close_time:
                            close_time_clean = close_time.replace(' ', '')
                            
                            if ':' in close_time_clean:
                                hour_part = close_time_clean.split(':')[0]
                                close_hour = int(hour_part)
                            else:
                                hour_part = close_time_clean.replace('PM', '').replace(':', '')
                                close_hour = int(hour_part)
                            
                            if close_hour == 12:
                                close_hour_24 = 12
                            elif close_hour < 12:
                                close_hour_24 = close_hour + 12
                            else:
                                close_hour_24 = close_hour
                            
                            if close_hour_24 > 18:
                                if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                                    weekday_extended = True
                                    break
                                        
            except:
                continue
        
        if weekday_extended:
            extended_hours_businesses.append({
                'gmap_id': gmap_id,
                'name': name,
                'hours_str': hours_str
            })
            
    except:
        continue

# Get unique gmap_ids
business_gmap_ids = [b['gmap_id'] for b in extended_hours_businesses]

result = {
    'businesses': extended_hours_businesses,
    'gmap_ids': business_gmap_ids,
    'count': len(extended_hours_businesses)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None', 'state': 'Open now'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'state': 'Open ⋅ Closes 6PM'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'state': 'Open ⋅ Closes 5PM'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 25, 'sample': [{'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}]}, 'var_functions.query_db:10': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}]}

exec(code, env_args)
